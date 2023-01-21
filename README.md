# a-simple-api
API service on FastAPI
---
This API may be used for a Shopping List. Feel free to use it for anything else. It has the Item object with the following features:

- Add
- Update
- Delete

You may run the app as a Docker file using command

>`docker compose up`

Else create a python virtual environment and install dependencies from requirements.txt

>`python -m venv venv`

>`pip install -r requirements.txt`

Run server with

>`uvicorn app:app --host 0.0.0.0 --port 80 --reload`

Needless to say this app is running on port 80
