Бэкенд-часть SPA веб-приложения "Трекер полезных привычек".

ЗАПУСК селери воркер:

celery -A config worker -l INFO


ЗАПУСК селери бит:

celery -A my_project beat —loglevel=info

ДОКУМЕНТАЦИЯ:

http://127.0.0.1:8000/redoc http://127.0.0.1:8000/swagger


СОЗДАНИЕ И ЗАПУСК КОНТЕЙНЕРОВ (на macos):

docker compose up -d --build
