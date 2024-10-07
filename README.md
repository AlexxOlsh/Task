Для запуска проекта необходимо установить:

    pip install djangorestframework

    pip install drf-yasg

    pip install djangorestframework_simplejwt

    Celery: celery -A conf worker --pool=threads --loglevel=info
    Celery-beat: celery -A conf  beat --loglevel=info
    Flower: celery -A conf flower