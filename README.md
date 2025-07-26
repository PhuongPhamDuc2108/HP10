# Django Travel Website

This is a Django-based travel website project inspired by Traveloka, providing features for searching and booking hotels and flights.

## Features

- Home page with banner and categories (Vé máy bay, Khách sạn, Tour, Xe đưa đón)
- Search for hotels or flights with filters
- Detail pages for hotels and flights with descriptions, images, ratings, and prices
- Booking functionality with order confirmation
- User registration and login
- User order management page
- Responsive design using Bootstrap 5
- SQLite database by default

## Installation

1. Clone the repository or copy the project files.

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

6. Load sample data fixtures (if provided):

```bash
python manage.py loaddata fixtures/sample_data.json
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open your browser and go to `http://127.0.0.1:8000/` to access the website.

## Notes

- Media files (hotel images) require proper media settings in development.
- You can customize the templates and static files in the `home/templates` and `home/static` directories.
- For production deployment, configure database, static/media files, and security settings accordingly.

## License

This project is for educational purposes.
