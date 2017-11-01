from .default import list_view
from .default import create_view
from .default import detail_view
from .default import update_view

def includeme(config):
    """Add views to our configuration."""
    config.add_view(list_view, route_name='home')
    config.add_view(detail_view, route_name='detail_view')
    config.add_view(create_view, route_name='new_entry')
    config.add_view(update_view, route_name='update')