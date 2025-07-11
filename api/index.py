import sys
import os

# Add the parent directory to the Python path so we can import the app module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import create_app

# Create the FastAPI app instance
app = create_app()

# Export the app for Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 