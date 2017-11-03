# pyramid-learning-journal

Personal learning journal using bootstrap css and some basic bootstrap blog html.
The webpage is deployed to heroku at https://creepy-barrow-47862.herokuapp.com/

**Uses the following routes:**
`    config.add_route('home', '/')`
`    config.add_route('detail_view', '/journal/{id:\d+}')`
`    config.add_route('new_entry', '/journal/new_entry')`
`    config.add_route('update', '/journal/{id:\d+}/update')`