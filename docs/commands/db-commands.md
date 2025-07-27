# Usefull commands fo PostgreSQL

## Check if you have already
- `sudo systemctl status postgresql`
- `psql --version`
- `sudo -u postgres psql`
- `alter user postgres with password '12345';`
- `quit`


## Install
- `sudo apt update`
- `sudo apt install postgresql postgresql-contrib`

## Upgade
- `psql --version`
- Update PostgreSQL via official PostgreSQL APT repository:
    - Import PostgreSQL signing key: `wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/postgresql.asc`
    - Add the PostgreSQL APT repository (replace `jammy` with your Ubuntu codename. Use the command `. /etc/os-release && echo "$VERSION_CODENAME"` to find out your codename): `echo "deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list`
    - `sudo apt update`
- Install the latest version, i.e. to install version 16: `sudo apt install postgresql-16`
- (Optional) Migrate your data:
    - `sudo systemctl stop postgresql`
    - Replace 12 and 16 with your actual old and new versions:
        - `sudo pg_upgradecluster 12 main`
        - `sudo systemctl start postgresql@16-main`
    - Remove old version (optional, after testing)
        - `sudo apt remove postgresql-12`
        - `sudo apt autoremove`

## Install PostgreSQL GUI
- GUI Monitoring: `https://www.pgadmin.org/`
    - Install via pgAdmin's Official APT Repository
        - `curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pgadmin.gpg`
        - `sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`
    - Install pgAdmin (GUI & WebApp in `http://localhost/pgadmin4`): `sudo apt install pgadmin4`

## Install python package
- `pip install psycopg2`
    - If it produces an error:
        - Option 1: Simplest fix is to install the binary version instead of building from source. Use psycopg2-binary for development, quick installs, or when you don't need to customize the build: `pip install psycopg2-binary`
        - Option 2: Build from source, which means you’ll need to install PostgreSQL client development libraries (Use psycopg2 (source version) in production or if your system policies restrict use of binary wheels):
            - `sudo apt update`
            - `sudo apt install libpq-dev python3-dev build-essential -y`
            - `pip install psycopg2`
    - If there are problems with psycopg2 version, then: `pip install psycopg2==2.8.6` or set `USE_TZ = False` in settings.py.
