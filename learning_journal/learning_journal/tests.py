"""."""
from pyramid.testing import DummyRequest
import pytest


def test_getting_html_list_view_status_code():
    """."""
    from learning_journal.views.default import list_view
    req = DummyRequest()
    response = list_view(req)
    assert response.status_code == 200


def test_getting_html_detail_view_status_code():
    """."""
    from learning_journal.views.default import detail_view
    req = DummyRequest()
    response = detail_view(req)
    assert response.status_code == 200


def test_getting_html_create_view_status_code():
    """."""
    from learning_journal.views.default import create_view
    req = DummyRequest()
    response = create_view(req)
    assert response.status_code == 200


def test_getting_html_update_view_status_code():
    """."""
    from learning_journal.views.default import update_view
    req = DummyRequest()
    response = update_view(req)
    assert response.status_code == 200


def test_getting_html_list_view_contains_unique_text():
    """."""
    from learning_journal.views.default import list_view
    req = DummyRequest()
    response = list_view(req)
    assert '<h2 class="blog-post-title">Sample blog post</h2>' in response.ubody


def test_getting_html_detail_view_unique_text():
    """."""
    from learning_journal.views.default import detail_view
    req = DummyRequest()
    response = detail_view(req)
    assert '<h1>Learning Journal: Class 11</h1>' in response.ubody


def test_getting_html_create_view_unique_text():
    """."""
    from learning_journal.views.default import create_view
    req = DummyRequest()
    response = create_view(req)
    assert '<h1 class="blog-title">Create New Learning Journal Entry</h1>' in response.ubody


def test_getting_html_update_view_unique_text():
    """."""
    from learning_journal.views.default import update_view
    req = DummyRequest()
    response = update_view(req)
    assert '<h1 class="blog-title">Update Learning Journal</h1>' in response.ubody