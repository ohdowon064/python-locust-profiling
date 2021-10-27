import uvicorn as uvicorn
from fastapi import FastAPI, Header, Depends
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from users import router as users_router
from items import router as items_router


async def get_token_header(x_token: str = Header(...)):
    if x_token != "this-is-token":
        raise HTTPException(status_code=401, detail="Not Authorized")


app = FastAPI()


@app.get("/")
async def index():
    return JSONResponse(
        status_code=200,
        content={"Hello": "World!"}
    )


@app.get("/login")
async def login():
    return JSONResponse(
        status_code=201,
        content={"x_token": "this-is-token"}
    )


app.include_router(router=users_router, dependencies=[Depends(get_token_header)])
app.include_router(router=items_router, dependencies=[Depends(get_token_header)])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
