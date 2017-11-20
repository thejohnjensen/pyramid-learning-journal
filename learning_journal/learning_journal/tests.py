"""Testing module for pyramid learning journal."""
from pyramid import testing
from learning_journal.models import Journal
from learning_journal.models.meta import Base
from learning_journal.data.data import journal_dict
from pyramid.httpexceptions import HTTPNotFound
import pytest


@pytest.fixture
def configuration(request):
    """Point to the database."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/learning_journal'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session to interact with database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)
    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Set up a fake HTTP request with dbsession."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_list(dummy_request):
    """Test that list_view returns a list."""
    from learning_journal.views.default import list_entry
    response = list_entry(dummy_request)
    assert isinstance(response['journals'], list)


def test_list_view_returns_my_data(dummy_request):
    """Test that my data is coming back."""
    from learning_journal.views.default import list_entry
    for entry in journal_dict:
        new_entry = Journal(
            title=entry['title'],
            date=entry['date'],
            body=entry['body']
        )
        dummy_request.dbsession.add(new_entry)
        dummy_request.dbsession.commit()
    response = list_entry(dummy_request)
    for index, entry in enumerate(response['journals']):
        assert entry['title'] == 'Class: {}'.format(index + 1)


def test_detail_view_returns_correct_details(dummy_request):
    """Test that the detail page returns the correct details."""
    from learning_journal.views.default import detail_view
    for entry in journal_dict[::-1]:
        new_entry = Journal(
            title=entry['title'],
            date=entry['date'],
            body=entry['body']
        )
        dummy_request.dbsession.add(new_entry)
        dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert response['entry']['id'] == 1


def test_create_new_entry(dummy_request):
    """Test that a new entry is created."""
    from learning_journal.views.default import new_entry
    for entry in journal_dict[::-1]:
        create_entry = Journal(
            title=entry['title'],
            date=entry['date'],
            body=entry['body']
        )
        dummy_request.dbsession.add(create_entry)
        dummy_request.dbsession.commit()
    entry_info = {
        "title": "Class: 14",
        "content": "This entry is to test new entry function"
    }
    dummy_request.method = "POST"
    dummy_request.POST = entry_info
    new_entry(dummy_request)
    entry = dummy_request.dbsession.query(Journal).all()
    temp = len(entry) - 1
    this = entry[temp].to_dict()
    assert this['title'] == 'Class: 14'


def test_update_entry(dummy_request):
    """Test that an entry can be updated and saved in db."""
    from learning_journal.views.default import update
    for entry in journal_dict[::-1]:
        create_entry = Journal(
            title=entry['title'],
            date=entry['date'],
            body=entry['body']
        )
        dummy_request.dbsession.add(create_entry)
        dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 17
    new_info = {
        "title": "Updated, Ehh!?",
        "content": "Hellz yeah!"
    }
    dummy_request.method = "POST"
    dummy_request.POST = new_info
    update(dummy_request)
    entry = dummy_request.dbsession.query(Journal).all()
    journal_len = len(entry) - 1
    assert entry[journal_len].title == "Updated, Ehh!?"


