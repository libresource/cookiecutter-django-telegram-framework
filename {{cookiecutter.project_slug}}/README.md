# {{cookiecutter.project_name}}
{{cookiecutter.description}}

## Run locally

### Env file

```shell
cp .env.example .env
```

### Fast way

```shell
chmod +x bootstarp.sh
./bootstrap.sh
```

### Prepare

```commandline
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

```commandline
docker compose up pg
```

### Run tests

```commandline
make test
make coverage
```

### Run linter

```commandline
make lint
```

### Migrations

```commandline
python manage.py migrate
```

### Admin user

```commandline
python manage.py create_admin
```

### Run web-site and bot

```commandline
make server
```

```commandline
make run_bot
```

## Run in docker

In .env file set `POSTGRES_HOST=pg`

```commandline
docker compose up
```