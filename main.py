from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model data pengguna
class User(BaseModel):
    id: int
    name: str
    email: str

# Data pengguna sebagai database sementara
users_db = []

# Endpoint untuk mengambil semua pengguna
@app.get("/users", response_model=List[User])
async def get_users():
    return users_db

# Endpoint untuk mengambil pengguna berdasarkan ID
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Endpoint untuk menambahkan pengguna baru
@app.post("/users", response_model=User)
async def create_user(user: User):
    if any(existing_user.id == user.id for existing_user in users_db):
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_db.append(user)
    return user

# Endpoint untuk memperbarui pengguna berdasarkan ID
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Endpoint untuk menghapus pengguna berdasarkan ID
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    global users_db
    users_db = [user for user in users_db if user.id != user_id]
    return {"message": "User deleted successfully"}
