"""."""

from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest, HTTPFound
from learning_journal.data.data import journal_dict
from learning_journal.models import Journal


@view_config(route_name='home',
             renderer="learning_journal:templates/index.jinja2")
def list_entry(request):
    """Render a list of all entries to home page."""
    entries = request.dbsession.query(Journal).all()
    entries = sorted([entry.to_dict() for entry in entries], key=lambda x: x['id'], reverse=True)
    return {
        "journals": entries
    }


@view_config(route_name='detail_view',
             renderer="learning_journal:templates/details.jinja2")
def detail_view(request):
    """Render a detailed view of the entry clicked on."""
    journal_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(journal_id)
    return {
        'entry': entry.to_dict()
    }
    raise HTTPNotFound


@view_config(route_name='new_entry',
             renderer="learning_journal:templates/create.jinja2")
def new_entry(request):
    """Can add a new entry and it adds it the database."""
    if request.method == 'GET':
        return {}

    if request.method == 'POST':
        if not all([field in request.POST for field in ['title', 'content']]):
            return HTTPBadRequest
        now = datetime.now()
        new_entry = Journal(
            title=request.POST['title'],
            date=now.strftime("%B %d, %Y"),
            body=request.POST['content']
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('home'))


@view_config(route_name='update',
             renderer="learning_journal:templates/edit.jinja2")
def update(request):
    """Update journal entry and persist the data."""
    journal_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(journal_id)
    if not entry:
        raise HTTPFound

    if request.method == 'GET':
        return {
            'entry': entry.to_dict()
        }
    now = datetime.now()
    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.date = now.strftime("%B %d, %Y")
        entry.body = request.POST['content']
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=entry.id))
