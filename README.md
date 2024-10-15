```bash
source .venv/bin/activate

sudo docker run -d -p 6379:6379 redis

cd backend
python manage.py runserver 8000
uvicorn backend.asgi:application --port 8001

cd frontend
npm run dev
```

## TODO

1. fix notification bell, sound might work for both parties of the notification process at the same time
