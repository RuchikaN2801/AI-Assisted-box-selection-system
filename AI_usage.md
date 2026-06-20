# AI_USAGE.md

## AI Tools Used

1. ChatGPT
2. GitHub Copilot


## Purpose of AI Usage

AI tools were used to assist with:

* Understanding project requirements
* Designing the database models
* Generating Django and Django REST Framework code
* Creating API endpoints
* Implementing box recommendation logic
* Writing unit tests
* Preparing project documentation

## Prompts Used

Examples of prompts provided to AI tools:

* Design a Django-based box recommendation system for ecommerce orders.
* Generate Django models for Product, Box, Order, and OrderItem.
* Create Django REST Framework serializers and viewsets.
* Implement logic to recommend the most suitable shipping box based on dimensions, weight, and cost.
* Generate unit tests for the box selection service.
* Create README.md and project documentation.


## Accepted Output

The following AI-generated suggestions were accepted:

* Initial project structure
* Django model definitions
* REST API implementation using Django REST Framework
* Service layer structure for box recommendation
* Unit test templates
* Documentation templates



## Modified Output

The following AI-generated outputs were modified before being used:

* Adjusted model fields and naming conventions.
* Refined the recommendation algorithm to check dimensions, weight limits, and volume.
* Improved API responses and endpoint structure.
* Updated documentation to match the final implementation.


## Rejected Output

The following suggestions were not used:

* Recommendation logic based only on volume calculations.
* Placing business logic directly inside API views.
* Unnecessary features that were outside the assignment scope.

## Mistakes Found in AI Output

* Some initial suggestions relied only on product volume and box volume, which could incorrectly recommend boxes where products would not physically fit.
* Some generated code required adjustment to fit the final project structure and assignment requirements.
* Test discovery suggestions required modification to work correctly with the Django project structure.


## Verification Process

The final implementation was verified through:

1. Manual testing of all API endpoints.
2. Creating sample products, boxes, and orders through the API.
3. Testing the box recommendation endpoint with different scenarios.
4. Running Django unit tests.
5. Reviewing application behavior and API responses.
6. Verifying that the recommended box satisfied dimension, weight, and cost requirements.

## Human Contribution

All AI-generated outputs were reviewed, validated, and modified where necessary. Final decisions regarding architecture, business logic, testing, and documentation were made after manual evaluation and verification.
