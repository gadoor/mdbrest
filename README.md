# mdbrest
RESTful API for mongodb

# Tutorial
### Configuration
For now, and just to keep it simple, ```config.yml``` allows you to configure which **mongodb** instance you want the
API to connect to.

### Requests
For now, the CRUD request are kept simple

#### Create
```
POST /{database:required}/{collection:required}
BODY: JSON
```
#### Read
```
GET /{database:required}/{collection:required}/{oid:optional}
```
#### Update
**Update One**
```
PUT /{database:required}/{collection:required}/{oid:required}
BODY: JSON
```
**Update Many**
```
PATCH /{database:required}/{collection:required}
{
    "filter": {},
    "data": {}
}
```
#### Delete
```
DELETE /{database:required}/{collection:required}/{oid:required}
```

# N.B
This API is still under development and always changing.