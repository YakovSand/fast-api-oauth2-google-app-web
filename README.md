# OAuth2 Google Auth Platform Demo

This sample project demonstrates the OAuth2 authentication process using Google Auth Platform. 

## Setup Instructions

Follow the steps below to run both the backend and frontend.

### Backend (FastAPI)

1. Navigate to the `backend` directory:

    ```bash
    cd ./backend/
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload --port 8000
    ```

### Frontend (Vue + Vite)

1. Open a new terminal and navigate to the frontend directory:

    ```bash
    cd ./frontend/vite-project
    ```

2. Initialize the frontend project:

    ```bash
    npm init -y
    ```

3. Install the required dependencies:

    ```bash
    npm install
    ```

4. Install `vue-router` (required for routing):

    ```bash
    npm install vue-router@4
    ```

5. Install Vite plugin for Vue:

    ```bash
    npm install -D @vitejs/plugin-vue
    ```

6. Start the frontend development server:

    ```bash
    npm run dev
    ```

### Access the Application

1. Open your browser and go to `http://localhost:3000/`.

2. Click the **Login with Google** button to initiate the OAuth2 authentication process.

---

## Notes
- Ensure you have Node.js and Python installed on your machine.
- If you encounter any issues, check that all dependencies are correctly installed and your virtual environment is activated.
