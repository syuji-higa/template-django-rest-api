## Commands

```sh
# Create project
$ django-admin.py startproject {project_name} .

# Add module
$ poetry add {module_name}
$ poetry add -D {module_name}

# Rebuild
$ docker-compose build

# Create app
$ docker-compose run web python manage.py startapp {app_name}

# Create migration file
$ docker-compose run web python manage.py makemigrations {app_name}

# Migration
$ docker-compose run web python manage.py migrate

# Create admin
$ docker-compose run web python manage.py createsuperuser

# Start image
$ docker-compose up

# Stop image
$ docker-compose down

# Check image
$ docker-compose images
```

### Factory boy

```sh
$ docker-compose run web python manage.py shell
```

```python
# add data
from books.factory import BookFactory
BookFactory.create_batch(10)

# check data
from books.models import Book
for x in Book.objects.all(): print('isbn={0}, title={1}, price={2}, publisher={3}, published={4}'.format(x.isbn, x.title, x.price, x.publisher, x.published))

```
