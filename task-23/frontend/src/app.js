const API_URL = "http://localhost:8000/students";

const studentForm = document.getElementById("studentForm");
const studentTableBody = document.getElementById("studentTableBody");
const searchInput = document.getElementById("searchInput");
const formTitle = document.getElementById("formTitle");
const formBadge = document.getElementById("formBadge");
const submitBtn = document.getElementById("submitBtn");
const cancelBtn = document.getElementById("cancelBtn");
const emptyState = document.getElementById("emptyState");
const statTotalStudents = document.getElementById("statTotalStudents");
const statTotalCourses = document.getElementById("statTotalCourses");
const dbStatus = document.getElementById("dbStatus");

async function checkHealth() {
  try {
    const res = await fetch("http://localhost:8000/health");
    if (res.ok) {
      dbStatus.innerText = "DB Connected & Healthy";
    } else {
      dbStatus.innerText = "API Error";
    }
  } catch (err) {
    dbStatus.innerText = "API Offline";
  }
}

async function fetchStudents(searchQuery = "") {
  try {
    const url = searchQuery ? `${API_URL}?search=${encodeURIComponent(searchQuery)}` : API_URL;
    const res = await fetch(url);
    if (!res.ok) throw new Error("Failed to load records");
    const data = await res.json();
    renderTable(data);
    updateStats(data);
  } catch (err) {
    console.error("Failed fetching students:", err);
    showToast("Error connecting to backend API", "error");
  }
}

function updateStats(students) {
  statTotalStudents.innerText = students.length;
  const uniqueCourses = new Set(students.map(s => s.course.trim().toLowerCase())).size;
  statTotalCourses.innerText = uniqueCourses;
}

function renderTable(students) {
  studentTableBody.innerHTML = "";
  if (students.length === 0) {
    emptyState.style.display = "block";
    return;
  }
  emptyState.style.display = "none";

  students.forEach((s) => {
    const row = document.createElement("tr");

    const idTd = document.createElement("td");
    idTd.textContent = `#${s.id}`;

    const nameTd = document.createElement("td");
    const nameStrong = document.createElement("strong");
    nameStrong.textContent = s.full_name;
    nameTd.appendChild(nameStrong);

    const emailTd = document.createElement("td");
    emailTd.textContent = s.email;

    const courseTd = document.createElement("td");
    const courseSpan = document.createElement("span");
    courseSpan.className = "badge";
    courseSpan.textContent = s.course;
    courseTd.appendChild(courseSpan);

    const enrollTd = document.createElement("td");
    const enrollCode = document.createElement("code");
    enrollCode.textContent = s.enrollment_number;
    enrollTd.appendChild(enrollCode);

    const actionTd = document.createElement("td");
    actionTd.className = "action-btns";

    const editBtn = document.createElement("button");
    editBtn.className = "btn edit";
    editBtn.textContent = "Edit";
    editBtn.addEventListener("click", () => editStudent(s));

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "btn danger";
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", () => deleteStudent(s.id));

    actionTd.appendChild(editBtn);
    actionTd.appendChild(deleteBtn);

    row.appendChild(idTd);
    row.appendChild(nameTd);
    row.appendChild(emailTd);
    row.appendChild(courseTd);
    row.appendChild(enrollTd);
    row.appendChild(actionTd);

    studentTableBody.appendChild(row);
  });
}

studentForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const id = document.getElementById("studentId").value;
  const payload = {
    full_name: document.getElementById("fullName").value,
    email: document.getElementById("email").value,
    course: document.getElementById("course").value,
    enrollment_number: document.getElementById("enrollmentNumber").value,
  };

  try {
    let res;
    if (id) {
      res = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
    } else {
      res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
    }

    if (!res.ok) {
      const errData = await res.json();
      throw new Error(errData.detail || "Operation failed");
    }

    showToast(id ? "Student record updated successfully!" : "Student registered successfully!", "success");
    resetForm();
    fetchStudents();
  } catch (err) {
    showToast(err.message, "error");
  }
});

async function deleteStudent(id) {
  if (confirm("Are you sure you want to delete this student record?")) {
    try {
      const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (!res.ok && res.status !== 204) throw new Error("Delete failed");
      showToast("Student deleted successfully!", "success");
      fetchStudents();
    } catch (err) {
      showToast("Failed to delete record.", "error");
    }
  }
}

function editStudent(student) {
  document.getElementById("studentId").value = student.id;
  document.getElementById("fullName").value = student.full_name;
  document.getElementById("email").value = student.email;
  document.getElementById("course").value = student.course;
  document.getElementById("enrollmentNumber").value = student.enrollment_number;

  formTitle.innerText = "Update Student Record";
  formBadge.innerText = `Editing #${student.id}`;
  submitBtn.innerText = "Save Changes";
  cancelBtn.style.display = "inline-flex";

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

cancelBtn.addEventListener("click", resetForm);

function resetForm() {
  document.getElementById("studentId").value = "";
  studentForm.reset();
  formTitle.innerText = "Register New Student";
  formBadge.innerText = "Create Mode";
  submitBtn.innerText = "Save Student Record";
  cancelBtn.style.display = "none";
}

function showToast(message, type = "success") {
  const container = document.getElementById("toastContainer");
  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  toast.innerText = message;
  container.appendChild(toast);

  setTimeout(() => {
    toast.remove();
  }, 3500);
}

let searchTimeout;
searchInput.addEventListener("input", (e) => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    fetchStudents(e.target.value);
  }, 250);
});

// Initial startup
checkHealth();
fetchStudents();
