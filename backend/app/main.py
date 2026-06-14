from fastapi import FastAPI

app = FastAPI(
    title="Astrovoya",
    description="A personal astrophotography atlas for tracking and cataloguing your journey across the night sky.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Astrovoya 🌌"}

@app.get("/health")
def health():
    return {"status": "ok"}