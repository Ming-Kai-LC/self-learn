# Django Fundamentals
> A comprehensive, hands-on introduction to Django web development using Jupyter notebooks

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/django-4.2%2B-green)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)

## About This Project

This project provides a complete, beginner-friendly introduction to Django, the popular Python web framework. Unlike traditional Django tutorials, this course uses Jupyter notebooks to make learning interactive and accessible. Each module builds progressively on the previous one, culminating in a fully functional blog application.

Django powers some of the world's most popular websites including Instagram, Pinterest, and Spotify. This project will teach you the fundamentals needed to build your own web applications.

## Who This Is For

- **Python developers** who want to learn web development
- **Complete beginners** to Django (Python basics assumed)
- **Data scientists** transitioning to web development
- **Students** learning full-stack development
- **Anyone** who wants hands-on, interactive Django learning

## What You'll Learn

By the end of this project, you will be able to:

- [ ] Set up and configure Django projects
- [ ] Design database models using Django's ORM
- [ ] Create and run database migrations
- [ ] Build custom admin interfaces
- [ ] Handle URL routing and views
- [ ] Create dynamic templates with Django Template Language
- [ ] Build and validate forms
- [ ] Manage static files and media uploads
- [ ] Implement user authentication and authorization
- [ ] Deploy Django applications to production
- [ ] Build a complete blog application from scratch

## Project Structure

```
django-fundamentals/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
├── notebooks/                         # Learning modules
│   ├── 00_setup_introduction.ipynb
│   ├── 01_django_basics_first_project.ipynb
│   ├── 02_models_databases.ipynb
│   ├── 03_django_admin.ipynb
│   ├── 04_views_urls.ipynb
│   ├── 05_templates.ipynb
│   ├── 06_forms_validation.ipynb
│   ├── 07_static_files_media.ipynb
│   ├── 08_user_authentication.ipynb
│   ├── 09_deployment_basics.ipynb
│   ├── 10_final_blog_project.ipynb
│   └── outputs/                       # Generated files
├── projects/                          # Django projects created during learning
│   └── .gitkeep
├── data/                              # Sample data and fixtures
│   └── .gitkeep
├── scripts/                           # Helper utilities
│   └── validate_notebooks.py
└── docs/                              # Additional documentation
    ├── CHEAT_SHEET.md                 # Quick reference
    ├── FAQ.md                         # Common questions
    └── GLOSSARY.md                    # Django terminology
```

## Prerequisites

### Knowledge Requirements
- **Python basics** - variables, functions, classes, modules
- **Basic command line** usage
- **HTML/CSS basics** (helpful but not required)
- **SQL fundamentals** (helpful but not required)

### Software Requirements
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- A code editor (VS Code, PyCharm, etc.)
- Git (for version control)
- Web browser (Chrome, Firefox, etc.)

## Installation

### 1. Clone or Navigate to Repository

```bash
cd projects/django-fundamentals
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import django; print(f'Django {django.get_version()} installed successfully!')"
```

### 5. Launch Jupyter

```bash
jupyter notebook
```

Navigate to the `notebooks/` folder and start with `00_setup_introduction.ipynb`.

## Learning Path

### Module 00: Setup & Introduction
**Time:** 1 hour | **Difficulty:** Beginner

**What You'll Learn:**
- Django philosophy and architecture
- Setting up development environment
- Understanding MVT (Model-View-Template) pattern
- Running your first Django command

**What You'll Build:**
- Configured Django development environment

---

### Module 01: Django Basics & First Project
**Time:** 1.5 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Creating Django projects and apps
- Project structure and configuration
- Development server basics
- Django settings overview

**What You'll Build:**
- Your first Django project structure

---

### Module 02: Models & Databases
**Time:** 2 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Defining models with Django ORM
- Field types and options
- Creating and applying migrations
- Database queries with QuerySet API
- Model relationships (ForeignKey, ManyToMany)

**What You'll Build:**
- Blog post and category models
- Database schema with relationships

---

### Module 03: Django Admin
**Time:** 1.5 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Accessing Django admin interface
- Registering models
- Customizing admin displays
- Adding filters, search, and actions

**What You'll Build:**
- Custom admin interface for blog management

---

### Module 04: Views & URLs
**Time:** 2 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Function-based views (FBVs)
- Class-based views (CBVs)
- URL patterns and routing
- URL parameters and path converters
- Generic views

**What You'll Build:**
- Views for listing, creating, and displaying blog posts

---

### Module 05: Templates
**Time:** 2 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Django Template Language (DTL) syntax
- Template inheritance and blocks
- Context variables and filters
- Template tags (for, if, include)
- Template organization

**What You'll Build:**
- Base template and blog-specific templates
- Dynamic blog post listing and detail pages

---

### Module 06: Forms & Validation
**Time:** 2.5 hours | **Difficulty:** Intermediate

**What You'll Learn:**
- Creating forms with Django Forms
- ModelForms for database models
- Form validation and error handling
- CSRF protection
- Processing form submissions

**What You'll Build:**
- Forms for creating and editing blog posts
- Comment submission forms

---

### Module 07: Static Files & Media
**Time:** 1.5 hours | **Difficulty:** Beginner

**What You'll Learn:**
- Configuring static files (CSS, JavaScript)
- Managing media uploads
- Using django.contrib.staticfiles
- Organizing assets
- Loading static files in templates

