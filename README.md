# DRF Websocket Django Backend

## Instructions to run

1. Clone the repository.
2. Create a new Python 3 virtual environment using `virtualenv -p python3 venv`. If you don't have `virtualenv` installed then install it first using `pip3 install virtualenv`.
3. Activate the virtual environment using `source venv/bin/activate`.
4. Install requirements using `pip install -r requirements.txt`.
5. This project uses postgresql as database, before running the server, a postgres db needs to be setup. Run the following commands to setup a new database for the project.
```bash
sudo su - postgres
psql
CREATE DATABASE projectdb;
CREATE USER projectdbuser WITH PASSWORD 'projectdbpassword';
ALTER ROLE projectdbuser SET client_encoding TO 'utf8';
ALTER ROLE projectdbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE projectdbuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE projectdb TO projectdbuser;
\q
exit
```
7. Proceed to step 8 if you created database, user and password with values provided in commands above. Head over to `activate` file of your virtual environment present at `<virtualenvironment>/bin/activate`, in this case `venv/bin/activate` and add the following environment variables at the end of the file. After adding the values deactivate the virtual environment using `deactivate` command and activate again using `source venv/bin/activate`
```bash
export DBNAME="database name"
export DBUSER="database user"
export DBPASSWORD="database user's password"
```
8. Migrate the database using `python manage.py migrate`
9. The raw restaurant data is in `hours.csv`. To process the raw data run `python dataloader.py` which will create `finalhours.csv`, one instance of `finalhours.csv` is already present in the repository.
10. Load the data in the database using `python manage.py importdata`. You will see when the loading is completed, it generally takes almost 1 minute.
11. Create a superuser using `python manage.py createsuperuser`
12. Run the server using `python manage.py runserver`
13. Use keyboard interrupt `Ctrl + C` to stop the server.
14. For subsequent runs, just activate the virtual environment and run the server using `python manage.py runserver`.
15. Admin panel can be accessed at `/admin`.

## Technologies Used:
1. Python3
2. Django
3. Django Channels (websocket support for realtime updates)
4. Django Rest Framework (for creating REST API's)
5. Django Rest Knox (for JWT Token authentication)
6. PostgreSQL Database

## License
MIT
