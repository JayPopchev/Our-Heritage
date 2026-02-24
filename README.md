Based on the project structure and requirements, here is the comprehensive README.md documentation for the OurHeritage project.

OurHeritage: Bulgarian Digital Archive
🏛️ Project Concept
The Bulgarian Heritage Archive is a specialized digital platform designed for curators and historians to catalog, track, and preserve ancient treasures. From Thracian gold to Medieval relics, this system provides a robust environment to monitor the lifecycle of historical artifacts through preservation logs and curated exhibitions.

🛠️ Tech Stack
Framework: Django 6.0.2.

Database: PostgreSQL.

Environment Management: python-dotenv for security.

Frontend: Modular CSS and Django Template Engine.

Interactivity: HTMX for real-time dashboard filtering.

📂 Project Structure & App Responsibilities
The project consists of five specialized Django applications:

artifacts: Manages the core database of historical items and their associated digital exhibitions.

categories: Defines and manages historical eras (e.g., Thracian, Roman, Byzantine).

preservation: Tracks the physical condition and restoration history of each artifact.

resources: Handles digital media metadata and image URLs for the archive.

common: Manages static informational pages and global base templates.

🔗 Database Architecture & Relationships
The system implements complex relationships to ensure data integrity:

Many-to-One (ForeignKey):

Every Artifact must belong to a specific Category (Historical Era).

Every PreservationRecord is linked to exactly one Artifact.

Every ArtifactResource is linked to an Artifact.

Many-to-Many (ManyToManyField):

Exhibition and Artifact share a Many-to-Many relationship, allowing an artifact to be featured in multiple exhibitions and an exhibition to contain many artifacts.

🚀 Setup & Installation
1. Prerequisites
Python 3.10+

PostgreSQL Server

2. Environment Variables
Create a .env file in the root directory and define the following variables as demonstrated in the template:

Code snippet
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=heritage_db
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
3. Quick Start
Clone the repository:

Bash
git clone <your-repository-url>
Install dependencies:

Bash
pip install -r requirements.txt
Configure PostgreSQL:
Ensure a database matching your DB_NAME exists in your PostgreSQL server.

Apply Migrations:

Bash
python manage.py migrate
Run the application:

Bash
python manage.py runserver
📋 Features & CRUD Functionality
Complete CRUD: Full Create, Read, Update, and Delete logic for Artifacts, Categories, and Preservation Logs.

Advanced Forms: Includes data validation, customized widgets, and protected "read-only" fields on edit views to preserve historical data integrity.

Dynamic Dashboard: Real-time filtering by material and historical period powered by django-filters and HTMX.

Safety Measures: Mandatory confirmation templates are required for all deletion actions to prevent accidental data loss.

Custom Error Handling: A personalized 404 page provides consistent branding even when assets are "lost to time".
