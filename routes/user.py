from curses.ascii import US
from fastapi import APIRouter, Response, status
from config.bd import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users', response_model= list[User], tags= ['User'])
def get_users():
    return userEntity(conn.local.user.find())

@user.post('/users/', response_model= list[User], tags =['Users'])
def create_users(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id" : id})
    return userEntity(user)

@user.get('/user/{id}', response_model= User, tags= ['Users'])
def find_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/users/')
def create_user():
    return {"Holis"}

@user.put('/users/{id}')
def update_user():
    return {"Holis"}

@user.delete('/users/{id}')
def delete_user():
    return {"Holis"}
