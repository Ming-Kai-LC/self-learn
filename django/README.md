# Django - Web Development from Beginner

> Learn Django web framework from scratch using hands-on Jupyter notebooks

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/django-4.2%2B-green)
![Status](https://img.shields.io/badge/status-complete-success)
![Difficulty](https://img.shields.io/badge/difficulty-beginner-brightgreen)

## About This Learning Path

This is a **complete beginner-friendly introduction to Django**, the powerful Python web framework used by Instagram, Pinterest, Spotify, and thousands of other websites. No web development experience required - just basic Python knowledge!

**What makes this different:**
- 🎯 **Interactive Learning** - Jupyter notebooks let you code along
- 📚 **Complete Curriculum** - 11 modules from setup to deployment
- 🏗️ **Build Real Projects** - Create a fully functional blog application
- 📖 **Comprehensive Docs** - Cheat sheets, FAQ, and glossary included
- ⭐ **Beginner Focused** - Clear explanations, no prior web dev needed

## Who This Is For

- ✅ **Python learners** wanting to build web applications
- ✅ **Complete beginners** to web development (HTML/CSS helpful but optional)
- ✅ **Self-learners** who prefer interactive, hands-on learning
- ✅ **Anyone** wanting to create their own websites and web apps

## What You'll Learn

By the end of this course, you will:

- ✅ Build complete web applications with Django
- ✅ Create and manage databases using Django ORM
- ✅ Design dynamic web pages with templates
- ✅ Handle user authentication (login, registration, permissions)
- ✅ Upload and manage images and files
- ✅ Create admin panels for content management
- ✅ Deploy Django applications to production
- ✅ Build a complete blog with comments and user profiles

## Quick Start

### 1. Prerequisites

**Knowledge:**
- Basic Python (variables, functions, classes)
- Basic command line usage
- HTML/CSS basics (helpful but not required)

**Software:**
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- A code editor (VS Code, PyCharm, etc.)
- Git (for version control)

### 2. Installation

```bash
# Navigate to django folder
cd self-learn/django

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import django; print(f'Django {django.get_version()} ready!')"

# Launch Jupyter
jupyter notebook
```

### 3. Start Learning

Open `notebooks/00_setup_introduction.ipynb` and begin your journey!

## Learning Path

### 📚 Module Overview

| Module | Topic | Time | Difficulty | What You'll Build |
|--------|-------|------|------------|-------------------|
| **00** | Setup & Introduction | 1h | ⭐ | Dev environment |
| **01** | Django Basics | 1.5h | ⭐ | First Django project |
| **02** | Models & Databases | 2h | ⭐ | Blog post models |
| **03** | Django Admin | 1.5h | ⭐ | Admin interface |
| **04** | Views & URLs | 2h | ⭐ | Blog views |
| **05** | Templates | 2h | ⭐ | Dynamic web pages |
| **06** | Forms & Validation | 2.5h | ⭐⭐ | Post creation forms |
| **07** | Static Files & Media | 1.5h | ⭐ | CSS styling & images |
| **08** | User Authentication | 2.5h | ⭐⭐ | Login system |
| **09** | Deployment Basics | 2h | ⭐⭐ | Production config |
| **10** | Final Blog Project | 3h | ⭐⭐ | Complete blog app |

**Total Learning Time:** ~20 hours
**Completion Rate:** Work at your own pace (1-2 modules per session recommended)

### 🎯 Detailed Module Breakdown

#### Module 00: Setup & Introduction (1 hour)
**Learn:**
- What is Django and why use it?
- MVT (Model-View-Template) architecture
- Setting up your development environment
- Running your first Django command

**Prerequisites:** Python basics only

---

#### Module 01: Django Basics & First Project (1.5 hours)
**Learn:**
- Creating Django projects and apps
- Understanding Django project structure
- Running the development server
- Basic Django settings

**Build:** Your first Django project structure

---

#### Module 02: Models & Databases (2 hours)
**Learn:**
- Defining database models with Django ORM
- Field types (CharField, TextField, DateField, etc.)
- Creating and applying migrations
- Querying the database with QuerySet API
- Model relationships (ForeignKey, ManyToMany)

**Build:** Blog post and category models with database

---

#### Module 03: Django Admin (1.5 hours)
**Learn:**
- Accessing the Django admin interface
- Registering models in admin
- Customizing admin displays and filters
- Adding search and bulk actions

**Build:** Custom admin interface for blog management

---

#### Module 04: Views & URLs (2 hours)
**Learn:**
- Function-based views (FBVs)
- Class-based views (CBVs)
- URL routing and patterns
- URL parameters and path converters
- Generic views for common tasks

**Build:** Views for listing and displaying blog posts

---

#### Module 05: Templates (2 hours)
**Learn:**
- Django Template Language (DTL) syntax
- Template inheritance and blocks
- Context variables and filters
- Template tags (for loops, if statements)
- Organizing templates

**Build:** Dynamic blog templates with base layout

---

#### Module 06: Forms & Validation (2.5 hours)
**Learn:**
- Creating forms with Django Forms
- ModelForms for database models
- Form validation and error handling
- CSRF protection
- Processing form submissions

**Build:** Forms for creating and editing blog posts

---

#### Module 07: Static Files & Media (1.5 hours)
**Learn:**
- Managing static files (CSS, JavaScript, images)
- Handling user uploads (media files)
- Using django.contrib.staticfiles
- Loading static files in templates

**Build:** Styled blog with custom CSS and image uploads

---

#### Module 08: User Authentication (2.5 hours)
**Learn:**
- Django's built-in authentication system
- User registration and login/logout
- Password management and reset
- Permissions and authorization
- Login-required views
- User profiles

**Build:** Complete user authentication system for blog

---

#### Module 09: Deployment Basics (2 hours)
**Learn:**
- Production vs development settings
- Environment variables and security
- Static file collection
- Database configuration for production
- Security checklist

**Build:** Production-ready Django configuration

---

#### Module 10: Final Blog Project (3 hours)
**Learn:**
- Integrating all components together
- Code organization best practices
- Basic testing strategies
- Performance optimization tips

**Build:** Complete blog application with:
- User authentication
- Post creation and editing
- Comment system
- Admin interface
- Responsive templates
- Image uploads

---

## Study Tips

### 📅 Recommended Study Schedule

**Option 1: Intensive (1-2 weeks)**
- 2-3 modules per day
- 2-3 hours of focused study daily
- Weekend project building

**Option 2: Moderate (3-4 weeks)**
- 1 module per day
- 1-2 hours daily
- Practice exercises between modules

**Option 3: Relaxed (6-8 weeks)**
- 1-2 modules per week
- 30-60 minutes daily
- More time for experimentation

### ✅ Learning Best Practices

1. **Code Along** - Don't just read, run every code cell
2. **Experiment** - Modify examples and see what happens
3. **Take Notes** - Keep a learning journal
4. **Build Projects** - Apply concepts to your own ideas
5. **Use Documentation** - Keep [Django docs](https://docs.djangoproject.com/) open
6. **Practice Daily** - Consistency beats marathon sessions
7. **Ask Questions** - Use docs/FAQ.md and Django communities

### 🎓 Alternative Learning Paths

**Fast Track (10 hours):**
- Modules: 00, 01, 02, 04, 05, 10
- Focus: Core concepts and final project

**Frontend Focus:**
- Modules: 00, 01, 04, 05, 06, 07, 10
- Emphasis: Templates, forms, static files

**Backend Focus:**
- Modules: 00, 01, 02, 03, 06, 08, 09
- Emphasis: Models, admin, authentication, deployment

## Project Structure

```
django/
├── README.md                   # This file - start here!
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── notebooks/                  # 📚 Learning modules (START HERE)
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
│   └── 10_final_blog_project.ipynb
│
├── docs/                       # 📖 Reference materials
│   ├── CHEAT_SHEET.md         # Quick reference guide
│   ├── FAQ.md                  # Common questions answered
│   └── GLOSSARY.md             # Django terminology
│
├── projects/                   # 🏗️ Your Django projects go here
│   └── (created during learning)
│
├── data/                       # 💾 Sample data (if needed)
│   ├── raw/
│   ├── processed/
│   └── sample/
│
└── scripts/                    # 🔧 Helper utilities
    └── (utility scripts)
```

## Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 4.2+ | Web framework |
| **Python** | 3.8+ | Programming language |
| **Jupyter** | Latest | Interactive learning |
| **Pillow** | 10.0+ | Image processing |
| **pytest** | 7.0+ | Testing framework |

See `requirements.txt` for complete list.

## Quick Reference

### Essential Django Commands

```bash
# Create new Django project
django-admin startproject myproject

# Create new app
python manage.py startapp myapp

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

For more commands, see `docs/CHEAT_SHEET.md`

## Getting Help

### 📚 Documentation Files

- **CHEAT_SHEET.md** - Quick reference for Django commands
- **FAQ.md** - Answers to 50+ common questions
- **GLOSSARY.md** - Django terminology explained

### 🌐 Django Resources

**Official:**
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Forum](https://forum.djangoproject.com/)

**Communities:**
- [r/django](https://www.reddit.com/r/django/) - Reddit community
- [Django Discord](https://discord.gg/xcRH6mN4fa) - Real-time chat
- [Stack Overflow](https://stackoverflow.com/questions/tagged/django) - Q&A

**Books (Recommended):**
- "Django for Beginners" by William S. Vincent
- "Two Scoops of Django" by Daniel and Audrey Feldroy

## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'django'`
**Solution:** Activate virtual environment and run `pip install -r requirements.txt`

**Issue:** Migrations not working
**Solution:** Delete `db.sqlite3` and `migrations/` folders, then run `makemigrations` and `migrate`

**Issue:** Port already in use
**Solution:** Use different port: `python manage.py runserver 8001`

**Issue:** Static files not loading
**Solution:** Run `python manage.py collectstatic` and check `STATIC_ROOT`

For more solutions, check `docs/FAQ.md`

## After This Course

### 🚀 Next Steps

Once you complete this beginner course, you can:

1. **Build Your Own Projects** - Apply skills to personal ideas
2. **Django REST Framework** - Learn API development
3. **Advanced Topics** - Caching, Celery, Channels
4. **Deploy to Production** - Heroku, AWS, DigitalOcean
5. **Testing** - Test-Driven Development with Django
6. **Django Packages** - Explore django-allauth, django-filters, etc.

### 💡 Project Ideas to Build

- Personal blog or portfolio
- Task management app
- E-commerce store
- Social media platform
- Learning management system
- API for mobile apps

## Success Stories

**What you can build after this course:**
- ✅ Multi-user blog platforms
- ✅ Content management systems
- ✅ User authentication systems
- ✅ Database-driven websites
- ✅ Admin dashboards
- ✅ RESTful APIs (with additional learning)

## Contributing

Found an issue or have suggestions? This is a personal learning project, but feedback is welcome via issues or pull requests.

## License

MIT License - Free to use for your learning journey.

---

## 🎯 Ready to Start?

**Your Learning Journey Begins Here:**

1. ✅ Install requirements (see Quick Start above)
2. ✅ Open `notebooks/00_setup_introduction.ipynb`
3. ✅ Code along and experiment
4. ✅ Build your blog project
5. ✅ Create your own Django applications!

**Remember:** Everyone starts as a beginner. The key is consistent practice and building real projects. You've got this! 🚀

---

**Questions?** Check `docs/FAQ.md` or the Django documentation.
**Stuck?** Review the GLOSSARY.md for terminology or CHEAT_SHEET.md for quick commands.

**Happy Learning!** 🎓
