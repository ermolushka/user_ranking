# Users ranking

This project uses Flask as a web framework and sqlite3 for storing file names. It accepts file as an input, preprocess it and calculates distances from the office (everything is dome in utils.py). Then it returns just a dictionary of user_ids and user names in JSON format.

All functions are covered by the tests.

For running this project you should run the following commands:

For installing all dependencies
```sh
$ pip3 install -r requirements.txt
```
For creating local database
```sh
$ python3 dbcreate.py
```
For running the web app

```sh
$ python3 main.py
```
Then navigate to http://127.0.0.1:5000/upload for uploading the file.

The output of the provided file **customers.txt** is

{4: 'Ian Kehoe', 5: 'Nora Dempsey', 6: 'Theresa Enright', 8: 'Eoin Ahearn', 11: 'Richard Finnegan', 12: 'Christina McArdle', 13: 'Olive Ahearn', 15: 'Michael Ahearn', 17: 'Patricia Cahill', 23: 'Eoin Gallagher', 24: 'Rose Enright', 26: 'Stephen McArdle', 28: 'Charlie Halligan', 29: 'Oliver Ahearn', 30: 'Nick Enright', 31: 'Alan Behan', 39: 'Lisa Ahearn'}

For running tests
```sh
$ pytest
```