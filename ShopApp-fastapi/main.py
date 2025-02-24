from fastapi import FastAPI
import uvicorn

from api import router as api_router

from core.config import settings


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)

