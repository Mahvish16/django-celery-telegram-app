
# 🧠 Django Backend Project – DRF, Celery, Redis, Telegram Bot

A small backend project that demonstrates Django REST Framework APIs, token-based authentication, Celery for background tasks, Redis as a broker, and integration with a Telegram bot. Follows production-level practices using `.env`, `gitignore`, and proper code structure.

---

## 🚀 Features

- Django + Django REST Framework (DRF)
- JWT or Token Authentication
- Public and Protected APIs
- Celery for async tasks (e.g., sending email after registration)
- Redis as a Celery broker
- Telegram Bot: stores user Telegram usernames on `/start`
- Web login with Django auth
- Secure production-ready `.env` setup

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Start Development Server

```bash
python manage.py runserver
```

---

## 🔌 Celery & Redis Setup

### 1. Start Redis Server

Make sure Redis is running on your system (default port 6379). On Linux:

```bash
sudo service redis-server start
```

### 2. Start Celery Worker

```bash
celery -A config worker --loglevel=info
```

> Celery is used to send background tasks like confirmation email on registration.

---

## 🤖 Telegram Bot Integration

1. Create a bot via [BotFather](https://t.me/BotFather) on Telegram  
2. Add the bot token to `.env` as `TELEGRAM_BOT_TOKEN`  
3. Run the bot script:

```bash
python telegram_bot/bot.py
```

> The bot listens for `/start` command and stores Telegram usernames into the Django DB.

---

## 🧪 API Endpoints

| Method | Endpoint        | Access     | Description                      |
|--------|------------------|------------|----------------------------------|
| GET    | /api/public/     | Public     | Returns public data              |
| GET    | /api/protected/  | Auth Only  | Requires JWT or Token Auth       |
| POST   | /api/register/   | Public     | Register a new user              |
| POST   | /api/login/      | Public     | Login and receive token          |

---

## 🔐 Authentication

Use JWT or DRF Token Auth in headers:

```
Authorization: Bearer <your_token>
```

or

```
Authorization: Token <your_token>
```

---

## 📦 Environment Variables

| Variable            | Description                      |
|---------------------|----------------------------------|
| SECRET_KEY          | Django secret key                |
| DEBUG               | Set to `False` for production    |
| ALLOWED_HOSTS       | Comma-separated host list        |
| DB_NAME             | Your database name               |
| DB_USER             | Database username                |
| DB_PASSWORD         | Database password                |
| DB_HOST             | Database host                    |
| DB_PORT             | Database port                    |
| TELEGRAM_BOT_TOKEN  | Token from BotFather             |

---

## 📄 Requirements

Install all Python dependencies using:

```bash
pip install -r requirements.txt
```

Example packages:

```
Django>=4.0
djangorestframework
python-decouple
djangorestframework-simplejwt
celery
redis
python-telegram-bot
```

---


## 💡 Author

Developed by [Mahvish Ruhi]  
