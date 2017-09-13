### Live demo

This project is up on a heroku instance [here](https://powerful-anchorage-17540.herokuapp.com/). It has two routes. 

##### `/`

Has a button to run our `loans.py` script and a small amount of UI to make it look presentable.

##### `/loans`

The raw json output that is returned from the `loans.py` function, that would be printed to the terminal when running locally, or passed to `/` when the button is clicked.


### Installation
1. Download pipenv. Pipenv is a python dependency manager married to a python virtual environment manager. Install this globally as you would `brew` or `pip` or `npm`. For more information read the [pipenv docs](http://docs.pipenv.org/en/latest/basics.html#installing-pipenv).

Python installation: 

```
pip install --user pipenv
```

2. Download sourcecode locally
3. In your new code directory run:

```
pipenv install
```

Frontend installation:

1. From the project root, run:

```
cd frontend && yarn build
```

### File structure

- root
  - `frontend/`
  	- `components/`
  	  - `App`: simple React App and local styles
  	  - `Loan`: simple react component that has a url and value property
  - `app.py`: flask routing for root and /loans page. Either runs the frontend or serves up static files depending on whether static files are found.
  - `constants.py`: static constants used in the other files
  - `loans.py`: data munging from specific queries from the kiva api dealing with loans
  - `clients.py`: class wrapper around a request library for hitting kiva's graphql url
  - `tests.py`: test class and method that mock the logic in `loans.py` and `clients.py`

### Running the code locally

To enter the Python virtual environment, run:

```
pipenv shell
```

Inside this shell, any of the following can be run:

1. Loans

When the loans file is run from the command line, it automatically runs the function that displays funding information and urls for all expiring loans in the next 24 hours which have the `fundRaising` status. To run this function:

```
python loans.py
```

2. Tests

Since python 2.7, the `TestCase` class from the `unittest` module in Python's standard library has built-in test discovery and runner from the command line. To run tests:

```
python -m unittest
```

3. Server

Runs the flask app located in `app.py`. Has the same routes as the heroku instance detailed above.

```
python app.py
```
