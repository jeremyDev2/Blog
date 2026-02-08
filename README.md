# Blog

Simple Django blog application with tagging, comments, RSS feed, and sitemap support.

## Features
- Published/draft posts with slugged URLs
- Tag filtering and "similar posts" by shared tags
- Comments with moderation flag
- Email sharing for posts
- RSS feed at `/blog/feed/`
- XML sitemap at `/sitemaps.xml`

## Setup
1) Create and activate a virtual environment
```
python3 -m venv django_env
source django_env/bin/activate
```

2) Install dependencies
```
pip install -r requirements.txt
```

3) Run migrations
```
python manage.py migrate
```

4) Start the server
```
python manage.py runserver
```

Open `http://127.0.0.1:8000/blog/`.

## Email configuration
Add email settings to `blog/settings.py` or environment variables:
```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "app_password"
DEFAULT_FROM_EMAIL = "My Blog <your_email@gmail.com>"
```

For local testing without SMTP, use:
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

## Static files
CSS is served from `blog/blog_app/static/blog.css` and loaded in `blog/blog_app/templates/blog/base.html`.
