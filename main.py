from fastapi import FastAPI, UploadFile, Form
from interview.session import InterviewSession
from interview.response import AudioResponse

app = FastAPI()

# Global session (for MVP)
session = InterviewSession(user_id="guest", role="software engineer")

@app.post("/upload/")
async def upload_audio(file: UploadFile):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    response = AudioResponse(file_location)
    session.add_response(response)

    return {
        "transcript": response.transcript,
        "tone": response.tone_data,
        "feedback": response.feedback
    }

@app.get("/next-question/")
def get_question():
    return {"question": session.next_question()}
