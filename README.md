# Todo App

It is a to-do application where users can manage their to-do items. Users can also be part of projects as members.

## Features
* Users can register themselves and log in using their credentials.
* Users can create, read, update, and delete (CRUD) their own to-do tasks.
* Users can join and collaborate on projects as members.

## Prerequisites
* Python >=3.8, <=3.12
* Django 4.2
* Django REST Framework (DRF)
* PostgreSQL

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jtg-induction/BE-DIVESH-SINGH-UID-00807.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd BE-DIVESH-SINGH-UID-00807
   ```

3. **Create and activate a virtual environment:**
   * **On Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **On macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   ```bash
   cp .env.template .env
   ```
   *(Open the `.env` file and update it with your Django `SECRET_KEY` and PostgreSQL database credentials.)*

6. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

## Usage

Start the Django development server:
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000`.

## License
Distributed under the MIT License.
