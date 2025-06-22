async function upload() {
  const fileInput = document.getElementById("folderInput");
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("folder", file);

  const response = await fetch("http://localhost:8000/upload_folder/", {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  alert(result.message || "Upload complete");
}

async function edit() {
  const prompt = document.getElementById("prompt").value;
  const formData = new FormData();
  formData.append("prompt", prompt);

  const response = await fetch("http://localhost:8000/edit_files/", {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  alert(result.message || "Edit complete");
}

async function deleteFile() {
  const filename = document.getElementById("deleteFile").value;
  const formData = new FormData();
  formData.append("filename", filename);

  try {
    const response = await fetch("http://localhost:8000/delete_file/", {
      method: "POST",
      body: formData
    });

    const result = await response.json();
    alert(result.message || result.error || "Delete complete");
  } catch (err) {
    console.error("Delete error:", err);
    alert("Delete failed");
  }
}
