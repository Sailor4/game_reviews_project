# Game Reviews Project
This is my Django project for SoftUni Basics exam

## 🚀 Features
* **Full CRUD for Games:** Users can register new games, view the catalog, edit details, and remove entries.
* **Full CRUD for Reviews:** Community members can post reviews, update their feedback, and delete old reviews.
* **Global Statistics:** A dedicated dashboard that calculates total games, total reviews, and identifies top-rated games per platform.
* **Dynamic Search:** A functional search bar in the navigation menu to filter games by title.
* **Template Inheritance:** Efficient frontend architecture using a master layout.

## 📂 Project Structure
I organized the project into logical apps to ensure the code is modular and clean:
* `game_catalog/` - Project configuration, settings, and main URL routing.
* `common/` - Contains logic for static-style pages (Home, About, Contact).
* `games/` - Handles the Game model, the catalog grid, and game management.
* `reviews/` - Handles the Review model and the community feed.
* `templates/` - Organized with a root `base.html` and subfolders for app-specific templates.
* `static/` - Contains the global `style.css` file.

## 🛠️ Technical Choices
* **Template Inheritance (DRY):** I implemented a master `base.html` file using Django's `{% extends %}` and `{% block %}` tags. This follows the "Don't Repeat Yourself" principle, making the UI consistent and the code easier to maintain.
* **PostgreSQL:** Used as the primary relational database to handle complex queries and data integrity.
* **Model Validation:** Implemented custom validators within the models to ensure ratings stay within a 1-10 scale and platforms are correctly categorized.

## 💻 How to Run
Follow these steps to get the project running locally:

1. **Clone the project** and navigate into the directory.
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure PostgreSQL is running and a database named game_reviews_db exists.
4. **Update the DATABASES setting in settings.py if your local credentials differ.
5. **Run the migrations to create the schema:
    ```bash
   python manage.py migrate
   ```
6. **Seed the Database provided:
    ```bash
    python seed_db.py
    ```
7. **Start the server:
    ```bash
    python manage.py runserver
    ```
8. ** Access the site: Open http://127.0.0.1:8000/ in your browser.