# Senior LLM / ML Engineer Portfolio

Single-file FastAPI portfolio website for **Shwet Prakash**.

## Local Run

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8008
   ```
4. Open:
   - `http://127.0.0.1:8008/web`
   - `http://127.0.0.1:8008/`
   - `http://127.0.0.1:8008/health`

## Deploy on Render (Web Service)

1. Push this folder to a GitHub repository.
2. In Render, create a **New Web Service** and connect that repo.
3. Use these settings:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Click **Deploy**.

After deploy, Render gives a public URL you can share.

## Files

- `app.py`: Main portfolio app (single Python file)
- `requirements.txt`: Python dependencies
- `resume_shwet.docx`: Resume source and downloadable file at `/resume`
