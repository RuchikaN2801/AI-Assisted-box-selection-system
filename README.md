# AI-Assisted Box Selection System

## Project Overview

This project is a Django REST Framework application that recommends the most suitable shipping box for an ecommerce order.

The recommendation is based on:

1. Product dimensions
2. Product weight
3. Box dimensions
4. Box weight capacity
5. Box cost

The system selects the lowest-cost box that can accommodate the order.

---

## Features

* Create and manage products
* Create and manage boxes
* Create orders with multiple products
* Recommend a suitable box for an order
* REST API endpoints for all operations
* Unit tests for box selection logic

---

## Technology Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd AI-Assisted-box-selection-system
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the server:

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

* name
* length
* width
* height
* weight

### Box

* name
* length
* width
* height
* max_weight
* cost

### Order

* created_at

### OrderItem

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
3. Checks if product dimensions fit inside the box.
4. Checks if the total weight is within the box capacity.
5. Finds all valid boxes.
6. Selects the valid box with the lowest cost.

If no suitable box is found, the system returns a message indicating that no box is available.

---

## Running Tests

Run:

```bash
python manage.py test
```

Example output:

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
├── config/
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
├── requirements.txt
└── manage.py
```
