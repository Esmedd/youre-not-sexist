from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/slack/events")
async def slack_events(payload: dict):
    # Process Slack events here
    return {"message": "Event received"}
