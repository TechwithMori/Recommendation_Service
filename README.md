# Recommendation Service

A scalable AI-driven recommendation service built with Django, PostgreSQL, and Docker.

## Features
- Django-based backend with REST framework
- PostgreSQL database integration
- AI-driven item recommendation system
- Dockerized setup for seamless deployment
- Includes tests for ensuring functionality

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:
- Python 3.10 or higher
- Docker and Docker Compose

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/TechwithMori/Recommendation_Service/new/master.git
    cd recommender_project
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Build and start the Docker containers**:
    ```sh
    docker-compose up --build
    ```

5. **Apply migrations**:
    ```sh
    docker-compose exec web python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

7. **Collect static files** (if needed):
    ```sh
    docker-compose exec web python manage.py collectstatic
    ```

## Running Tests

To run tests, use the following command:
```sh
docker-compose exec web python manage.py test
```

## Usage
Access the application at http://127.0.0.1:8000/ and the admin interface at http://127.0.0.1:8000/admin/.

## Contributing
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.
