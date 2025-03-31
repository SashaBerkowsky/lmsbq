# Django Library Management System
Objective: Create a **Dockerized Django project** with an **admin interface** that manages books and users, mimicking a simple **library system**

## System Requirements
1. Models
    - User (Django built-in User model)
    - Book
        - title (CharField)
        - author (CharField)
        - status (ChoiceField, Available/Borrowed)
        - borrowed_by (ForeignKey to User, nullable)
2. Admin Panel
    - Books should be manageable via *Django Admin*
    - Admins can assign books to users (borrow)
3. Dockerization
    - Provide a `Dockerfile` and `docker-compose.yml`
    - App should run on `http://localhost:8000/admin`
4. Database
    - Use *SQLite*
5. Bonus
    - Add a *filter* in the *admin panel* to show only available books
