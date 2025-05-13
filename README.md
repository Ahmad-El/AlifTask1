# 🏢 Система бронирования кабинетов

Консольное Python-приложение для бронирования 5 офисных кабинетов с сохранением данных в PostgreSQL и уведомлениями по email и SMS.

---

## 🚀 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Ahmad-El/AlifTask1.git
cd booking-app
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте базу данных PostgreSQL:
```bash
createdb office_reservation
```

4. Создайте `.env` файл в корне проекта и добавьте туда переменные:

```env
DB_USERNAME=db_user
PASSWORD=db_user_password
DB_NAME=db_name
DB_HOST=db_host_name
DB_PORT=db_port

```

5. Инициализируйте таблицы и добавьте 5 кабинетов:
```bash
python setup_db.py
```

---

## ⚙️ Использование

Запуск команд через `main.py` с флагами:

### ✅ Проверка доступности кабинета

```bash
python main.py check --cabin НОМЕР --time "ГГГГ-ММ-ДД ЧЧ:ММ"
```

**Пример:**
```bash
python main.py check --cabin 3 --time "2025-05-15 14:00"
```

---

### 📅 Бронирование кабинета

```bash
python main.py reserve \
  --cabin НОМЕР \
  --time "ГГГГ-ММ-ДД ЧЧ:ММ" \
  --duration МИНУТЫ \
  --user_name "ИМЯ" \
  --user_email "EMAIL" \
  --user_phone "НОМЕР"
```

**Пример:**
```bash
python main.py reserve \
  --cabin 2 \
  --time "2025-05-15 15:00" \
  --duration 60 \
  --user_name "Иван" \
  --user_email "ivan@example.com" \
  --user_phone "+992111111111"
```

---


## 📄 Аргументы команд

| Аргумент       | Описание                                | Обязателен | Пример                        |
|----------------|------------------------------------------|------------|-------------------------------|
| `--cabin`       | Номер кабинета (1–5)                    | ✅         | `--cabin 1`                   |
| `--time`        | Время начала бронирования               | ✅         | `"2025-05-14 15:00"`          |
| `--duration`    | Длительность брони в минутах            | ✅ | `--duration 60`              |
| `--user_name`   | Имя пользователя                        | ✅ | `--user_name "Иван"`         |
| `--user_email`  | Email пользователя                      | ✅ | `--user_email test@mail.com` |
| `--user_phone`  | Телефон пользователя (в формате +...)   | ✅ | `--user_phone +79991112233`  |
| `check`         | Проверить доступность                   | ✅         |                               |
| `reserve`       | Забронировать кабинет                   | ✅         |                               |

---

## 📦 Используемые технологии

- Python 3.10+
- PostgreSQL
- SQLAlchemy
- SMTP (email)
- Twilio (SMS)
- Git
- `python-dotenv`

---

## 🧠 Автор

Ахмад Элмуродов — [GitHub](https://github.com/Ahmad-El)