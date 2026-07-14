# YouTube Research Tool

A simple AI-powered web application that turns a single topic into a structured YouTube video outline.

The app accepts a topic from the user, sends it to a FastAPI backend, and returns a polished outline with:
- title
- hook
- description
- sections
- examples
- call-to-action (CTA)

## Features

- Clean and modern web interface
- FastAPI backend for API requests
- LLM-powered outline generation
- Fallback outline generation if the AI provider is unavailable
- Simple local development workflow

## Project Structure

```text
youtube-research-tool/
├── app/
│   ├── api/
│   ├── core/
│   ├── frontend/
│   ├── llms/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── requirements.txt
├── .env
├── .gitignore
└── Readme.md
```

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- HTML, CSS, and JavaScript
- OpenAI / Gemini-compatible LLM integration

## Prerequisites

Make sure you have Python installed on your machine.

## Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd youtube-research-tool
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root
   ```env
   GEMINI_API_KEY=your_api_key_here
   MODEL_NAME=gemini-2.0-flash
   ```

## Running the Project

Start the backend server:

```bash
source .venv/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Then open the app in your browser:

```text
http://127.0.0.1:8000/
```

## API Endpoint

### Generate Outline

```http
POST /api/generate
Content-Type: application/json
```

Example request:

```json
{
  "title": "Python automation"
}
```

Example response:

```json
{
  "title": "Python automation",
  "hook": "Why Python automation matters right now",
  "description": "A quick starter outline for Python automation.",
  "sections": ["Introduce the topic", "Share key points", "Add an example"],
  "examples": ["Real-world example", "Comparison example"],
  "cta": "Subscribe for more ideas"
}
```

## Testing

Run tests locally:

```bash
pytest -q
```

## Deployment Notes

This project is designed to be deployed as a Python/FastAPI application. For production deployment, use a platform such as Render or Railway.

## License

This project is intended for learning and personal use.
