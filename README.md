# pyramid-learning-journal

Personal learning journal using bootstrap css and some basic bootstrap blog html.

This site is deployed to Heroku at:
https://creepy-barrow-47862.herokuapp.com/

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