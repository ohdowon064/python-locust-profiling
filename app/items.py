from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.database import SimpleDatabase as Database

router = APIRouter()


@router.post("/items")
async def create_item():
    new_item = await Database.Items.create()

    return JSONResponse(
        status_code=201,
        content={"data": new_item}
    )


@router.get("/items")
async def get_items():
    items = await Database.Items.get_all()

    return JSONResponse(
        status_code=200,
        content={"data": items}
    )


@router.get("/item/{item_id}")
async def get_item(item_id: int):
    if item := await Database.Items.get(item_id) is None:
        raise HTTPException(status_code=404, detail=f"Not Exist Item {item_id}")

    return JSONResponse(
        status_code=200,
        content={"data": item}
    )
