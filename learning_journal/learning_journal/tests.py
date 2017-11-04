"""."""
from pyramid import testing
from learning_journal.models import Journal
from learning_journal.models.meta import Base
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
    new_entry = Jou
