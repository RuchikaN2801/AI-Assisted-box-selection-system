# AI-Assisted Box Selection System

## Project Overview

This project is a Django REST Framework application that recommends the most suitable shipping box for an ecommerce order.

The recommendation is based on:

* Product dimensions
* Product weight
* Box dimensions
* Box weight capacity
* Box cost

The system selects the lowest-cost box that can safely accommodate the order.

---

## Features

* Create and manage products
* Create and manage boxes
* Create orders with multiple products
* Recommend a suitable box for an order
* REST API endpoints for all operations
* Unit tests for box selection logic
* Swagger API documentation

---

## Technology Stack

* Python
* Django
* Django REST Framework
* SQLite
* drf-spectacular (Swagger/OpenAPI)
* Git & GitHub

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-Assisted-box-selection-system
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## Data Models

### Product

Stores product information.

Fields:

* name
* length
* width
* height
* weight

### Box

Stores available shipping boxes.

Fields:

* name
* length
* width
* height
* max_weight
* cost

### Order

Represents a customer order.

Fields:

* created_at

### OrderItem

Stores products and quantities within an order.

Fields:

* order
* product
* quantity

---

## API Endpoints

### Products

```http
GET /api/products/
POST /api/products/
```

### Boxes

```http
GET /api/boxes/
POST /api/boxes/
```

### Orders

```http
GET /api/orders/
POST /api/orders/
```

### Box Recommendation

```http
GET /api/orders/<order_id>/recommend_box/
```

---

## Recommendation Logic

For each order, the system:

1. Calculates total order weight.
2. Calculates total order volume.
3. Checks whether product dimensions fit inside the box.
4. Verifies that the total weight does not exceed the box capacity.
5. Finds all valid boxes.
6. Selects the valid box with the lowest cost.

If no suitable box is found, the system returns a message indicating that no box is available.

---

## Example Response

Request:

```http
GET /api/orders/1/recommend_box/
```

Response:

```json
{
    "recommended_box": "Small Box",
    "cost": 20.0
}
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

ReDoc:

```text
http://127.0.0.1:8000/api/redoc/
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/api/schema/
```

---

## Running Tests

Run:

```bash
python manage.py test
```

Example Output:

```text
Found 2 test(s).

..
----------------------------------------------------------------------
Ran 2 tests

OK
```

---

## Project Structure

```text
AI-Assisted-box-selection-system/

├── products/
├── boxes/
├── orders/
├── services/
│   └── box_selector.py
├── docs/
│   └── AI_CHAT_TRANSCRIPT.pdf
├── screenshots/
├── config/
├── README.md
├── AI_usage.md
├── test_output.md
├── requirements.txt
└── manage.py
```

---

## Chat Transcript

The AI conversation transcript used during development is included in:

```text
docs/AI_CHAT_TRANSCRIPT.pdf
```

---

## Assumptions

* All products are treated as rectangular cuboids.
* Product rotation is allowed during dimension checks.
* Orders are packed into a single shipping box.
* Advanced 3D bin-packing optimization is outside the scope of this project.

---

## Author

Ruchika Navrange
