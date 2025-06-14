from fastapi import FastAPI
from recommendation import recommend_trips
from models import RecommendationRequest

app = FastAPI()

@app.post("/recommend_trips")
def get_recommendations(request: RecommendationRequest):
    recommended_trips = recommend_trips(request)
    return {"recommended_trips": recommended_trips}

