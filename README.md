## 📌 Project Title 
🎬📚 CRUD Smart tracker - With ai recomenndation

## Description Project
Smart tracker ini menggunakan flask libary sebagai webnya dan sqlite sebagai mini database.
Web app ini berguna untuk mentrack dan menlist movie, anime dan buku di satu tempat.
Web app ini memiliki fitur CRUD (create, read, update, delete) dan bisa mensorting category/ genre yang ingin dilihat.
Dan jika bingung atau ingin mencari rekomendasi bisa kita tanyakan AI.

## 🛠️ Technologies Used
1. Backend = python, flask
2. Database = SQLite
3. Frontend = HTML, bootsrap 5
5. AI = Ollama (local AI) Ai yang digunakan adalah mistral
6. Version control =  Git + github

## ✨ Features
- Add, edit, and delete movies, anime, atau buku
- sorting dari category (movie, anime, buku) dan dari genre (action, romance,)
-Bantuan AI:
   -Mencari film, buku atau anime yang ingin ditonton
   -Bisa merekomendasikan film buku atau anime yang lagi hangat sekarang

## setup instraction
1. clone repositorynya
   ```bash
   git clone https://github.com/Sunraku23/Smart-Tracker-IBM-project.git
   cd Smart-Tracker-IBM-project

2. Buat dan aktifkan virtual envnya:
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3. Install dependensi
   pip install -r requirements.txt
4.Siapkan databasenya:
   python database.py

5. jalankan appnya
     flask run
   

