from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello":"world"}

@app.get("/search/{track_id}")
def search_track(track_id):
    return {"track_id": track_id}

