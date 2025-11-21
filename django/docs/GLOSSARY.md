# Django Terminology Glossary

A comprehensive glossary of Django terms and concepts.

## A

**Admin Interface**
Django's built-in administrative interface for managing site content. Automatically generated from your models.

**App**
A self-contained component of a Django project that provides specific functionality (e.g., blog, users, comments).

**ASGI (Asynchronous Server Gateway Interface)**
Standard interface for asynchronous Python web applications. Django 3.0+ supports ASGI for handling async views.

**auto_now / auto_now_add**
Field options for DateTimeField. `auto_now_add` sets the field when created; `auto_now` updates it on every save.

## B

**blank**
Model field option. If `True`, the field is allowed to be empty in forms. Different from `null`.

**Block**
Template tag for defining sections that can be overridden in child templates. Used in template inheritance.

## C

**CBV (Class-Based Views)**
Views defined as Python classes instead of functions. Provide reusability through inheritance and mixins.

**Context**
A dictionary of variables passed from a view to a template for rendering.

**CSRF (Cross-Site Request Forgery)**
Security exploit where malicious websites trick users into performing unwanted actions. Django has built-in CSRF protection.

**CRUD**
Create, Read, Update, Delete - the four basic operations for persistent storage.

## D

**DEBUG**
Boolean setting that enables detailed error pages. Must be `False` in production for security.

**Decorator**
Python function that modifies another function. Common Django decorators: `@login_required`, `@require_POST`.

**DTL (Django Template Language)**
Django's template system for generating HTML dynamically.

## E

**Extending**
Inheriting from a base template using `{% extends %}`.

## F

**FBV (Function-Based Views)**
Views defined as Python functions. Simpler than CBVs for basic cases.

**Field**
Database column defined in a model (e.g., `CharField`, `IntegerField`).

**Filter (QuerySet)**
Method to narrow down query results: `Post.objects.filter(status='published')`.

**Filter (Template)**
Modifies variables in templates: `{{ value|lower }}`.

**Fixture**
Serialized data for populating the database, often used for testing or initial data.

**ForeignKey**
Database relationship representing a many-to-one relationship.

**Form**
Django class for handling HTML forms, validation, and data cleaning.

## G

**Generic Views**
Built-in class-based views for common patterns (ListView, DetailView, CreateView, etc.).

**get_absolute_url()**
Model method that returns the canonical URL for an object.

## H

**HttpRequest**
Object representing an HTTP request, passed to views as the `request` parameter.

**HttpResponse**
Object representing an HTTP response returned by views.

## I

**INSTALLED_APPS**
List in settings.py of all Django apps enabled in your project.

**Include**
Template tag to insert another template: `{% include 'header.html' %}`.

## L

**login_required**
Decorator that restricts views to authenticated users only.

**Lookup**
Query filter syntax for field comparisons: `title__contains`, `date__gte`, etc.

## M

**makemigrations**
Management command that creates migration files from model changes.

**Manager**
Interface for database operations on models. Default is `objects`: `Post.objects.all()`.

**ManyToManyField**
Database relationship where both sides can have multiple related objects.

**Meta**
Inner class in models for metadata (ordering, verbose names, indexes, etc.).

**Middleware**
Framework hooks that process requests and responses globally.

**migrate**
Management command that applies migrations to the database.

**Migration**
Python file describing database schema changes. Created by `makemigrations`, applied by `migrate`.

**Mixin**
Reusable class providing specific functionality to be inherited by views or models.

**Model**
Python class representing a database table. Inherits from `models.Model`.

**ModelForm**
Form automatically generated from a model.

**MVT (Model-View-Template)**
Django's architectural pattern. Model (data), View (logic), Template (presentation).

## N

**null**
Model field option. If `True`, database can store NULL values. Different from `blank`.

## O

**OneToOneField**
Database relationship where each record relates to exactly one record in another table.

**ORM (Object-Relational Mapping)**
Django's database abstraction layer allowing Python code to interact with databases.

**on_delete**
Required parameter for relationship fields specifying behavior when related object is deleted.
- `CASCADE`: Delete this object too
- `PROTECT`: Prevent deletion
- `SET_NULL`: Set to NULL
- `SET_DEFAULT`: Set to default value

## P

**Pagination**
Splitting query results across multiple pages.

**Path Converter**
URL pattern syntax for capturing values: `<int:id>`, `<slug:slug>`, `<str:name>`.

**Project**
Top-level Django application containing settings and configuration.

## Q

**QuerySet**
Object representing a database query. Lazy evaluation - only executes when needed.

## R

**Redirect**
Sending user to a different URL. Function: `redirect()` or class: `HttpResponseRedirect`.

**related_name**
Reverse relation name for accessing related objects from the other side of a relationship.

**Render**
Combining a template with context to produce HTML: `render(request, template, context)`.

**Reverse**
Generating URLs from view names: `reverse('view_name')` in Python, `{% url 'view_name' %}` in templates.

## S

**SECRET_KEY**
Cryptographic key for signing and security. Must be kept secret and unique.

**Session**
Server-side storage of user-specific data across requests.

**settings.py**
Main configuration file for a Django project.

**Signal**
Notification sent when certain actions occur (e.g., model save). Allows decoupled applications.

**Slug**
URL-friendly string (lowercase, hyphens, no spaces): `my-blog-post`.

**SlugField**
Model field for storing slugs with validation.

