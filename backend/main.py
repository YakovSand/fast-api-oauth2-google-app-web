from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

# Create FastAPI app
app = FastAPI(debug=True)

# Include router
app.include_router(router)

# Configure CORS middleware for frontend-backend communication during development
# Allow requests from the frontend running on localhost:3000
# Note: In production, configure CORS appropriately for your deployment setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],        
)
