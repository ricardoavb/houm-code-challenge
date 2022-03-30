# houm-code-challenge
This repository contains the pokemon api test suite

## Libraries
1. **pytest** - Test framework
2. **requests** - HTTP client
3. **Flake8** and **autopep8** - linting
4. **pipenv** - package manager, virtual environment

## :rocket: How to run the tests locally?
First of all, you will need to install python 3.8

once python is installed, you would need to install pipenv as follows:

```
cd houm-code-challenge
pip install pipenv
```

then you need to install all the packages and activate your virtual environment:

```
pipenv shell
pipenv install
```

we use **pytest** as a test runner, you can run the tests as follows:

```
pipenv run pytest -v
```

if everything goes well, you will see a message like this:

test/integration/test_pokemon_api.py::test_pokemon_name_contains_at_and_double_a PASSED [ 33%]
test/integration/test_pokemon_api.py::test_raichu_compatible_species PASSED [ 66%]
test/integration/test_pokemon_api.py::test_smallest_and_biggest_pokemon PASSED [100%]

============================= 3 passed in 46.21s ==============================

## :mag: How to run the linter?

we use **flake8** and **autopep8** as a linting tools, you can run the linter as follows:

```
pipenv run flake8 --ignore E501
```

if everything goes well, it should not show any warnings,
you can use **autopep8** to auto-fix those warnings

## :octocat: Github Actions

In order to make sure nothing was broken, the **pull_request.yml** workflow
will run some jobs when creating a new PR

The following jobs will be executed:

1. Linter
2. Integration test
