# Democraft API (Passport System)
***
>**Протестированно на:**<br>
>Docker Version: 20.10.23 <br>
>Docker-Compose version: v2.15.1
***
## Функционал (планы)
1. RESTful API для доступа к полям базы данных
2. Telegram бот для админки и создания паспортов
3. Сайт с личным кабинетом для игроков
***
## Инструкция по сборке и запуску

### Для режима разработки:
1. Создайте .env.dev файл следующего содержания:
```dotenv
FLASK_APP=democraft_api/__init__.py
FLASK_DEBUG=1
DATABASE_URI=postgresql://admin:admin@db:5432/democraft_api
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
TELEGRAM_TOKEN=<your telegram token>
TELEGRAM_DATABASE_URI=postgresql://admin:admin@db:5432/democraft_api_telegram
```

2. Соберите docker-compose.dev.yml
```bash
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d 
```
***
## Стэк
> Flask, SQLAlchemy, Alembic, aiogram