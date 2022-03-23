from fastapi import APIRouter

user = APIRouter()

@user.get('/user/{id}')
def get_user():
    return {"Holis"}

@user.get('/users/')
def get_users():
    return {"Holis"}

@user.post('/users/')
def create_user():
    return {"Holis"}

@user.put('/users/{id}')
def update_user():
    return {"Holis"}

@user.delete('/users/{id}')
def delete_user():
    return {"Holis"}