# OAuth 2 with Google SSO for FastAPI Web App #

This is a simple FastAPI app which works with a SQL database. Admin users are required to authenticate through Google SSO and later go through authorization with JWT tokens. It was completed as part of a larger project for COMS 6998: Cloud Computing.


### The structure of the app: ###

The folder instance in the repo contains a SQLite3 Database that contains information about feedback, actions, and admins. The class MySQLDataService contained in backend/app.py interacts directly with the database. app.py in the root folder of the repo contains code for Google SSO authentication for admins. Once an admin is authenticated, later authorization happens using JWT tokens. Frontend files are contained in static and templates folders.

- Regular users of the app are allowed to leave feedback
- Admin users are allowed to update admin info, delete admins (soft deletion only, information is retained in the database), add admins, and view feedback comments


### To use the app: ###

- Activate the virtual environment:   
source venv/bin/activate

- Download the required packages:     
pip install -r requirements.txt

- Run the server:             
python3 app.py

- Put "http://0.0.0.0:8084" in the browser
