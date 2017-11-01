from pyramid.response import Response
import os

HERE = os.path.abspath(__file__)
TEMPLATES = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'templates')
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')

def list_view(request):
    """."""
    with open(os.path.join(TEMPLATES, 'index.html')) as file:
        return Response(file.read())


def detail_view(request):
    """."""
    with open(os.path.join(DATA, 'data.html')) as file:
        return Response(file.read())

def create_view(request):
    """."""
    with open(os.path.join(TEMPLATES, 'create.html')) as file:
        return Response(file.read())

def update_view(request):
    """."""
    with open(os.path.join(TEMPLATES, 'edit.html')) as file:
        return Response(file.read())