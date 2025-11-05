from fastapi import FastAPI, Query, status, HTTPException
from random import randint
from typing import Annotated
status.HTTP_404_NOT_FOUND
app = FastAPI()

names_list=[
    {"id":1, "name":"a"},
    {"id":2, "name":"b"},
    {"id":3, "name":"c"},
    {"id":4, "name":"d"},
    {"id":5, "name":"d"},
    {"id":6, "name":"d"},
    {"id":7, "name":"d"},
    {"id":8, "name":"d"},
]

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/names")
def get_names_list(q : Annotated[str | None, Query(max_length=50)]=None):
    if q:
        return [item for item in names_list if item["name"] == q]
    return names_list

@app.post("/names", status_code=status.HTTP_201_CREATED)
def create_name(name:str):
    name_obj = {"id":randint(5,100), "name":name}
    names_list.append(name_obj)
    return name_obj

@app.get("/names/{name_id}")
def get_names_detail(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            return item
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="object not found")

@app.put("/names/{name_id}", status_code=status.HTTP_200_OK)
def update_names_detail(name_id:int, name:str):
    for item in names_list:
        if item["id"] == name_id:
            item["name"] = name
            return item
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="object not found")

@app.delete("/names/{name_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return {"detail": "Object Removed Successfuly" }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="object not found")