from fastapi import FastAPI
from model import Todo

app = FastAPI()

todos = []


@app.get("/")
async def root():
    return { "message": "Home page" }


@app.get("/todo")
async def get_all_todos():
    return { "todos": todos }


@app.get("/todo/{id}")
async def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    return { "message": "Todo was not found" }


@app.post("/todo")
async def create_todo(todo: Todo):
    for obj in todos:
        if obj.id == todo.id:
            return { "message": "Id already exists" }
    todos.append(todo)
    return { "message": "Todo has been added" }


@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
    for obj in todos:
        if obj.id == id:
            obj.item = todo.item
            return todo
    return { "message": "Todo was not found" }


@app.delete("/todo/{id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return { "message": "Todo was deleted" }
    return { "message": "Todo was not found" }