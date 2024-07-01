from typing import Dict
from datetime import datetime

from fastapi import FastAPI
from fastapi.requests import Request

from features.product.endpoints import product_router


# main app
app = FastAPI()

# add routers
app.include_router(product_router)


@app.get("/api/health")
def health_check(_: Request) -> Dict:
    return {
        "status": "healthy",
        "path": "/api",
        "timestamp": datetime.now(),
    }
