"""
Policy Impact Transparency AI — Main API Server
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.simulate import router as simulate_router

app = FastAPI(
    title="Policy Impact Transparency AI",
    description=(
        "See how government decisions affect YOU "
        "before they happen."
    ),
    version="1.0.0",
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(simulate_router, prefix="/api", tags=["Simulation"])


@app.get("/")
async def root():
    return {
        "name": "Policy Impact Transparency AI",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "scenarios": "/api/scenarios",
            "simulate": "/api/full-simulation",
            "compare": "/api/compare",
            "tax": "/api/quick-tax",
            "subsidies": "/api/subsidies",
        },
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}