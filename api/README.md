# api for NotaBene app

## Initialize the project
1. Create a virtual environment
```bash
python3 -m venv venv
```
2. Activate the virtual environment
```bash
source venv/bin/activate
```
3. Install the dependencies
```bash
pip3 install -r requirements.txt
```
4. Run the application
```bash
make run
```
5. Open the browser and go to http://127.0.0.1:8000/docs


## Architecture
1. `main.py` - FastAPI application with all the routes
2. `database.py` - Database connection and models
3. `schemas.py` - Pydantic models for request and response
4. `services.py` - Functions to interact with the database
5. `tasks.py` - Logical functions for the application 