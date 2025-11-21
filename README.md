# Multimedia Website

A modern Django web application for uploading, managing, and viewing multimedia content (images and videos). This project features a responsive UI with dark mode support and is ready for deployment.

## Features

-   **Media Management**: Upload, view, edit, and delete images and videos.
-   **Modern UI**: Clean, card-based layout with glassmorphism effects.
-   **Dark Mode**: Built-in dark/light theme toggle with preference persistence.
-   **Interactive Elements**: Animated menu buttons, smooth transitions, and dynamic file input feedback.
-   **Responsive Design**: Works seamlessly across desktop and mobile devices.

## Prerequisites

Before you begin, ensure you have the following installed:
-   [Python](https://www.python.org/downloads/) (3.8 or higher)
-   [Git](https://git-scm.com/downloads)

## Local Development Setup

Follow these steps to get the project running on your local machine for development or upscaling.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd assignment5
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Set up the local SQLite database.

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Project Structure

-   `media_app/`: Core application logic (models, views, forms).
-   `multimedia_website/`: Project settings and configuration.
-   `templates/`: HTML templates.
-   `static/`: CSS, JavaScript, and static assets.
-   `media/`: User-uploaded content (images/videos).

## Deployment

This project is configured for deployment on **Render**.

1.  Push your code to GitHub.
2.  Create a new **Web Service** on Render.
3.  Connect your GitHub repository.
4.  Render will automatically detect the `render.yaml` file (Blueprint) or you can configure manually:
    -   **Build Command**: `./build.sh`
    -   **Start Command**: `gunicorn multimedia_website.wsgi:application`
    -   **Environment Variables**:
        -   `PYTHON_VERSION`: `3.10.12` (or your version)
        -   `SECRET_KEY`: (Generate a strong key)
        -   `DATABASE_URL`: (Internal connection string if using Render Postgres)

## Contributing

If you'd like to upscale or improve this project:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.
