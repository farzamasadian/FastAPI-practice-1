from fastapi import FastAPI

app = FastAPI()

names_list=[
    {"id":1, "name":"a"},
    {"id":2, "name":"b"},
    {"id":3, "name":"c"},
    {"id":4, "name":"d"},
]

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/names")
def get_names_list():
    return names_list

# @app.get("/names")
# def get_names_list():
#     return names_list