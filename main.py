from fastapi import FastAPI
from schema import Task, TaskCreate, TaskUpdateStatus
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

tasks: list[Task] = []
task_id_counter = 1
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
def get_tasks():
    serialized_tasks = [task.dict() for task in tasks]

    return JSONResponse(status_code=200, content={
        "success": True,
        "message": "Data fetched!",
        "data": serialized_tasks
    })

@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, title=task.title, description=task.description, status=False)
    task_id_counter += 1
    tasks.append(new_task)
    return JSONResponse(status_code=201, content={
                "success": True,
                "message": "Task Disimpan!|Data task berhasil ditambahkan!",
                "data": {}
            })

@app.put("/tasks/{task_id}")
def update_task_status(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                status=True
            )
            tasks[i] = updated_task
            return JSONResponse(status_code=200, content={
                "success": True,
                "message": "Task Selesai!|Data task berhasil diubah!",
                "data": {}
            })

    return JSONResponse(status_code=404, content={
                "success": False,
                "message": "Data task tidak ditemukan!",
                "data": {}
            })

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return JSONResponse(status_code=200, content={
                "success": True,
                "message": "Task Dihapus!|Data task berhasil dihapus!",
                "data": {}
            })
        
    return JSONResponse(status_code=404, content={
                "success": False,
                "message": "Data task tidak ditemukan!",
                "data": {}
            })