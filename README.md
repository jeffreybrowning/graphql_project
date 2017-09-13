### Installation
1. Download pipenv. Pipenv is a python dependency manager married to a python virtual environment manager. Install this globally as you would `brew` or `pip` or `npm`. For more information read the [pipenv docs](http://docs.pipenv.org/en/latest/basics.html#installing-pipenv).

```
pip install --user pipenv
```

2. Download sourcecode locally
3. In your new code directory run:

```
pipenv install
```

4. To enter the virtual environment where we are segregating the project's dependencies, now type:

```
pipenv shell
```

All further directions for running code will be from this shell and directory.

### File structure

- <root>
  - `constants.py`: static constants used in the other files
  - `loans.py`: data munging from specific queries from the kiva api dealing with loans
  - `clients.py`: class wrapper around a request library for hitting kiva's graphql url
  - `tests.py`: test class and method that mock the logic in `loans.py` and `clients.py`

### Running the code

1. Loans

When the loans file is run from the command line, it automatically runs the function that displays funding information and urls for all expiring loans in the next 24 hours which have the `fundRaising` status. To run this function, type the following in the `Kiva` directory. 

```
python loans.py
```

2. Tests

Since python 2.7, the `TestCase` class from the `unittest` module in Python's standard library has built-in test discovery and runner from the command line. To run tests, type the following in the `Kiva` directory.

```
python -m unittest
```


