from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model_loader import predict_url

app = FastAPI()

# ✅ Allow requests from Chrome extension
origins = [
    "chrome-extension://__EXTENSION_ID__",
    "http://localhost",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
def predict(request: URLRequest):
    url = request.url
    prob, label = predict_url(url)
    return {"url": url, "probability": float(prob), "label": label}
