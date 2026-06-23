from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head><meta charset="utf-8"><title>MAESTRO Verify Test</title></head>
      <body>
        <h1>MAESTRO Verify Test</h1>
        <p>Welcome to the MAESTRO verify test application.</p>
        <p>MAESTRO is an AI-powered software engineering agent that automates coding tasks by planning, writing, and validating code changes across a project.</p>
      </body>
    </html>
    """
