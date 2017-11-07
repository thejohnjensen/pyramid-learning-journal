import os
import sys
import transaction
from learning_journal.data.data import journal_dict

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models import Journal
from datetime import datetime


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    settings['sqlalchemy.url'] = os.environ["DATABASE_URL"]
    engine = get_engine(settings)
    Base.metadata.create_all(engine)

 # ---- NOTHING BELOW THIS POINT IS NECESSARY UNLESS YOU WANT TO START WITH A NEW MODEL INSTANCE -----

    session_factory = get_session_factory(engine)

    # with transaction.manager:
    #     dbsession = get_tm_session(session_factory, transaction.manager)

    #     all_entries = []
    #     for entry in journal_dict[::-1]:
    #         all_entries.append(
    #             Journal(
    #                 title=entry['title'],
    #                 date=entry['date'],
    #                 body=entry['body']
    #             )
    #         )

    #     dbsession.add_all(all_entries)
