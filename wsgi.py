# wsgi.py
import uvicorn
from app import app

App_port = 8084

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=App_port)