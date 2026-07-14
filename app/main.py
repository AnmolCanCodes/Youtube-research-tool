from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

try:
    from app.api.routes import router
except ModuleNotFoundError:  # pragma: no cover - supports running from the app directory
    from api.routes import router

app = FastAPI(title="YouTube Research Tool")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=router,
    prefix="/api",
    tags=["Research Outline Generator"],
)

frontend_dir = Path(__file__).resolve().parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/", include_in_schema=False)
async def root():
    return FileResponse(frontend_dir / "index.html")