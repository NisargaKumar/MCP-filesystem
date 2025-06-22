# MCP Filesystem Editor

A simple FastAPI-based backend with a modern HTML frontend that allows users to:

- 📁 Upload ZIP folders containing code files
- 📝 Add prompts to edit `.js` files (e.g., insert comments)
- 🗑️ Delete specific files from the uploaded folder

## 🔧 Features

- FastAPI server with endpoints for upload, edit, and delete
- Frontend with a clean UI (HTML + CSS)
- CORS-enabled for frontend-backend communication
- Handles file extraction and prompt-based modifications

## 📁 Folder Structure

```
mcp-filesystem/
├── server/
│   └── main.py
├── frontend/
│   ├── index.html
│   └── script.js
├── uploads/
├── venv/ (optional, use .gitignore)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd mcp-filesystem
```

### 2. Set Up Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI Server

```bash
uvicorn server.main:app --reload
```

### 5. Run Frontend

```bash
cd frontend
python -m http.server 5500
```

Open [http://localhost:5500](http://localhost:5500) in your browser.

## ✨ Endpoints

| Method | Route                | Description              |
|--------|----------------------|--------------------------|
| POST   | /upload_folder/      | Upload and extract ZIP   |
| POST   | /edit_files/         | Add prompt to `.js` files|
| POST   | /delete_file/        | Delete a specific file   |

## 🛡️ .gitignore (Example)

```
__pycache__/
venv/
uploads/
*.zip
```
---

Made with ❤️ using FastAPI and plain HTML/CSS.