**Static Files**
CSS, JavaScript, images, and other files served to the client unchanged.

**Superuser**
User account with all permissions, can access admin interface.

## T

**Tag (Template)**
Template logic and control flow: `{% if %}`, `{% for %}`, `{% block %}`.

**Template**
HTML file with Django template language for dynamic content generation.

**Template Inheritance**
Creating base templates and extending them in child templates.

**TextField**
Model field for large text content.

**Transaction**
Database operation treated as a single unit - all changes succeed or all fail.

## U

**URL Pattern**
Mapping between URL paths and views in `urls.py`.

**URLconf (URL Configuration)**
Python module defining URL patterns, usually `urls.py`.

**URL Dispatcher**
Django component that matches requested URLs to views.

**UUID (Universally Unique Identifier)**
128-bit identifier, can be used as primary keys for distributed systems.

## V

**Validation**
Checking data meets requirements before saving to database.

**verbose_name**
Human-readable name for a model or field.

**View**
Python function or class that processes HTTP requests and returns HTTP responses.

**Virtual Environment**
Isolated Python environment for project dependencies.

## W

**Widget**
HTML representation of a form field (e.g., text input, checkbox, select).

**WSGI (Web Server Gateway Interface)**
Standard interface between web servers and Python web applications.

## Common Abbreviations

| Abbreviation | Full Term | Meaning |
|--------------|-----------|---------|
| **CBV** | Class-Based View | View as a class |
| **FBV** | Function-Based View | View as a function |
| **ORM** | Object-Relational Mapping | Database abstraction |
| **MVT** | Model-View-Template | Django architecture |
| **MVC** | Model-View-Controller | Traditional architecture |
| **CSRF** | Cross-Site Request Forgery | Security vulnerability |
| **XSS** | Cross-Site Scripting | Security vulnerability |
| **SQL** | Structured Query Language | Database language |
| **CRUD** | Create, Read, Update, Delete | Basic operations |
| **DTL** | Django Template Language | Template syntax |
| **API** | Application Programming Interface | Software interface |
| **REST** | Representational State Transfer | API architecture |
| **JSON** | JavaScript Object Notation | Data format |

## Common Model Field Types

| Field Type | Description | Example Use Case |
|------------|-------------|------------------|
| **CharField** | Short text | Title, name |
| **TextField** | Long text | Article content |
| **IntegerField** | Whole number | Age, count |
| **DecimalField** | Decimal number | Price, rating |
| **BooleanField** | True/False | Is active, is published |
| **DateField** | Date only | Birth date |
| **DateTimeField** | Date and time | Created at, published at |
| **EmailField** | Email address | User email |
| **URLField** | URL | Website link |
| **SlugField** | URL-friendly text | Post slug |
| **FileField** | File upload | Document |
| **ImageField** | Image upload | Profile picture |
| **ForeignKey** | Many-to-one relationship | Post → Author |
| **ManyToManyField** | Many-to-many relationship | Posts ↔ Categories |
| **OneToOneField** | One-to-one relationship | User → Profile |

## Common QuerySet Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `.all()` | QuerySet | All objects |
| `.filter()` | QuerySet | Filtered objects |
| `.exclude()` | QuerySet | Exclude matching objects |
| `.get()` | Single object | One object (raises error if 0 or >1) |
| `.first()` | Single object or None | First object |
| `.last()` | Single object or None | Last object |
| `.count()` | Integer | Number of objects |
| `.exists()` | Boolean | Check if any objects exist |
| `.order_by()` | QuerySet | Sort results |
| `.values()` | QuerySet | Return dictionaries |
| `.values_list()` | QuerySet | Return tuples |
| `.distinct()` | QuerySet | Remove duplicates |

## Common Template Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `{% if %}` | Conditional | `{% if user.is_authenticated %}` |
| `{% for %}` | Loop | `{% for post in posts %}` |
| `{% block %}` | Define block | `{% block content %}` |
| `{% extends %}` | Inherit template | `{% extends 'base.html' %}` |
| `{% include %}` | Include template | `{% include 'header.html' %}` |
| `{% url %}` | Generate URL | `{% url 'post_detail' post.id %}` |
| `{% static %}` | Static file URL | `{% static 'css/style.css' %}` |
| `{% csrf_token %}` | CSRF protection | In POST forms |
| `{% load %}` | Load tag library | `{% load static %}` |
| `{% with %}` | Cache variable | `{% with total=posts.count %}` |

## Common Template Filters

| Filter | Purpose | Example |
|--------|---------|---------|
| `{{ var\|lower }}` | Lowercase | `{{ title\|lower }}` |
| `{{ var\|upper }}` | Uppercase | `{{ name\|upper }}` |
| `{{ var\|title }}` | Title case | `{{ heading\|title }}` |
| `{{ var\|length }}` | Get length | `{{ items\|length }}` |
| `{{ var\|date:"Y-m-d" }}` | Format date | `{{ created\|date:"Y-m-d" }}` |
| `{{ var\|truncatewords:30 }}` | Truncate | `{{ content\|truncatewords:30 }}` |
| `{{ var\|default:"N/A" }}` | Default value | `{{ bio\|default:"No bio" }}` |
| `{{ var\|safe }}` | Mark as safe HTML | `{{ html_content\|safe }}` |
| `{{ var\|join:", " }}` | Join list | `{{ tags\|join:", " }}` |

---

**Keep this glossary handy while learning Django!**
