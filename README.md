# houm-code-challenge
This repository contains the pokemon api test suite

## Libraries
1. **pytest** - Test framework
2. **requests** - HTTP client
3. **Flake8** and **autopep8** - linting
4. **pipenv** - package manager, virtual environment

## How to run the project locally?
First of all, you will need to install python 3.8

once python is installed, you would need to install pipenv:

```
cd houm-code-challenge
pip install pipenv
```

then you need to install all the packages and activate your virtual environment:

```
pipenv shell
```

we use **pytest** as a test runner, you can run the tests as follows:

```
pipenv run pytest -v
```
