# Challenge 2: Mofa’s Kitchen Buddy

## Overview

Mofa's Kitchen Buddy is a backend system designed to help Mofa manage the ingredients in his kitchen and suggest recipes based on the available ingredients. The system is powered by an AI-driven chatbot integrated with a Large Language Model (LLM), allowing Mofa to interact with the system and receive personalized recipe recommendations based on his preferences, such as cravings or specific meal types.

## Project Structure

The project consists of the following main components:

- **Ingredient Management API**: Handles adding, updating, retrieving, and deleting ingredients.
- **Recipe Management API**: Manages storing and retrieving recipes, including parsing saved recipe text data.
- **Chatbot API**: Interacts with users and provides recipe suggestions based on available ingredients and preferences.
  
The backend is built with Django, and the project is structured to be scalable and maintainable.

## API Documentation

This section provides detailed information about the available APIs, including how to interact with them.

### 1. **Ingredient Management APIs**

#### - Add Ingredient
- **Route**: `/api/ingredients/add/`
- **Method**: `POST`
- **Description**: Adds a new ingredient to the kitchen inventory.
- **Request Payload**:
  ```json
  {
    "name": "Sugar",
    "quantity": "500g",
    "category": "Sweeteners"
  }
  ```
- **Sample Response**:
  ```json
  {
    "name": "Sugar",
    "quantity": "500g",
    "category": "Sweeteners"
  }
  ```
- **Status Codes**:
  - `201 Created`: Ingredient added successfully.
  - `400 Bad Request`: Invalid data provided.

#### - Get Ingredient by Name
- **Route**: `/api/ingredients/`
- **Method**: `GET`
- **Description**: Retrieves ingredients by their name.
- **Query Parameters**:
  - `name`: The name of the ingredient to search for.
- **Sample Request**:
  ```
  GET /api/ingredients/?name=sugar
  ```
- **Sample Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Sugar",
      "quantity": "500g",
      "category": "Sweeteners"
    }
  ]
  ```
- **Status Codes**:
  - `200 OK`: Ingredients found.
  - `400 Bad Request`: Missing or invalid query parameter.
  - `404 Not Found`: No ingredients found.

#### - Update Ingredient
- **Route**: `/api/ingredients/update/<id>/`
- **Method**: `PUT`
- **Description**: Updates the details of an existing ingredient.
- **Request Payload**:
  ```json
  {
    "name": "Sugar",
    "quantity": "1kg",
    "category": "Sweeteners"
  }
  ```
- **Sample Response**:
  ```json
  {
    "id": 1,
    "name": "Sugar",
    "quantity": "1kg",
    "category": "Sweeteners"
  }
  ```
- **Status Codes**:
  - `200 OK`: Ingredient updated successfully.
  - `400 Bad Request`: Invalid data provided.
  - `404 Not Found`: Ingredient with the specified ID not found.

#### - Delete Ingredient
- **Route**: `/api/ingredients/delete/<id>/`
- **Method**: `DELETE`
- **Description**: Deletes an ingredient from the kitchen inventory.
- **Sample Response**:
  ```json
  {
    "message": "Ingredient deleted successfully."
  }
  ```
- **Status Codes**:
  - `200 OK`: Ingredient deleted successfully.
  - `404 Not Found`: Ingredient with the specified ID not found.



## Setup Instructions

### Requirements

- Python 3.8+
- Django 5.x
- Django REST Framework
- SQLite (or any other database of your choice)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hasib-39/Light-Fair-School_preli.git
   cd Light-Fair-School_preli/Challenge_2
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request with a detailed description of the changes.

---

