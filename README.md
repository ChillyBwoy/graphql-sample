# GraphQL Sample App

## Installation:

```
$ pip install virtualenv
$ virtualenv .env --no-site-packages
$ . .env/bin/activate
$ pip install -r requirements.txt
```

## Migrate
```
$ ./manage.py migrate
```

## Populate database:

### 1. Create users:
```
$ ./manage.py populate goods.User --count 40
```

### 2. Create categories:
```
$ ./manage.py populate goods.Category --count 15
```

### 3. Create products:
```
$ ./manage.py populate goods.Product --count 1000
```

### 4. Create reviews:
```
$ ./manage.py populate goods.ProductUserReview --count 5000
```

## Start app
```
$ ./manage.py runserver
```

navigate to http://localhost:8000/graphql/