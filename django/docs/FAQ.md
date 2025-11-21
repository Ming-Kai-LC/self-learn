# Django Fundamentals - Frequently Asked Questions (FAQ)

Common questions and answers for Django beginners.

## Table of Contents
- [General Questions](#general-questions)
- [Installation & Setup](#installation--setup)
- [Models & Database](#models--database)
- [Views & URLs](#views--urls)
- [Templates](#templates)
- [Forms](#forms)
- [Admin Interface](#admin-interface)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

---

## General Questions

### Q: What is Django and why should I use it?

**A:** Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. You should use it because:
- It's fast to develop with
- Highly secure (protection against SQL injection, XSS, CSRF, etc.)
- Scalable (used by Instagram, Pinterest, NASA)
- Batteries included (admin, ORM, authentication built-in)
- Large community and ecosystem

### Q: Do I need to know HTML/CSS/JavaScript to use Django?

**A:** Basic HTML is recommended but not required to start. Django handles the backend (server-side logic), but you'll eventually need HTML/CSS for templates and JavaScript for interactive features. You can learn them as you go.

### Q: How is Django different from Flask?

**A:**
- **Django**: Full-featured framework with built-in admin, ORM, authentication (opinionated)
- **Flask**: Lightweight micro-framework, more flexibility, less built-in features

Choose Django for larger projects with common requirements. Choose Flask for smaller projects or when you want more control.

### Q: What is the MVT pattern?

**A:** MVT stands for Model-View-Template:
- **Model**: Data structure (database)
- **View**: Business logic (processes requests)
- **Template**: Presentation layer (HTML)

It's similar to MVC (Model-View-Controller) but with Django-specific naming.

---

## Installation & Setup

### Q: What Python version do I need?

**A:** Django 4.2 requires Python 3.8 or higher. Check your version:
```bash
python --version
```

### Q: Should I use a virtual environment?

**A:** **Yes, always!** Virtual environments keep project dependencies isolated.

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### Q: How do I install Django?

**A:**
```bash
pip install django

# Or specific version
pip install django==4.2
```

### Q: What's the difference between a project and an app?

**A:**
- **Project**: Your entire website (one per site)
- **App**: A component with specific functionality (multiple per project)

Example: An e-commerce project might have apps for: products, cart, orders, users.

---

## Models & Database

### Q: What database does Django use?

**A:** By default, Django uses SQLite (perfect for development). For production, you can use:
- PostgreSQL (recommended)
- MySQL/MariaDB
- Oracle
- Others with third-party backends

### Q: Do I need to know SQL?

**A:** No! Django's ORM (Object-Relational Mapping) lets you interact with databases using Python:

```python
# Instead of SQL
# SELECT * FROM posts WHERE status = 'published'

# Use Django ORM
Post.objects.filter(status='published')
```

### Q: What are migrations?

**A:** Migrations are Django's way of propagating model changes to your database schema.

```bash
# Create migrations (after changing models)
python manage.py makemigrations

# Apply migrations (update database)
python manage.py migrate
```

### Q: I changed my model. What now?

**A:**
1. Make migrations: `python manage.py makemigrations`
2. Review the migration file (optional)
3. Apply migrations: `python manage.py migrate`

### Q: Can I reset my database?

**A:** Yes, for SQLite (development only):
```bash
# Delete database
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Delete migrations (keep __init__.py!)
# Then recreate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**Warning**: This deletes all data!

### Q: What's the difference between `null=True` and `blank=True`?

**A:**
- `null=True`: Database can store NULL (database-level)
- `blank=True`: Field can be empty in forms (validation-level)

```python
# Text field can be empty
content = models.TextField(blank=True, default='')

# Date can be null in database
published_date = models.DateField(null=True, blank=True)
```

---

## Views & URLs

### Q: What's the difference between FBV and CBV?

**A:**
- **FBV (Function-Based Views)**: Simple functions, easier for beginners
- **CBV (Class-Based Views)**: Reusable classes, better for complex logic

Example FBV:
```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})
```

Example CBV:
```python
class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
```

### Q: How do I pass data to templates?

**A:** Use the context dictionary:
```python
def my_view(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'My Blog',
    }
    return render(request, 'template.html', context)
```

### Q: How do I create URL parameters?

**A:**
```python
# urls.py
path('posts/<int:id>/', views.post_detail, name='post_detail')

# views.py
def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {'post': post})
```

---

## Templates

### Q: Where should I put my templates?

**A:** Two options:

1. **App-level** (recommended for reusable apps):
   ```
   blog/
   └── templates/
       └── blog/
           └── post_list.html
   ```

2. **Project-level** (for shared templates):
   ```
   templates/
   └── base.html
   ```

### Q: How do I use template inheritance?

**A:**
```django
<!-- base.html -->
<!DOCTYPE html>
<html>
<head><title>{% block title %}My Site{% endblock %}</title></head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- post_list.html -->
{% extends 'base.html' %}

{% block title %}Posts{% endblock %}

{% block content %}
    <h1>Posts</h1>
    <!-- content here -->
{% endblock %}
```

### Q: How do I display variables in templates?

**A:**
```django
{{ variable }}                  <!-- Display variable -->
{{ post.title }}               <!-- Object attribute -->
{{ post.created_date|date:"Y-m-d" }}  <!-- With filter -->
```

### Q: What's the difference between `{{ }}` and `{% %}`?

**A:**
- `{{ variable }}`: Display/output data
- `{% tag %}`: Logic and control flow (if, for, block, etc.)

---

## Forms

### Q: Should I use Form or ModelForm?

**A:**
- **Form**: General forms not tied to a model
- **ModelForm**: Forms based on a model (most common)

```python
# ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

### Q: How do I handle form submission?

**A:**
```python
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'form.html', {'form': form})
```

### Q: What is CSRF and why do I need `{% csrf_token %}`?

**A:** CSRF (Cross-Site Request Forgery) is a security attack. Django protects against it by requiring a CSRF token in all POST forms:

```django
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

---

## Admin Interface

### Q: How do I access the admin interface?

**A:**
1. Create superuser: `python manage.py createsuperuser`
2. Start server: `python manage.py runserver`
3. Visit: `http://127.0.0.1:8000/admin/`
4. Login with superuser credentials

### Q: How do I add my models to admin?

**A:**
```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Q: How do I customize the admin interface?

**A:**
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_date']
    list_filter = ['status', 'created_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
```

---

## Deployment

### Q: How do I deploy Django?

**A:** Basic steps:
1. Set `DEBUG = False`
2. Set `ALLOWED_HOSTS`
3. Use environment variables for secrets
4. Collect static files: `python manage.py collectstatic`
5. Use a production database (PostgreSQL)
6. Use a WSGI server (Gunicorn, uWSGI)
7. Use a web server (Nginx, Apache)

Popular platforms:
- **Heroku** (easiest)
- **PythonAnywhere**
- **DigitalOcean**
- **AWS**

### Q: How do I protect my SECRET_KEY?

**A:** Use environment variables:

```python
# Install python-decouple
# pip install python-decouple

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

Create `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
```

**Never commit .env to git!**

---

## Troubleshooting

### Q: "No module named 'django'" error?

**A:** Django is not installed or virtual environment not activated.
```bash
# Activate venv
venv\Scripts\activate  # Windows

# Install Django
pip install django
```

### Q: "ModuleNotFoundError: No module named 'blog'" error?

**A:** Make sure your app is in `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'blog',
]
```

### Q: "Table doesn't exist" error?

**A:** Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Q: Static files not loading?

**A:** Check:
1. `{% load static %}` at top of template
2. Settings configured:
   ```python
   STATIC_URL = '/static/'
   ```
3. For production, run: `python manage.py collectstatic`

### Q: "CSRF verification failed" error?

**A:** Make sure you have `{% csrf_token %}` in your POST forms and `django.middleware.csrf.CsrfViewMiddleware` in `MIDDLEWARE`.

### Q: Port already in use?

**A:** Either:
1. Stop the running server (Ctrl+C)
2. Use different port: `python manage.py runserver 8080`
3. Kill the process using the port

### Q: Changes not showing?

**A:**
1. **Python changes**: Restart development server
2. **Template changes**: Hard refresh browser (Ctrl+F5)
3. **Static files**: Clear browser cache or hard refresh
4. **Model changes**: Run migrations

### Q: "Operational Error: no such table" after deployment?

**A:** Run migrations on production:
```bash
python manage.py migrate
```

---

## Best Practices

### Q: Should I use ForeignKey or ManyToManyField?

**A:**
- **ForeignKey**: Many-to-One (many posts → one author)
- **ManyToManyField**: Many-to-Many (many posts ↔ many categories)

### Q: How should I organize my project?

**A:** Recommended structure:
```
myproject/
├── myproject/          # Project config
│   ├── settings.py
│   └── urls.py
├── apps/               # Your apps
│   ├── blog/
│   └── users/
├── templates/          # Shared templates
├── static/             # Shared static files
├── media/              # User uploads
├── requirements.txt
└── manage.py
```

### Q: Should I use the default User model or create a custom one?

**A:** If you're just starting, use the default `User` model. For new projects that might need custom user fields later, create a custom user model from the beginning (hard to change later).

---

## Getting Help

### Where can I get help?

- **Official Docs**: https://docs.djangoproject.com/
- **Django Forum**: https://forum.djangoproject.com/
- **Stack Overflow**: Tag your questions with `django`
- **Discord**: https://discord.gg/xcRH6mN4fa
- **Reddit**: r/django

### How do I ask good questions?

1. Search first (Google, Stack Overflow, Django docs)
2. Include Django version
3. Show relevant code
4. Include full error traceback
5. Describe what you've tried

---

**Still have questions? Check the Django documentation or ask in the community!**
