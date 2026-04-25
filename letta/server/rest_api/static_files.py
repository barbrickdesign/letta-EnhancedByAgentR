from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse

DASHBOARD_FILE = Path(__file__).resolve().parent / "static" / "dashboard.html"


def mount_static_files(app: FastAPI):
    @app.get("/", include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse(url="/docs")

    @app.get("/dashboard", include_in_schema=False)
    @app.get("/dashboard/", include_in_schema=False)
    async def serve_dashboard():
        if DASHBOARD_FILE.exists():
            return FileResponse(DASHBOARD_FILE)
        return RedirectResponse(url="/docs")
