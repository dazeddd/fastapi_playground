from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Query, Path
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: Optional[str] = Query(None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# query parameters and string validations
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results


    # @app.put("/items/{id}")



