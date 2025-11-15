
# 📰 **News Dashboard — Django Admin & News Management System**

News Dashboard adalah aplikasi manajemen berita berbasis **Django**, dilengkapi fitur autentikasi, manajemen kategori, role-based menu, dan dashboard admin.
Aplikasi ini dirancang untuk lingkungan sekolah, kantor, atau organisasi yang membutuhkan sistem CRUD berita yang sederhana namun dapat dikembangkan menjadi skala produksi.

---

## 🚀 **Fitur Utama**

### 🔐 **Autentikasi & Manajemen User**

* Login & Logout
* Proteksi halaman menggunakan `login_required`
* Redirect otomatis & session-based auth
* Struktur modular untuk menambah Role/Permission

### 📰 **Manajemen Berita (News)**

* Dashboard index untuk melihat semua berita (WIP)
* CRUD kategori berita
* Filter berita berdasarkan kategori

### 🧩 **Modular App Structure**

* `apps/news` → Manajemen berita & kategori
* `apps/users` → Autentikasi
* `apps/dashboard` → Dashboard utama

### 🎨 **UI Template**

* Menggunakan template HTML kustom (siap integrasi dengan AdminLTE, Tailwind, Bootstrap)

### 🗂 **Static & Media Support**

* Static file dengan konfigurasi Django
* Media directory untuk upload file (jika dikembangkan)

---

## 🏗 **Arsitektur Folder**

```
news-dashboard/
│
├── apps/
│   ├── dashboard/
│   ├── users/
│   └── news/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
├── static/
├── media/
├── venv/
├── manage.py
└── README.md
```

---

## 🔧 **Instalasi & Setup**

### 1️⃣ Clone Repo

```bash
git clone https://github.com/eka0789/news-dashboard.git
cd news-dashboard
```

### 2️⃣ Buat Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Konfigurasi Database (SQLite / PostgreSQL)

Default SQLite (langsung jalan).

Jika pakai PostgreSQL, sesuaikan di `config/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "news",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5️⃣ Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Jalankan Server

```bash
python manage.py runserver
```

---

## 🔑 **Akun Admin**

Pastikan membuat superuser:

```bash
python manage.py createsuperuser
```

---

## 🧪 **Route Utama**

| Route                         | Deskripsi        |
| ----------------------------- | ---------------- |
| `/auth/login/`                | Halaman login    |
| `/users/`                     | Dashboard user   |
| `/news/`                      | Dashboard berita |
| `/news/category/`             | List kategori    |
| `/news/category/create/`      | Tambah kategori  |
| `/news/category/<id>/edit/`   | Edit kategori    |
| `/news/category/<id>/delete/` | Hapus kategori   |

---

## 📝 **To-Do (Roadmap Pengembangan)**

* [ ] CRUD Berita lengkap
* [ ] Upload thumbnail berita
* [ ] Pagination & Searching
* [ ] Role-based authorization (Admin, Editor)
* [ ] API RESTful menggunakan Django REST Framework
* [ ] Integrasi Tailwind atau AdminLTE
* [ ] Unit Testing (pytest)

---

## 📸 Screenshots

*(Tambahkan nanti)*

```
![Dashboard Screenshot](./screenshots/dashboard.png)
![Login Page](./screenshots/login.png)
```

---

## 📜 Lisensi

Proyek ini menggunakan lisensi **MIT**.


