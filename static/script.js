const form = document.getElementById("resumeForm");
const loader = document.getElementById("loader");

// Show loader when form is submitted
form.addEventListener("submit", () => {
    loader.classList.remove("hidden");
});

// Improve file upload UX
const fileInput = document.querySelector('input[type="file"]');
const uploadBox = document.querySelector(".file-upload span");

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        uploadBox.textContent = fileInput.files[0].name;
    }
});
