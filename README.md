# External API Integration in Django with Django REST Framework

This repository provides an example of how to integrate an external API into a Django project using the Django REST Framework (DRF). The example demonstrates how to make API requests, handle responses, and expose the data through your own API endpoints.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Setting Up the Environment](#setting-up-the-environment)
- [Configuring the API Integration](#configuring-the-api-integration)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)

## Prerequisites

- Python (3.6+)
- Django (3.0+)
- Django REST Framework (3.12+)

## Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/JoseMiracle/EXTERNAL_API_CONSUMPTION.git
cd EXTERNAL_API_CONSUMPTION.git
```

## Setting Up the Environment

1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install the required packages:

```bash
pip install -r requirements.txt
```


```bash
python manage.py runserver
```

Access the DRF APIS at `http://127.0.0.1:8000/external-api-integration/`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or a pull request.


