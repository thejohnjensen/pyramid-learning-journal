"""Test module."""
from pyramid.testing import DummyRequest
from pyramid.httpexceptions import HTTPNotFound
import pytest


@pytest.fixture
def dummy_request():
    """Create the dummy request fixture so we can reuse it."""
    return DummyRequest()


def test_getting_all_entry_data_in_list_view(dummy_request):
    """Test that my list response returns all my data in journal_dict."""
    from learning_journal.views.default import list_entry
    from learning_journal.data.data import journal_dict
    response = list_entry(dummy_request)
    assert response['journals'] == journal_dict


def test_getting_html_list_view_data(dummy_request):
    """Test that getting back expected dictionary with my journals."""
    from learning_journal.views.default import list_entry
    response = list_entry(dummy_request)
    assert response['journals'][0]['id'] == 12


def test_getting_html_detail_view_data(dummy_request):
    """Test that we get the correct data back for id."""
    from learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 12
    response = detail_view(dummy_request)
    assert 'Class 12' in response['entry']['title']


def test_getting_html_detail_view_data_not_found(dummy_request):
    """Test that we get the correct data back for id."""
    from learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 22
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_create_new_entry_form_is_returned(dummy_request):
    """Test that the create new form page renders."""
    from learning_journal.views.default import new_entry
    response = new_entry(dummy_request)
    assert response['title'] == 'Title'
