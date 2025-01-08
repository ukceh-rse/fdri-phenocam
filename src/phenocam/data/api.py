from collections.abc import AsyncGenerator

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from phenocam.data.vectorstore import SQLiteVecStore, vector_store

app = FastAPI()


async def get_db() -> AsyncGenerator[SQLiteVecStore]:
    store = vector_store("sqlite", "./data/vectors/test.db")
    try:
        yield store
    finally:
        store.db.close()


class SimilarityQuery(BaseModel):
    url: str
    n_results: int = 25


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}


@app.post("/query/similar")
async def query_similar(query: SimilarityQuery, db: SQLiteVecStore = Depends(get_db)) -> dict:
    try:
        embeddings = db.get(query.url)
        results = db.closest(embeddings=embeddings, n_results=query.n_results)
        return {"urls": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
