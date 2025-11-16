# Django Command Cheat Sheet

Quick reference for common Django commands and patterns.

## Table of Contents
- [Project & App Management](#project--app-management)
- [Database & Migrations](#database--migrations)
- [Running the Server](#running-the-server)
- [Admin & Users](#admin--users)
- [Shell & Management](#shell--management)
- [Common Model Fields](#common-model-fields)
- [QuerySet API](#queryset-api)
- [URL Patterns](#url-patterns)
- [Template Tags & Filters](#template-tags--filters)

---

## Project & App Management

### Create New Project
```bash
django-admin startproject projectname
```

### Create New App
```bash
python manage.py startapp appname
```

### Add App to INSTALLED_APPS
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'appname',
]
```

---

## Database & Migrations

### Create Migrations
```bash
# For all apps
python manage.py makemigrations

# For specific app
python manage.py makemigrations appname
```

### Apply Migrations
```bash
# Apply all migrations
python manage.py migrate

# Apply specific app migrations
python manage.py migrate appname
```

### Show Migrations
```bash
python manage.py showmigrations
```

### SQL for Migration
```bash
python manage.py sqlmigrate appname 0001
```

### Reset Database (SQLite)
```bash
# Delete database and migrations
del db.sqlite3
# On Linux/Mac: rm db.sqlite3

# Remove migrations (keep __init__.py)
del appname\migrations\*.py
# Keep __init__.py!

# Recreate
python manage.py makemigrations
python manage.py migrate
```

---

## Running the Server

### Start Development Server
```bash
python manage.py runserver
```

### Custom Port
```bash
python manage.py runserver 8080
```

### Custom Host and Port
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## Admin & Users

### Create Superuser
```bash
python manage.py createsuperuser
```

### Change User Password
```bash
python manage.py changepassword username
```

### Create User Programmatically
```python
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'john@example.com', 'password123')
```

---

## Shell & Management

### Django Shell
```bash
python manage.py shell
```

### Enhanced Shell (with django-extensions)
```bash
python manage.py shell_plus
```

### Check Project for Issues
```bash
python manage.py check
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Clear Database
```bash
python manage.py flush
```

---

## Common Model Fields

### Text Fields
```python
CharField(max_length=200)           # Short text
TextField()                         # Long text
SlugField(max_length=200)          # URL-friendly text
EmailField()                        # Email validation
URLField()                          # URL validation
```

### Numeric Fields
```python
IntegerField()                      # Integer
DecimalField(max_digits=10, decimal_places=2)  # Decimal
FloatField()                        # Float
BooleanField()                      # True/False
```

### Date/Time Fields
```python
DateField()                         # Date only
TimeField()                         # Time only
DateTimeField()                     # Date and time
DateTimeField(auto_now_add=True)   # Set on creation
DateTimeField(auto_now=True)       # Update on save
```

### Relationship Fields
```python
ForeignKey(Model, on_delete=models.CASCADE)
ManyToManyField(Model)
OneToOneField(Model, on_delete=models.CASCADE)
```

### File Fields
```python
FileField(upload_to='uploads/')
ImageField(upload_to='images/')
```

### Field Options
```python
null=True                           # Allow NULL in database
blank=True                          # Allow blank in forms
default='value'                     # Default value
unique=True                         # Unique constraint
choices=CHOICES                     # Limited options
help_text='Help text'              # Form help text
verbose_name='Name'                # Display name
```

---

## QuerySet API

### Basic Queries
```python
# Get all objects
Model.objects.all()

# Get single object
Model.objects.get(id=1)
Model.objects.get(slug='my-slug')

# Filter objects
Model.objects.filter(status='published')
Model.objects.filter(created_date__gte=some_date)

# Exclude objects
Model.objects.exclude(status='draft')

# Order results
Model.objects.order_by('-created_date')
Model.objects.order_by('title', '-created_date')

# Limit results
Model.objects.all()[:5]             # First 5
Model.objects.all()[5:10]           # 6th to 10th

# Count
Model.objects.count()
Model.objects.filter(status='published').count()

# Check existence
Model.objects.filter(title='Test').exists()
```

### Field Lookups
```python
# Exact match
Model.objects.filter(title='Exact Title')
Model.objects.filter(title__exact='Exact Title')

# Case-insensitive
Model.objects.filter(title__iexact='exact title')

# Contains
Model.objects.filter(title__contains='Django')
Model.objects.filter(title__icontains='django')  # Case-insensitive

# Starts/Ends with
Model.objects.filter(title__startswith='How')
Model.objects.filter(title__endswith='Guide')

# Greater than / Less than
Model.objects.filter(views__gt=100)
Model.objects.filter(views__gte=100)
Model.objects.filter(views__lt=100)
Model.objects.filter(views__lte=100)

# In list
Model.objects.filter(status__in=['draft', 'published'])

# Range
Model.objects.filter(created_date__range=[start_date, end_date])

# Is null
Model.objects.filter(published_date__isnull=True)
```

### Related Object Queries
```python
# Forward relationship (ForeignKey)
post.author.username

# Reverse relationship
user.blog_posts.all()
user.blog_posts.filter(status='published')

# Many-to-many
post.categories.all()
post.categories.add(category)
post.categories.remove(category)
category.posts.all()
```

### Aggregation
```python
from django.db.models import Count, Avg, Max, Min, Sum

# Count
Model.objects.aggregate(Count('id'))

# Average
Model.objects.aggregate(Avg('views'))

# Annotate
Model.objects.annotate(num_posts=Count('posts'))
```

### Creating & Updating
```python
# Create - Method 1
obj = Model(title='Title', content='Content')
obj.save()

# Create - Method 2
obj = Model.objects.create(title='Title', content='Content')

# Update
obj.title = 'New Title'
obj.save()

# Update multiple
Model.objects.filter(status='draft').update(status='published')

# Get or create
obj, created = Model.objects.get_or_create(
    slug='my-slug',
    defaults={'title': 'My Title'}
)

# Delete
obj.delete()
Model.objects.filter(status='draft').delete()
```

---

## URL Patterns

### Basic URL Patterns
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

### URL Parameters
```python
# String parameter
path('posts/<slug:slug>/', views.post_detail, name='post_detail')

# Integer parameter
path('posts/<int:pk>/', views.post_detail, name='post_detail')

# Path converters
# <int:name>    - Integer
# <str:name>    - String (default)
# <slug:name>   - Slug
# <uuid:name>   - UUID
# <path:name>   - Path with slashes
```

### Include Other URLconfs
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
```

### App Namespaces
```python
# blog/urls.py
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
]

# Reference in template
{% url 'blog:index' %}
```

---

## Template Tags & Filters

### Template Tags
```django
{% load static %}                   <!-- Load static files -->

{% if condition %}                  <!-- If statement -->
    ...
{% elif other_condition %}
    ...
{% else %}
    ...
{% endif %}

{% for item in items %}             <!-- For loop -->
    {{ item }}
{% empty %}
    No items
{% endfor %}

{% url 'view_name' %}               <!-- Generate URL -->
{% url 'view_name' arg1 arg2 %}

{% static 'path/to/file.css' %}     <!-- Static file URL -->

{% csrf_token %}                    <!-- CSRF protection -->

{% include 'template.html' %}       <!-- Include template -->

{% block content %}{% endblock %}   <!-- Template inheritance -->

{% now "Y-m-d" %}                   <!-- Current date/time -->

{% comment %}...{% endcomment %}    <!-- Comment -->
```

### Template Filters
```django
{{ value|lower }}                   <!-- Lowercase -->
{{ value|upper }}                   <!-- Uppercase -->
{{ value|title }}                   <!-- Title case -->
{{ value|capfirst }}                <!-- First letter uppercase -->

{{ value|length }}                  <!-- Length -->
{{ value|truncatewords:30 }}        <!-- Truncate to 30 words -->
{{ value|truncatechars:100 }}       <!-- Truncate to 100 chars -->

{{ value|date:"Y-m-d" }}            <!-- Format date -->
{{ value|time:"H:i" }}              <!-- Format time -->
{{ value|timesince }}               <!-- Time since -->
{{ value|timeuntil }}               <!-- Time until -->

{{ value|default:"N/A" }}           <!-- Default if empty -->
{{ value|default_if_none:"N/A" }}   <!-- Default if None -->

{{ value|filesizeformat }}          <!-- Human-readable file size -->
{{ value|pluralize }}               <!-- Pluralize -->
{{ value|join:", " }}               <!-- Join list -->

{{ value|safe }}                    <!-- Mark as safe HTML -->
{{ value|escape }}                  <!-- Escape HTML -->
{{ value|linebreaks }}              <!-- Convert \n to <p> and <br> -->

{{ value|add:5 }}                   <!-- Add -->
{{ value|divisibleby:3 }}           <!-- Check divisibility -->
```

---

## Useful Code Snippets

### Model with Timestamp
```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

### Custom Manager
```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    # ...
    objects = models.Manager()
    published = PublishedManager()

# Usage
Post.published.all()
```

### ModelForm
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
```

### Class-Based View
```python
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published')
```

---

## Production Settings

### Environment Variables
```python
# Install python-decouple
# pip install python-decouple

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
```

### Static Files (Production)
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Run this command
# python manage.py collectstatic
```

### Security Checklist
```bash
python manage.py check --deploy
```

---

## Quick Tips

1. **Always use virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Freeze requirements**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Run migrations after model changes**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Never commit SECRET_KEY or sensitive data**

6. **Use .env file for secrets**

7. **Set DEBUG=False in production**

8. **Use ALLOWED_HOSTS in production**

---

**Keep this cheat sheet handy while learning Django!**
