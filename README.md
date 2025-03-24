# FastAPI Microservice with Celery

## Overview
This project is a FastAPI-based microservice that supports user authentication, product and category management, asynchronous data processing with Celery, and data export functionality. It is designed to be modular and scalable, following best practices.

## Features
### 1. User Authentication (JWT-based)
- Signup and login with JWT tokens.
- Secure password storage in the database.
- Protected API endpoints requiring authentication.

### 2. Product Management
- CRUD APIs for managing products.
- Product fields: `ID`, `category_id`, `title`, `description`, `price`, `status`, `created_at`, `updated_at`.

### 3. Category Management
- Create and fetch categories.
- Category fields: `ID`, `name`.

### 4. Asynchronous Data Processing (Celery)
- `/generate-products` API to generate dummy products asynchronously.
- Celery workers handle background tasks.

## How to Run the Project

### Prerequisites
- Python
- MySQL (configured in `settings.py` file)
- Redis (for Celery, if using asynchronous tasks)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application
1. Start the FastAPI server:
   ``` 
   python main.py
   ```
2Access the API documentation:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints
### Authentication
- `POST /signup` - Register a new user.
- `POST /login` - Authenticate and receive a JWT token.

### Product Management
- `POST /products` - Create a product.
- `GET /products` - Get all products.
- `GET /products/{id}` - Get product details.
- `PUT /products/{id}` - Update a product.
- `DELETE /products/{id}` - Delete a product.

### Category Management
- `POST /categories` - Create a category.
- `GET /categories` - Get all categories.

### Async Data Processing
- `POST /generate-products` - Generate dummy products asynchronously.
## Future Enhancements
- `GET /export` - Export products to CSV/Excel and get the download link.
- AES encryption for response data.
- Complete Docker setup with Docker Compose.

## Branch Information
This code is available on the `feat/assignment_changes` branch.
