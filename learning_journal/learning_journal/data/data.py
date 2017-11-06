from datetime import datetime



FMT = '%m/%d/%Y'
journal_dict = [
    {
        'title': 'Class: 15',
        'date': datetime.strptime('11/3/2017', FMT).date(),
        'body': 'Today we had a review of pyramid which was very much needed. I feel like i have a much better understanding of it now, starting step 4 I now understand step 2...I think thats how it\'s supposed to be. Also finished up the graph, I want to do some research to see what the best practices are fore implementing it.'
    },
    {
        'title': 'Class: 14',
        'date': datetime.strptime('11/2/2017', FMT).date(),
        'body': 'Finished up the priority queue data structure assignment. Ended up using a dictionary which made it much easier than how we tried to build initially with a linked list. Continued working on the pyramid learning journal. Went back and watched some of the previous videos and its crazy how much more sense it makes once I\'ve tried to code it and broke it several times. TESTS! How?'
    },
    {
        'title': 'Class: 13',
        'date': datetime.strptime('11/1/2017', FMT).date(),
        'body': 'I finally got my jinja templates to display properly. Seriously needed to map out the path of the name to route to function to data in order to figure it out. Starting to connect to sql...my brains not ready for this. Real firehose type of a day.'
    },
    {
        'title': 'Class: 12',
        'date': datetime.strptime('10/31/2017', FMT).date(),
        'body': 'Today we added another data structure to our knowledge - binary heap. \
        We eventual got it and the tests passing but I don\'t think our \
        solution is very efficient. Our code was pretty modular though \
        but I think we could reduce our lines of code significantly. I \
        didn\'t get around to the Jinja assignment but I did get my pyramid \
        site deployed to heroku which was good.'
    },
    {
        'title': 'Class: 11',
        'date': datetime.strptime('10/30/2017', FMT).date(),
        'body': 'Today I am learning pyramid! Like right now, as I type. I now have a better understanding of how pyramid takes a request from the routes module, uses the config module to connect that route with the function in the default.py view folder. This is thanks to my paired programming partner Adrienne, she explained it to me.'
    },
    {
        'title': 'Class: 10',
        'date': datetime.strptime('10/27/2017', FMT).date(),
        'body': "Had a long morning of code review, got a good example of why test coverage isn't indicative of good tests. Can have great coverage but still have some problems with functionality. White board challenge was good but couldn't get the O(n) solution, once I saw it though I was impressed by it's simplicity. Getting the http client to stop receiving from the server based on content length...wtf, stuck on that. I can get the content length send from the server but handling it and making it be useful is beyond me right now."
    },
    {
        'title': 'Class: 9',
        'date': datetime.strptime('10/26/2017', FMT).date(),
        'body': "Today we covered the queue data structure. We made it pretty much just by inheriting methods from our double linked list. We also talked about concurrency: - multithreading -multiprocessing -async We also covered how you can make methods read only or assign them as setter. I learned more about using the python debugger and commands to use while in it.",
    },
    {
        'title': 'Class: 8',
        'date': datetime.strptime('10/25/2017', FMT).date(),
        'body': "Today we went over: - Super class: another way (albeit different with its own idiosyncrasies) to manage inheriting methods from a parent or sibling class. Watching the youtube video linked in the reading showed how python super differs from the super method in other languages in that the MRO is based off of the parents children instead of just the current classes parent class. Meaning I can access my parents other child classes I guess. -pytest fixtures: a way to make tests more dry. Can also be useful for testing across different projects if the same fixtures can be reused. -Doubly linked list: A variation of linked list but with a previous pointer, tail, and append method. Really probably one of the best days of coding so far. Things seemed to really click with the data structures lab and the white boarding went well although getting started was pretty tough, once we got going we made good progress. First day of proper TDD also, writing tests first and then building out functions is definitely the way to go, so useful once you get the hang of it.",
    },
    {
        'title': 'Class: 7',
        'date': datetime.strptime('10/24/2017', FMT).date(),
        'body': "Learning more about web sockets and HTTP protocol. One thing I really liked while doing the reading for the quiz was a link to another tutorial by jmarshal for parsing CGI, and to my surprise, we had basically already done that during our gist exercise.",
    },
    {
        'title': 'Class: 6',
        'date': datetime.strptime('10/23/2017', FMT).date(),
        'body': "Today we continued covering the basics of python. We got into the basics of object oriented programming with classes. Still trying to get the hang of using them but it'll come with practice. We also talked about data structures and had our first data structures assignment: linked lists. During code review I learned about the zip method and isinstance().,"
    },
    {
        'title': 'Class: 5',
        'date': datetime.strptime('10/21/2017', FMT).date(),
        'body': "Worked on code wars katas today. Learned how to use Tox to cross platform test python2 and 3. Gained more experience just writing tests in general which was good. Python 2 and python3 have a different default type with single (/ vs //) division. Python2 defaults truncate to int while python3 defaults to float.",
    },
    {
        'title': 'Class: 4',
        'date': datetime.strptime('10/20/2017', FMT).date(),
        'body': "Today we learned about lambda functions and how to use them, how to use exception handling, more on mutability, map, and a bunch more. During the lab I became much more familiar with system.py and running code from the command line. We covered testing with Tox but I didnt get around to using it in the lab yet.",
    },
    {
        'title': 'Class: 3',
        'date': datetime.strptime('10/19/2017', FMT).date(),
        'body': "We covered a ton today; starting with the code review I learned quite a bit about using pytest, pytest coverage, pytest verbose and how to ignore part of your code for the test. Then covered sequence data types; lists, tuples, strings. Also, dir() will provide a list of methods for that type which is great to know right now. Talked about unicode and byte strings and their differences. String concat, need to break away from 'string' + 'string2'. Dictionaries time comp: O(1) when looking up a key. How to open up a file, and run a function from the command line...all good stuff.,"
    },
    {
        'title': 'Class: 2',
        'date': datetime.strptime('10/17/2017', FMT).date(),
        'body': "Started the day with a code review, learned more about the stack call depth and how other people in the class did the assignment. We covered how to see global variables in the terminal which I was wondering about. args and *kwargs....not sure about these little guys but they seem useful...The biggest topic from the day was running tests and doing TDD. Need to read the docs on pytest.",
    },
    {
        'title': 'Class: 1',
        'date': datetime.strptime('10/16/2017', FMT).date(),
        'body': "Today I learned about working in virtual environments and why they are necessary. These are used to keep modules and packages used for a project separate from another project. I also learned some of the key differences between python 3 and python 2. I was surprised to learn that python 2 allowed print without parenthesis, I find this pretty annoying in python 3 and almost always mess it up. It was also useful to brush up on the basic python syntax. I also learned about equivalence vs. identity, I'm not sure about the 'string' is 'string' being false in the example though. I think adding a space in a string makes the identity false. Apparently this is because the interpreter will sometimes optimize memory by storing strings in the same location, in which case \'hello\' is \'hello\' evaluates to true but this should not be relied upon."
    }
]
