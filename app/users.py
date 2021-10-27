from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.database import SimpleDatabase as Database


router = APIRouter()


@router.post("/users")
async def create_user():
    new_user = await Database.Users.create()

    return JSONResponse(
        status_code=201,
        content={"data": new_user}
    )


@router.get("/users")
async def get_users():
    users = await Database.Users.get_all()

    return JSONResponse(
        status_code=200,
        content={"data": users}
    )


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    if user := await Database.Users.get(user_id) is None:
        raise HTTPException(status_code=404, detail=f"Not Exist User {user_id}")

    return JSONResponse(
        status_code=200,
        content={"data": user}
    )
