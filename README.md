# Created by: @pdonaire1

# Installation:

```
virtualenv store_krato
source store_krato/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
The data is already charged in db.sqlite3

# Users:
```
user: admin
pass: Password123
user: userone
pass: Password123
```

# DataBase Graph
![alt text](https://github.com/pdonaire1/store_krato/blob/master/Diagrama1.png)

# Endpoints
## Administration
URL of administration: `/admin/`
## Tasks:
- 5.a. GET todos los usuarios de una tienda:
`/api/v1/stores/{id}/users/`
sample:
`/api/v1/stores/1/users/`

- 5.b. GET de todas las tiendas dado el id de un usuario.
`/api/v1/users/{user_id}/stores/`
sample:
`/api/v1/users/2/stores/`

- 5.c. GET de todas las tiendas de una ciudad, ASOCIADAS A UN USUARIO.
`/api/v1/cities/{city_id}/stores/?user_id={user_id}`
sample:
`/api/v1/cities/2/stores/?user_id=1`
