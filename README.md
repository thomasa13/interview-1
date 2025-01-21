# Interview

### Context
This software is an exercice for the recruitment process of BNP Paribas Fortis. The context is to create a django application serving a machine learning model.


It is separated in two apps to have modularity : 
- interview: contains the default settings of the project
- linear_regression: contains the logic of the linear model and the api and views that expose it.


The algorithm can be accessed two ways: 
- Through the interface when navigating with the browser to the home page (/) or to /linear_regression/
- Through the api on /api/linear_regression/

### Next steps / Good to have
- Authentication
- Standardized error management
- Better interfaces / SPA frontend

### Manual Installation (linux)
- Make sure you have python and pip installed
- Create a venv with `python -m venv .venv`
- Activate venv with `source .venv/bin/activate`
- Install dependencies with `make install` or `pip install -r requirements.txt` 
- (optional) Configure postgresql connexion through environment variables `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`. Sqlite will be used otherwise
- Run the migrations with `make migrate` or `python3 manage.py migrate`
- Run the application with `make run` or `python3 manage.py runserver`

### Docker installation (with PostgreSQL)
- Run `sudo docker-compose up`