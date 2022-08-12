import shutil
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files")
async def create_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"fila_name": file.filename}

