from fastapi import FastAPI, Query
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flight_search_api import search_flights

app = FastAPI(
    title="TripGain Flight Search API",
    description="Runs Playwright automation and returns flight data as JSON",
    version="1.0.0"
)


@app.get("/flight-search", response_model=List[Dict])
def flight_search(
    origin: str = Query(..., example="Bangalore"),
    destination: str = Query(..., example="Delhi"),
    journey_date: str = Query(..., example="2025-10-20")
):
    """Endpoint that triggers Playwright automation."""
    try:
        results = search_flights(origin, destination, journey_date)
        return results
    except Exception as e:
        # Return empty list to match response_model
        return []


# Run with: uvicorn flight_search_api:app --reload
