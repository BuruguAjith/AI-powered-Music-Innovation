import logging
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Mount Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Add CORS middleware to allow frontend and backend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or replace with specific URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def index(request: Request):
    """
    Renders the index page (main HTML page).
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-music")
async def generate_music(prompt: str = Form(...), duration: int = Form(...)):
    """
    Generates music based on the user's text prompt and the specified duration.
    """
    logging.info(f"Received prompt: {prompt}, duration: {duration}")

    try:
        # In this case, we're returning the static SoundHelix song as the generated music
        melody_url = generate_melody()

        # Return the generated music URL in the response
        return JSONResponse(content={"url": melody_url})

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return JSONResponse(content={"error": "Failed to generate music"}, status_code=500)
