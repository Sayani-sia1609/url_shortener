# 🔗 URL Shortener 

A simple and clean URL Shortener web application built using **Flask** and **MySQL**.  
Users can submit a long URL and receive a short URL that redirects to the original link.

This project demonstrates:
- Backend logic
- Database automation
- URL validation
- Real HTTP redirection

---

## 🚀 Features

- 🔹 Shorten long URLs
- 🔹 Automatically generates unique short codes
- 🔹 Redirects users to the original URL
- 🔹 URL validation before insertion
- 🔹 MySQL database integration
- 🔹 Database & table creation automated
- 🔹 Clean and minimal backend design

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** MySQL
- **Language:** Python 3
- **Libraries:** mysql-connector-python, Flask
- **Frontend**  HTML,CSS
---

## 📂 Project Structure

```text
URL_shortener/
│
├── main.py              # Main Flask application
├── db.py                # Database setup (automated)
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Automated Database Setup

The database and table are **created automatically** when the setup script runs.

### Database

### Table: `urls`

| Column     | Type          | Constraints            |
|------------|---------------|------------------------|
| id         | INT           | AUTO_INCREMENT         |
| long_url   | VARCHAR(2083) | NOT NULL               |
| short_url  | VARCHAR(10)   | PRIMARY KEY, NOT NULL  |

No manual SQL setup is required.

---

## 🚀 How It Works

### 1️⃣ Create Short URL
- User sends a POST request with a long URL
- URL is validated using regex
- A random short code is generated
- Mapping is stored in the database
- Short URL is returned

### 2️⃣ Redirect
- User opens `/short_code`
- Backend fetches the original URL
- Flask redirects the user instantly

---

## 🔁 Core Routes

### `/` — Create Short URL
- **Method:** `POST`
- **Input:** `url`
- **Output:** Shortened URL

### `/<short_code>` — Redirect
- **Method:** `GET`
- **Action:** Redirects to original URL

---

## 🛠️ Running the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣Run Database Setup

```bash 
python databases/db.py
```
### 3️⃣Start the Server

```bash 
python main.py
```
### Server Runs at 

```bash 
http://localhost:5000
```
## 📝 Future Improvements
-  UI dashboard

- Click analytics

- Custom aliases

- Expiry dates

- Authentication

- REST API version

  ---
  Built with ❤️ by Sayani Das
