# Credit Card Transaction Matching

![alt text](images/image.png)

# About

- This is a quick credit card transaction matching solution. The aim is to create a rewards calculation system that calculates the total monthly reward points earned based on a customer's credit card purchases.
- This simple server has one API endpoint, which consumes a list of transactions, and computes the max earn from that list, for the user that transacted on those transactions.

# How to Run

### Virtual Environment

Launch a Python virtual environment. First navigate to project root directory:

```bash
python -m venv venv
```

Activate the virtual environment:
On MacOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

To check whether the python interpreter is the one created by virtual environment, run:

```bash
which python3
```

This should point to the python interpreter within the `venv` directory.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch the webserver

```bash
fastapi run src/main.py
```

Once finished, deactivate the python virtual environment:

```bash
deactivate
```

# API Docs

By default, FastAPI will generate OpenAPI standard Swagger docs for us:

- Served at: http://0.0.0.0:8000
- API Docs: API docs: http://0.0.0.0:8000/docs
