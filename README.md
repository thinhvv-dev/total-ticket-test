# Total ticket test

### Problem
```
A website that processes online orders with high concurrent traffic requires an order ID scheme of the format <date>-<sequential number> such as in "YYYYMMDD-nnnnn".
Sequence number will increase by 1 for each following order
Sequence number will start again from 1 for each day
Order id need unique. 
With high concurrent traffic and lots of orders being processed at the same time so duplicate order id may occur.
```

### Solution
```
1. Custom save method for model Orders with logic generate new order_id
2. Create repository function include logic create new Orders object
3. Use celery to create queue task to avoid conflict order_id exception
```

### Pros/Cons
- Pros:
```
This solution will make sure there is never an order_id conflict with high concurrent traffic
```
- Cons:
```
Any logic that wants to create a new order object must use the `repository.order_create` function
```

## Installation
```sh
$ cp .env.example .env
# pass value environment variables
```

### Basic Commands
- Run docker-compose
```bash
$ docker-compose up -d

# url
http://localhost:8083
```
- Interact container os
```bash
$ docker exec -it app sh

# If new model was created run migration
$ python manage.py makemigrations
$ python manage.py migrate

# If want to create super user
$ python manage.py createsuperuser
```

- If environment crash...
```bash
$ docker-compose down -v && docker-compose up --build
```
