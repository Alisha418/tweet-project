# 🐦 Django Tweet Hub
> A sophisticated social media micro-blogging platform.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

---

### 🌟 Project Overview
**Django Tweet Hub** is a full-featured web application designed to demonstrate secure user authentication and seamless CRUD operations. It bridges the gap between public consumption and private interaction.

### ✨ Key Capabilities

| Feature | Public Access | Registered Users |
| :--- | :---: | :---: |
| **View Tweets** | ✅ | ✅ |
| **Search Tweets** | ✅ | ✅ |
| **Create/Post** | ❌ | ✅ |
| **Edit/Delete** | ❌ | ✅ (Own Tweets Only) |
| **Image Uploads**| ❌ | ✅ |

---

### 🛠️ Technical Architecture

* **Backend:** Django Framework (Pythonic Core)
* **Database:** SQLite (Development) / PostgreSQL Ready
* **Authentication:** Django Built-in Auth System
* **UI/UX:** Responsive Bootstrap 5 & Custom CSS

---

### 🚀 Rapid Deployment

#### 1. Clone & Navigate
```bash
git clone [https://github.com/Alisha418/tweet-project.git](https://github.com/Alisha418/tweet-project.git)
cd tweet

2. Environment Setup
python -m venv venv
# Windows Activation
source venv/Scripts/activate

3. Initialization
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

📂 Structural Blueprint
├── firstproject/      # Core Project Engine & Settings
├── tweet/             # App Logic (Models, Views, Controllers)
│   ├── migrations/    # Database Evolution Files
│   └── templates/     # Feature-specific HTML (CRUD/Search)
├── templates/         # Global Layouts & Auth Templates
└── manage.py          # Command-line Utility

Developed by **Alisha** | [GitHub Profile](https://github.com/Alisha418)