# Cinebh Application automation - UI and API tests - Atlantbh Quality Assurance Python Internship

## Project description

This is a repository in which I have placed both UI and API tests and necessary dependencies for running tests for Cinebh Application.

## Prerequisites

Test and environment are set up and written on macOS operating system. To run the test you need to have installed following:

[Python3](https://www.python.org/downloads/) - choose the version according to your macOS

[Homebrew](https://brew.sh/) - package manager for macOS

[PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac) - best IDE for running and writing tests in Python

[Postman](https://www.postman.com/downloads/) - recommended, download desktop app to run API requests effectively

[Docker](https://www.docker.com/) - frontend and backend stored in containers, and built using Docker images


## Installation

All the dependencies are placed in **requirements.txt** file. Simply copy in the terminal command below:

## 1. Clone the Repository
```
git clone[https://github.com/cinebh-1/Cinebh-Application-Automation---Atlantbh-Quality-Assurance-Python-Internship.git](https://github.com/cinebh-1/Cinebh-Application-Automation---Atlantbh-Quality-Assurance-Python-Internship.git)
```
```
cd CinemaAppAtlantBh

```

## 2. Clone frontend and backend of application
```
git clone[https://github.com/cinebh-1/qa-collaboration.git](https://github.com/cinebh-1/qa-collaboration.git)
```

## 3. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```
macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate
Windows:
python -m venv .venv
.venv\Scripts\activate
```
## 4. Install Dependencies
Install the required Python packages listed in requirements.txt:
```
pip install -r requirements.txt
```
## 5. Install Playwright Browsers
Playwright requires its own browser binaries (Chromium, Firefox, WebKit).
```
playwright install
```
## Configuration
Create a .env file in the root directory of the project. This file will store the connection details for the deployed application and database.
# Application URLs and other necessary variables 
```
BASE_URL=http://localhost:8080/api/v1
BASE_URL_UI=http://localhost:5173/
TEST_DELETE_USER_SECRET=mariotester13!
JWT_SECRET=b5d8f38c1ffc9b07499b7ac0bd7a67d313267207eb3f4fc0d3775a178f079688
RESEND_API_KEY=generate your own
STRIPE_SECRET_KEY=generate your own
STRIPE_WEBHOOK_SECRET=generate your own
TEST_DELETE_USER_SECRET=place anything you want

# Database Connection
DB_URL=jdbc:postgresql://db:5432/cinebh_db
DB_USER=cinebh_user
DB_PASSWORD=cinebh123
POSTGRES_USER=cinebh_user
POSTGRES_PASSWORD=cinebh123
POSTGRES_DB=cinebh_db

# Email Integration (Gmail IMAP)
GMAIL_APP_PASSWORD=generate your own Gmail app password
```
## Project structure

Below is the project structure tree schema

```bash
├── pages
│   ├── currently_showing_page.py
│   ├── home_page.py
│   ├── page_manager.py
│   ├── signin_page.py
│   ├── signup_page.py
│   └── upcoming_movies_page.py
├── tasks
│   ├── api_tasks.py
│   └── ui_tasks.py
├── test_data
│   └── projection_data.py
├── tests
│   ├── API_tests
│   │   └── test_smoke_api.py
│   ├── UI_tests
│   │   └── test_smoke.py
│   └── conftest.py
└── utilities
    ├── email_getter.py
    ├── logging.py
    └── user_data.py
├── README.md
├── api.Dockerfile
├── e2e.Dockerfile
├── pytest.ini
├── requirements.txt

```
## Running Tests

To run tests, use the following command

```bash
  python -m pytest tests/select_desired_test_file.py
```

To use test markers, created in **pytest.ini** file, simply run the command in terminal

```bash
  python -m pytest -m desired_test_marker  
```

## Generating Reports

To generate reports, and run the command below:

```bash
  allure serve allure-results
```
## Author

[@mnizicqa](https://github.com/mnizicqa)

## License

[MIT](https://choosealicense.com/licenses/mit/)