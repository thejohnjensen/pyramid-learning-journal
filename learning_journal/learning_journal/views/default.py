from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.data.data import journal_dict


@view_config(route_name='home',
             renderer="learning_journal:templates/index.jinja2")
def list_entry(request):
    """Function that renders the view of the home page."""
    return {
        "journals": journal_dict
    }


@view_config(route_name='detail_view',
             renderer="learning_journal:templates/details.jinja2")
def detail_view(request):
    """Render the detail view of one journal entry."""
    journal_id = int(request.matchdict['id'])
    if journal_id < 0 or journal_id > len(journal_dict):
        raise HTTPNotFound
    entry = list(filter(lambda journal_dict: journal_dict['id'] == journal_id, journal_dict))[0]
    return {
        'entry': entry
    }


@view_config(route_name='new_entry',
             renderer="learning_journal:templates/create.jinja2")
def new_entry(request):
    """Render the page for creating a new entry."""
    return {
        'title': 'Title'
    }
