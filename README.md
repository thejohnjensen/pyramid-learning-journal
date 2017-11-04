# pyramid-learning-journal

Personal learning journal using bootstrap css and some basic bootstrap blog html.
The webpage is deployed to heroku at https://creepy-barrow-47862.herokuapp.com/

**Uses the following routes:**
`    config.add_route('home', '/')`
`    config.add_route('detail_view', '/journal/{id:\d+}')`
`    config.add_route('new_entry', '/journal/new_entry')`
`    config.add_route('update', '/journal/{id:\d+}/update')`


**Getting Started**
- Change directory into your newly created project.
    `cd learning_journal`

- Create a Python virtual environment.
    `python3 -m venv env`

- Upgrade packaging tools.
    `env/bin/pip install --upgrade pip setuptools`

- Install the project in editable mode with its testing requirements.
    `env/bin/pip install -e ".[testing]"`

- Configure the database.
    `env/bin/initialize_learning_journal_db development.ini`

- Run your project's tests.
    `env/bin/pytest`

- Run your project.
    `env/bin/pserve development.ini`


**STEP 1:**
---------- coverage: platform darwin, python 3.6.3-final-0 -----------
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
learning_journal/__init__.py                   9      7    22%
learning_journal/models/__init__.py           24     14    42%
learning_journal/models/meta.py                5      0   100%
learning_journal/models/mymodel.py             8      0   100%
learning_journal/routes.py                     6      5    17%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/initializedb.py      26     16    38%
learning_journal/views/__init__.py             9      4    56%
learning_journal/views/default.py             17      0   100%
learning_journal/views/notfound.py             4      2    50%
--------------------------------------------------------------
TOTAL                                        108     48    56%

**STEP 2:**
---------- coverage: platform darwin, python 3.6.3-final-0 -----------
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
learning_journal/__init__.py                   8      6    25%
learning_journal/data/__init__.py              0      0   100%
learning_journal/data/data.py                  3      0   100%
learning_journal/models/__init__.py           24     14    42%
learning_journal/models/meta.py                5      0   100%
learning_journal/models/mymodel.py             8      0   100%
learning_journal/routes.py                     6      5    17%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/initializedb.py      26     16    38%
learning_journal/views/__init__.py             0      0   100%
learning_journal/views/default.py             19      5    74%
learning_journal/views/notfound.py             4      2    50%
--------------------------------------------------------------
TOTAL                                        103     48    53%

**STEP 3:**


**STEP 4:**
Test Coverage:
---------- coverage: platform darwin, python 3.6.3-final-0 -----------
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
learning_journal/__init__.py                  10      7    30%
learning_journal/data/__init__.py              0      0   100%
learning_journal/data/data.py                  3      0   100%
learning_journal/models/__init__.py           24      3    88%
learning_journal/models/meta.py                5      0   100%
learning_journal/models/mymodel.py            14      2    86%
learning_journal/routes.py                     6      0   100%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/initializedb.py      31     19    39%
learning_journal/views/__init__.py             0      0   100%
learning_journal/views/default.py             39      5    87%
learning_journal/views/notfound.py             4      2    50%
--------------------------------------------------------------
TOTAL                                        136     38    72%

