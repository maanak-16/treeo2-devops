from fastapi import FastAPI

app = FastAPI(
    title="TreeO2 Backend API",
    description="A sample backend API for the TreeO2 DevOps Jenkins pipeline.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "TreeO2 Backend API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "treeo2-backend"
    }


@app.get("/metrics")
def metrics():
    return {
        "monitoring": "enabled",
        "api_status": 1,
        "service": "treeo2-backend"
    }


@app.get("/trees")
def get_trees():
    return [
        {
            "id": 1,
            "species": "Sandalwood",
            "farmer": "Farmer A",
            "status": "validated"
        },
        {
            "id": 2,
            "species": "Mahogany",
            "farmer": "Farmer B",
            "status": "pending"
        }
    ]


@app.get("/farmers")
def get_farmers():
    return [
        {
            "id": 1,
            "name": "Farmer A",
            "location": "Timor-Leste",
            "trees_registered": 120
        },
        {
            "id": 2,
            "name": "Farmer B",
            "location": "Timor-Leste",
            "trees_registered": 85
        }
    ]