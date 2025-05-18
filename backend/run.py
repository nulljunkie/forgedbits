# from whitenoise import WhiteNoise
import uvicorn

'''
    pip install whitenoise
    add whitenoise.middleware.WhiteNoiseMiddleware
'''

if __name__ == "__main__":
    # application = WhiteNoise(getattr(django.core.wsgi, 'application'))
    # application.add_files('/path/to/static/files')

    uvicorn.run(
        "backend.asgi:application",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
