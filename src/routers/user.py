from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=150)


class User(UserCreate):
    id: int


users = {
    1: {"id": 1, "name": "Ivan", "age": 25},
    2: {"id": 2, "name": "Anna", "age": 22},
}


@router.get("/", response_model=list[User])
def get_users():
    return list(users.values())


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return users[user_id]


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_id = max(users.keys()) + 1
    users[new_id] = {
        "id": new_id,
        "name": user.name,
        "age": user.age,
    }

    return users[new_id]
