from fastapi import FastAPI
from gov import get_schemes, search_scheme

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Government Assistant Running"}


@app.get("/schemes")
def schemes():

    return get_schemes()


@app.get("/search")
def search(q: str):

    return search_scheme(q)