pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

## Usage

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

```
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```

Local Example w/ local path:

```
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

