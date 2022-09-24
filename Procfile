release: python manage.py migrate
web: gunicorn myprojects.asgi:application -k uvicorn.workers.UvicornWorker
worker: REMAP_SIGTERM=SIGQUIT celery -A myproject.celery worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A myproject.celery beat --loglevel=info