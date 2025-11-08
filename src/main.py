from fastapi import FastAPI, Query, status, HTTPException, Path, Form, Body
from fastapi.responses import JSONResponse
from random import randint
from typing import Annotated
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
def root():
    return JSONResponse(content={"message": "Hello World"}, status_code=status.HTTP_202_ACCEPTED)

@app.get("/names")
def get_names_list(q : Annotated[str | None, Query(alias="search",description="item will be searched with the title you provided", example="a", max_length=50)]=None):
    if q:
        return [item for item in names_list if item["name"] == q]
    return names_list

@app.post("/names", status_code=status.HTTP_201_CREATED)
def create_name(name:str = Body(embed=True)):
    name_obj = {"id":randint(5,100), "name":name}
    names_list.append(name_obj)
    return name_obj

@app.get("/names/{name_id}")
def get_names_detail(name_id:int = Path(alias="object id", title="object id", description="the id of the name in names_list")):
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
            return JSONResponse(content={"detail": "Object Removed Successfuly" }, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="object not found")