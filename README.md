# MyProject

[![Devspaces](https://img.shields.io/badge/devspaces-enabled-blue)](http://start.devspaces.com/)
[![API Documentation](https://img.shields.io/badge/apidoc-swagger-brightgreen)](https://trilogy-group.github.io/MyProject/docs/)


## Setting up development environment

### DevSpaces
DevSpaces is the recommended development environment for this repo. To get started, just open this repo with [DevSpaces](https://trilogy.devspaces.com/). 

It will start a dev server by default (on port 8000). If it doesn't you can start it by executing the following command in a terminal

```
source scripts/devspace/setup_project_gitpod.sh
```


### Local Setup

Follow these steps to setup a local development environment

```bash
git clone https://github.com/trilogy-group/MyProject.git
python3 -m venv ./venv

# You need GH token to install npm package from GH
eval $(gp env -e GITHUB_TOKEN=<YOUR_GH_TOKEN>) # this is for devspace, you can also configure it here https://trilogy.devspaces.com/variables
export GITHUB_TOKEN=<YOUR_GH_TOKEN> # for local env

# On Linux/Mac
source ./venv/bin/activate
# On windows, you run:
# source ./venv/Scripts/activate

# Run the following command first time on local setup (it runs automatically on devspace startup)
source scripts/setup_project.sh

# setup_project.sh will start the server, for subsequent server restart
python manage.py runserver
```

## Committing Migrations

Follow this process to make changes to models:
- Make changes to the model and run `python integration_hub_v2/manage.py makemigrations`
- This command will create migrations in `integration_hub_v2/integration_hub_v2/test_migrations` directory. Copy the migrations to `disabled_migrations` directory and push it to your feature branch
- Get your migrations and model changes approved
- After they're approved, move the migrations from `disabled_migrations` to `migrations` directory

This process must be followed to ensure that WIP changes to model do not affect the DevCentral DB.

## Linting
We use `pylint` for linting the code. Execute following command to check the code for any linting issues:

```
pylint --load-plugins=pylint_django myproject/ --rcfile=.pylintrc_github --disable=django-not-configured
```



## Environment Variables

Details about each environment variable & how to generate it can be found [here](https://github.com/trilogy-group/cn-integration-hub-v2/blob/master/integration_hub_v2/.env.example)


