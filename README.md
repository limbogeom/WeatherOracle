# 🌦️ WeatherOracle

WeatherOracle is a backend service built with **Flask** and **PostgreSQL** for collecting, storing, and querying weather data such as temperature, humidity, and light intensity.

The project is designed as a **REST API**, suitable for IoT devices (ESP32, sensors), scheduled data ingestion (once per hour), and simple frontend visualization.

---

## ✨ Features

* REST API for weather data
* PostgreSQL database
* SQLAlchemy ORM
* Flask-Migrate (Alembic) for database migrations
* JSON/JSONB fields (light data)
* Filtering and sorting queries
* Ready for deployment (Render / Supabase / Railway alternatives)
* Simple frontend endpoint

---

## 🧱 Tech Stack

* **Python 3.10+**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Migrate**
* **PostgreSQL**
* **Gunicorn** (for production)

---

## 📁 Project Structure

```text
WeatherOracle/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
├── migrations/
├── run.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Configuration

Create an environment variable for the database connection:

```bash
export DATABASE_URL="postgresql://user:password@host:5432/dbname"
```

> ⚠️ Make sure the variable name is **`DATABASE_URL`**

---

## 🚀 Running Locally

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Initialize database migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3️⃣ Run the server

```bash
flask run
```

Server will be available at:

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### ➕ Add weather data

```bash
curl -X POST http://127.0.0.1:5000/api/weather \
-H "Content-Type: application/json" \
-d '{
  "temperature": 25.5,
  "humidity": 60,
  "light": {"lux": 120},
  "stored_at": "2026-02-01T12:00:00"
}'
```

---

### 📄 Get weather data

```bash
curl http://127.0.0.1:5000/api/weather/backend
```

With filters:

```bash
curl "http://127.0.0.1:5000/api/weather/backend?temp_gt=0&lux_gt=10&limit=100"
```

---

### ❌ Delete record

```bash
curl -X DELETE http://127.0.0.1:5000/api/weather/1
```

---

## 🕒 Timezone

* All timestamps are stored in **UTC**
* You can convert to local time (e.g. Kyiv) on the client or query layer

---

## 📦 Production Mode

Run with Gunicorn:

```bash
gunicorn run:app
```
---

## 🧠 Use Cases

* Weather station backend
* ESP32 / IoT data ingestion
* Data collection every hour via cron
* Educational backend project (Junior level)

---

## 📜 License

MIT License
Feel free to use, modify, and deploy.

---

## 👤 Author

**Limbo**
GitHub: [limbogeom](https://github.com/limbogeom)
