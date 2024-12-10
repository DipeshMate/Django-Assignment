# Django Assignment

#### Instructions
A simple user management Django application, includes functionality for retrieving user details, adding new users, and handling errors for non-existent users.

---

## Table of Contents
- [Getting Started](#getting-started)
- [Setup Requirements](#setup-requirements)
- [Running the Application](#running-the-application)
- [Database Schema](#database-schema)
- [Git Workflow](#git-workflow)
- [SQL Queries](#sql-queries)

---

## Getting Started
Follow these instructions to set up and run the application on your local machine.
##### Following Steps to Setup this Django Application:
- 1. Install Python 3.x on your machine.
- 2. Clone the repository:
     - git clone <repository-url>;
     - cd <repository-folder>
- 3. Create and activate a Virtual environment:
     - python3 -m venv venv
     - venv\Scripts\activate
- 4. install all the required dependencies:
  - install Manually:
     - Install django using pip: pip install django.
  - install by requirements.txt file
     - pip install -r requirements.txt
- 5. Set up the database:
     - To connect a Django project to a MySQL database, install xampp on your machine , start your MySQL server and Apache. install mysqlclient: " pip install mysqlclient "
     - Create a MySQL database named users.
     - Apply the schema provided in the Database Schema section.
     
##### To Run the Application 
- python manage.py runserver 
  - which will be accessible at http://127.0.0.1:8000.



## Database Schema
This Django application uses a MySQL database named `users` and the schema for the `users` table is as follows:

```sql-code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(100) NOT NULL
);
```

## Git Workflow

- 1: Clone the Repository:
  - git clone <repository-url> # copy the repository url

- 2: Create a New Branch:
  - Use a descriptive name for your branch
    - $ git checkout -b <your-branch-name>

- 3: Make your changes and commit them:
     - git add. git commit -m "your commit name..."

- 4: Push the Changes:
   - First all the steps the contributor should follow: Push your branch to the remote repository:
     -  git push origin <your-branch-name>

- 5: Create a Pull Request to merge your branch to the main branch.


### Following SQL Queries 
##### Insert Sample Data

```sql
INSERT INTO users (name, email, role) VALUES
('John cena', 'john.cena@email.com', 'Admin'),
('Great Khali', 'kahli987@gmail.com', 'Guitarist'),
('Tom Cruise', 'tommy.hilfger@gmail.com', 'Developer'),
('Bob the Builder', 'bob.pogo@email.com', 'Game Developer');
```
##### Retrieve All Users
```sql
SELECT * FROM users;
```

##### Retrieve a Specific User by ID
```sql
SELECT * FROM users 
WHERE id = <USER_ID>;
```
