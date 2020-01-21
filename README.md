# pyramid-learning-journal

**Authors:** John Jensen and [Adrienne Karnoski](https://github.com/adriennekarnoski)

**Deployed At:** https://creepy-barrow-47862.herokuapp.com/

Personal learning journal blog built on [pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/#) web framework and [cookiecutter-alchemy](https://github.com/Pylons/pyramid-cookiecutter-alchemy) template. Using bootstrap template css.

**Uses the following routes:**

| Route | Route Name | Description |
| --- | --- | --- |
| `/` | home | shows a list view of all my journal entries |
| `/journal/new_entry` |  new_entry | create a new journal entry |
| `/journal/{id:\d+}` | detail_view | show the full details of an entry |
| `/journal/{id:\d+}/update` | update | edit the selected entry |


**Getting Started**
- Clone the repo: copy the link from this repo.
    `$ git clone <link>`

- Change directory into your newly created project.
    `$ cd pyramid_learning_journal`

- Create a Python virtual environment.
    `$ python3 -m venv env`

- Change directory into `learning_journal`

- Upgrade packaging tools.
    `learning_journal $ pip install --upgrade pip setuptools`

- Install the project in editable mode with its testing requirements.
    `learning_journal $ pip install -e ".[testing]"`

- Create a database with [postgresSQL](https://www.postgresql.org/).
    `$ createdb learning_journal`

- Configure the database.
    `learning_journal $ initialize_db development.ini`

- Run your project's tests.
    `learning_journal $ pytest`

- Run your project.
    `$ pserve development.ini`


#Testing Plan

* Test each of the view functions:
    * Test that list_entry returns the list of journal entries.
    * Test that list_entry returns the data I inteded for.
    * Test that detail view shows the details for the correct journal entry.
    * Test that creating a new entry creates the entry intended and persists the data in database.
    * Test getting an entry, edit it, and commit it to the database.



**STEP 1:**

| Name |                                       Stmts |  Miss | Cover |
| --- | --- | --- | --- |
| learning_journal/__init__.py        |           9   |   7  |  22%
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

