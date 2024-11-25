Бэкенд-часть SPA веб-приложения "Трекер полезных привычек".

Запуск селери воркер
celery -A config worker -l INFO


Запуск селери бит
celery -A my_project beat —loglevel=info

ДОКУМЕНТАЦИЯ:
http://127.0.0.1:8000/redoc http://127.0.0.1:8000/swagger

СОЗДАНИЕ И ЗАПУСК КОНТЕЙНЕРОВ (на macos):

docker compose up -d --build
