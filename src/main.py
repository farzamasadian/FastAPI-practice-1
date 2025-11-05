from fastapi import FastAPI
from random import randint
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

@app.post("/names")
def create_name(name:str):
    name_obj = {"id":randint(5,100), "name":name}
    names_list.append(name_obj)
    return name_obj

@app.get("/names/{name_id}")
def get_names_detail(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            return item
    return {"detail": "Object Not Found" }

@app.put("/names/{name_id}")
def update_names_detail(name_id:int, name:str):
    for item in names_list:
        if item["id"] == name_id:
            item["name"] = name
            return item
    return {"detail": "Object Not Found" }

@app.delete("/names/{name_id}")
def delete_name(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return {"detail": "Object Removed Successfuly" }
    return {"detail": "Object Not Found" }