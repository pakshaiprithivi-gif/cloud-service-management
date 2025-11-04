☁️ Cloud Service Management Tracker

## 📘 Overview

The **Cloud Service Management Tracker** is a Python-based mini project designed to **simulate and manage cloud resources** such as virtual machines, databases, and storage services.
It helps users monitor resource usage, calculate costs, and manage active/inactive services effectively — mimicking a simplified version of real-world cloud billing and resource management systems.

---

## ⚙️ Features

* ✅ Add, view, and deactivate cloud services
* ⏱️ Track and update service usage hours
* 💰 Automatically calculate service costs
* 📊 Generate summary and cost reports
* 🧩 Simulate multiple cloud resources dynamically

---

## 🧠 Objectives

* Understand the fundamentals of **cloud resource management**.
* Learn how to **track usage and compute cloud billing**.
* Demonstrate **Object-Oriented Programming (OOP)** principles in Python.
* Simulate **cloud monitoring dashboards** in a simplified form.

---

## 🖥️ Technologies Used

* **Language:** Python 3.x
* **Libraries:**

  * `prettytable` — for formatted tabular reports
  * `datetime` — for timestamp and tracking
  * `random` — for usage simulation

---

## 📂 Project Structure

```
Cloud-Service-Management-Tracker/
│
├── cloud_service_tracker.py    # Main project source code
└── README.md                   # Project documentation
```

---

## 🚀 How to Run

### 1️⃣ Install Required Packages

```bash
pip install prettytable
```

### 2️⃣ Run the Project

```bash
python cloud_service_tracker.py
```

---

## 🧩 Working Principle

1. **Add Services:**
   The user can create cloud resources like *VMs, Databases, or Storage* with hourly costs.

2. **Track Usage:**
   Each service keeps track of the number of hours it’s used.

3. **Compute Cost:**
   The program multiplies the usage hours by the cost per hour to get the total expense.

4. **Generate Reports:**
   Display all active/inactive services, usage stats, and total billing summary in tabular format.

---

## 📊 Sample Output

```
=== ☁️ Cloud Service Management Tracker ===

[INFO] Added new service: Compute Engine (VM)
[INFO] Added new service: Cloud Storage (Storage)
[INFO] Added new service: SQL Database (Database)
[INFO] Added 30 hours usage to service ID 1
[INFO] Added 50 hours usage to service ID 2
[INFO] Added 20 hours usage to service ID 3

+----+----------------+-----------+----------+-------------+----------+------------+
| ID |  Service Name  |   Type    |  Status  | Usage (hrs) | Cost ($) |   Created  |
+----+----------------+-----------+----------+-------------+----------+------------+
| 1  | Compute Engine |    VM     |  Active  |     30      |   7.5    | 2025-11-04 |
| 2  | Cloud Storage  |  Storage  |  Active  |     50      |   5.0    | 2025-11-04 |
| 3  | SQL Database   | Database  |  Active  |     20      |   6.0    | 2025-11-04 |
+----+----------------+-----------+----------+-------------+----------+------------+

💰 Total Cloud Cost: $18.5
📊 Cloud Service Usage Report
------------------------------
- Compute Engine (VM) -> 30 hrs, $7.5
- Cloud Storage (Storage) -> 50 hrs, $5.0
- SQL Database (Database) -> 20 hrs, $6.0
```

---

## 📈 Learning Outcomes

By completing this project, you will:

* Understand how **cloud cost tracking** works.
* Learn to implement **OOP concepts** in real-world scenarios.
* Use Python’s libraries to **format, organize, and present data**.
* Gain experience in designing **simulation-based applications**.

---

## 💡 Future Enhancements

* Add **data persistence** using SQLite or JSON files.
* Integrate a **web-based dashboard (Flask or Streamlit)**.
* Include **user authentication** for multi-user management.
* Implement **real-time cost graphs** using Matplotlib.

---

## 👩‍💻 Author

Akshaya P
Akalya S
Akash S
