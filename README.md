# Introduction

Clean code exercise.

API that calls a calculator service to execute the basic arithmetic operations (+, -, *, /)

## Technology Stack:

- FastAPI
- Uvicorn (server)
- Pytest (\*)

## Development environment

### Activate development environment

```
poetry install
```

This will create a new virtual environment (if it does not exists) and will install all the dependencies.

To activate the virtual environment use:

```
poetry shell
```

### Add/remove dependencies

```
poetry add PIP_PACKAGE [-G group.name]
```

Add dependency to the given group. If not specified will be added to the default group.

```
poetry remove PIP_PACKAGE [-G group.name]
```

Remove dependency from the given group

### Run project from command line


```
poetry run python -m uvicorn main:app --reload --port 8000
```

### Debug project from VS Code

First create a .env file in the root folder and set the environment variables.

Then use the Launch option from Visual Studio Code

## Tests

### Debug From VS Code

Launch "Pytest launch" from the run/debug tab.

You can set breakpoints and inspections

### Launch tests from command line

```
poetry run pytest --cov-report term-missing ./tests
```

This will launch tests and creates a code coverage report.

### Exclude code from coverage

When you need to exclude code from the code coverage report set, in the lines or function to be excluded, the line:

```
# pragma: no cover
```

See: https://coverage.readthedocs.io/en/6.4.4/excluding.html

