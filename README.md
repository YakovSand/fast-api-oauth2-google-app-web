# OAuth2 Google Auth Platform Demo

This sample project demonstrates the OAuth2 authentication process using Google Auth Platform. 

## Prerequisites

Before running this project, make sure you have:

1. **OAuth2 Client**: You need to have an OAuth2 client created in Google Cloud Platform (GCP) to use Google authentication. Follow these steps to create your OAuth2 client:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing project.
   - Navigate to **APIs & Services > Credentials**.
   - Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Set up the OAuth consent screen and create the client ID.
   - Note the **Client ID** and **Client Secret** provided, as you will need these for configuring the backend.

More details: https://developers.google.com/identity/protocols/oauth2/web-server#python_1

2. **Node.js** and **npm**: Ensure you have Node.js and npm installed for the frontend setup.
   - Download and install Node.js from [here](https://nodejs.org/).

3. **Python 3.x**: Ensure you have Python 3 installed for the backend setup.
   - Download and install Python from [here](https://www.python.org/).

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
- If you encounter any issues, check that all dependencies are correctly installed and your virtual environment is activated.
