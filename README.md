# Office Booking API

This is a Django-based API for managing office bookings, rooms, and related functionalities. It also includes automatic API documentation using Swagger and ReDoc.

## Features:
- Manage offices, rooms, and bookings via API endpoints
- Interactive API documentation through Swagger and ReDoc
- SQLite database for development (can be switched to PostgreSQL for production)

## Setup and Installation

### Prerequisites:
- Python 3.12+
- Django 5.1.3+
- Django REST Framework
- drf_yasg (for API documentation)

### Installation Steps:
1. **Clone the repository:**

    ```bash
    git clone https://github.com/Bakhti-developer/office_booking.git
    cd office_booking
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    This will set up the SQLite database for development (you can switch to a different database if needed):

    ```bash
    python manage.py migrate
    ```

4. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

5. **Run the development server:**

    Start the development server with:

    ```bash
    python manage.py runserver
    ```

    Your API should now be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### API Endpoints:
- **Offices:** `/api/offices/`
- **Rooms:** `/api/rooms/`
- **Bookings:** `/api/bookings/`

### API Documentation:
- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