**What You'll Build:**
- Styled blog with custom CSS
- Image upload functionality for posts

---

### Module 08: User Authentication
**Time:** 2.5 hours | **Difficulty:** Intermediate

**What You'll Learn:**
- Django authentication system
- User registration and login
- Password management
- Permissions and authorization
- Login-required views
- User profile management

**What You'll Build:**
- User registration and login system
- Author-specific blog post management

---

### Module 09: Deployment Basics
**Time:** 2 hours | **Difficulty:** Intermediate

**What You'll Learn:**
- Production vs development settings
- Environment variables with python-decouple
- Static file collection
- Database configuration
- Security checklist
- Deployment preparation

**What You'll Build:**
- Production-ready configuration
- Deployment checklist

---

### Module 10: Final Blog Project
**Time:** 3 hours | **Difficulty:** Intermediate

**What You'll Learn:**
- Integrating all components
- Code organization best practices
- Testing Django applications
- Performance optimization basics

**What You'll Build:**
- Complete, fully functional blog application with:
  - User authentication
  - Post creation and editing
  - Comment system
  - Admin interface
  - Responsive templates

---

**Total Time:** ~20 hours
**Total Modules:** 11

## How to Use This Project

### Recommended Approach

1. **Sequential Learning** - Complete modules in order (00 → 10)
2. **Hands-On Practice** - Run every code cell, don't just read
3. **Experimentation** - Modify code examples and observe results
4. **Build Along** - Create the blog project as you progress
5. **Reference Materials** - Use the cheat sheet, FAQ, and glossary

### Study Tips

- **Take breaks** - Aim for 1-2 modules per study session
- **Practice daily** - Consistency is more important than marathon sessions
- **Build projects** - Apply concepts to your own project ideas
- **Read documentation** - Supplement with official Django docs
- **Join communities** - Engage with Django communities for help

### Alternative Paths

- **Fast Track** (10 hours): Focus on modules 00, 01, 02, 04, 05, 10
- **Web Dev Focus**: Emphasize modules 04, 05, 06, 07
- **Backend Focus**: Deep dive into modules 02, 03, 08, 09

## Technologies Used

### Core Framework
- **Django 4.2+** - High-level Python web framework
- **Python 3.8+** - Programming language

### Development Tools
- **Jupyter Notebook** - Interactive learning environment
- **django-extensions** - Enhanced Django shell for notebooks
- **IPython** - Enhanced Python shell

### Additional Libraries
- **Pillow** - Image processing for media uploads
- **python-decouple** - Environment variable management
- **django-crispy-forms** - Beautiful form rendering (optional)

## Quick Start

For experienced developers who want to jump right in:

```bash
# Setup
pip install -r requirements.txt

# Start learning
jupyter notebook notebooks/00_setup_introduction.ipynb

# Run Django development server (after module 01)
cd projects/myblog
python manage.py runserver
```

## Tips for Success

1. **Environment Setup** - Always activate your virtual environment before starting
2. **Migrations** - Run migrations after model changes
3. **Server Debugging** - Use Django's excellent error pages for troubleshooting
4. **Documentation** - Keep Django docs open: https://docs.djangoproject.com
5. **Code Quality** - Follow PEP 8 style guidelines
6. **Version Control** - Commit your work regularly
7. **Testing** - Test your code as you build
8. **Security** - Never commit sensitive data (use .env files)

## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'django'`
**Solution:** Ensure virtual environment is activated and dependencies installed

**Issue:** `django.db.migrations.exceptions.MigrationSyntaxError`
**Solution:** Check your models for syntax errors, then remake migrations

**Issue:** Static files not loading
**Solution:** Run `python manage.py collectstatic` and check STATIC_ROOT settings

**Issue:** Database errors
**Solution:** Delete db.sqlite3 and migrations, then run `makemigrations` and `migrate`

**Issue:** Port already in use
**Solution:** Use a different port: `python manage.py runserver 8001`

For more issues, check `docs/FAQ.md`.

## Next Steps

After completing this project:

1. **Build Your Own Project** - Apply skills to a personal project
2. **Django REST Framework** - Learn to build APIs
3. **Advanced Django** - Explore caching, celery, channels
4. **Testing** - Master Django testing frameworks
5. **Production Deployment** - Deploy to Heroku, AWS, or DigitalOcean
6. **Django Packages** - Explore django-allauth, django-filters, etc.

## Additional Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

### Books
- "Django for Beginners" by William S. Vincent
- "Two Scoops of Django" by Daniel and Audrey Feldroy
- "Django for Professionals" by William S. Vincent

### Online Courses
- Django Official Tutorial
- Real Python Django Tutorials
- Test-Driven Development with Django

### Communities
- [Django Forum](https://forum.djangoproject.com/)
- [r/django](https://www.reddit.com/r/django/)
- [Django Discord](https://discord.gg/xcRH6mN4fa)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/django)

### Tools & Extensions
- Django Debug Toolbar
- Django Extensions
- Django REST Framework
- Celery (for async tasks)

## Contributing

Found an issue or have suggestions? This is a personal learning project, but feedback is welcome!

## License

This project is licensed under the MIT License - feel free to use it for your own learning.

## Acknowledgments

- Django Software Foundation for the amazing framework
- The Django community for excellent documentation
- All the Django developers who share their knowledge

---

**Happy Learning!** Start with `notebooks/00_setup_introduction.ipynb` and build something amazing.
