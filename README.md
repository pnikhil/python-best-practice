## Setup
```sh
# Install dependencies
pipenv install --dev

# Install pre-commit
brew install pre-commit

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push

# Run locally
docker build -t fibonacci .  
docker run -it --rm fibonacci 20

```

Repo for Python best practice

[![Test](https://github.com/pnikhil/python-best-practice/actions/workflows/test.yml/badge.svg)](https://github.com/pnikhil/python-best-practice/actions/workflows/test.yml)
