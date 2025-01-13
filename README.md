**GI Corporation Assessment task**

A simple Django project that processes user data from a CSV
file.

---

## **Features**

- RESTful API build using Django

## **Installation**

### Clone the Repository

```
git clone <repository-url>
cd <repository-folder>
```

### Using docker:-

    `cd gi_csv_app`

    `docker-compose -f docker-compose.yaml up -d`

    `docker exec -it <container_name/id> bash`

   `python manage.py migrate`

### Without using docker:-

    `cd gi_csv_app`

    `py manage.py migrate`

    `py manage.py runserver`
