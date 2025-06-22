from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os, shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
UPLOAD_FOLDER = "uploads"

@app.post("/upload_folder/")
async def upload_folder(folder: UploadFile = File(...)):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    zip_path = os.path.join(UPLOAD_FOLDER, folder.filename)
    with open(zip_path, "wb") as f:
        f.write(await folder.read())
    shutil.unpack_archive(zip_path, UPLOAD_FOLDER)
    return {"message": "Folder uploaded and extracted"}

@app.post("/edit_files/")
async def edit_files(prompt: str = Form(...)):
    # Basic prompt handling example
    for root, _, files in os.walk(UPLOAD_FOLDER):
        for file in files:
            if file.endswith(".js"):
                path = os.path.join(root, file)
                with open(path, "r+") as f:
                    content = f.read()
                    f.seek(0)
                    f.write(f"// {prompt}\n{content}")
    return {"message": "Edit complete"}

@app.post("/delete_file/")
async def delete_file(filename: str = Form(...)):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(full_path):
        os.remove(full_path)
        return {"message": f"{filename} deleted"}
    return JSONResponse(status_code=404, content={"error": "File not found"})

@app.get("/")
def root():
    return {"message": "MCP server is working!"}
