from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import sessionmanager
from app.settings.config import DATABASE_URL,DEBUG
from app.routers import tasks
import uvicorn
import os
os.environ["PYTHONBREAKPOINT"] = "0"

@asynccontextmanager
async def lifespan(app: FastAPI):
    sessionmanager.init(DATABASE_URL)
    await sessionmanager.init_db()
    yield


app = FastAPI(lifespan=lifespan, debug=True)
app.include_router(tasks.router,prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8009, workers=1)