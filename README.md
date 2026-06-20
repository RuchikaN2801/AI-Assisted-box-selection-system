# AI-Assisted Box Selection System

## Project Overview

This project is a Django REST Framework application that recommends the most suitable shipping box for an ecommerce order.

The recommendation is based on:

<<<<<<< HEAD
- Product dimensions
- Product weight
- Box dimensions
- Box weight capacity
- Box cost

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

<<<<<<< HEAD
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

<<<<<<< HEAD

---

## Important

After editing, your README **must not contain** any of these:

```text
<<<<<<< HEAD
=======
>>>>>>>
```

Search the entire file and remove all conflict markers.

---

## Save the file

Then run:

```bash
git add README.md
```

Continue the rebase:

```bash
git rebase --continue
```

If Git opens an editor:

### In VS Code

Save and close the file.

### In terminal Vim editor

Press:

```text
Esc
```

then type:

```text
:wq
```

and press Enter.

---

## After Rebase Completes

Push:

```bash
git push
```

---

## Verify

Run:

```bash
git status
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### If `git rebase --continue` gives another conflict

Run:

```bash
git status
```

and paste the output. I'll tell you exactly which file to fix next and what commands to run.
