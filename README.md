# internassignment

# Notification Service (FastAPI + HTML + JS)

This is a full-stack notification service with Email, SMS, and In-App support (simulated).

## 🔧 Features
- FastAPI backend
- Beautiful frontend with dark/light mode
- In-memory queue simulation
- Toast alerts, loading spinner
- Responsive, animated UI

## 🧪 Endpoints
- `POST /notifications`
- `GET /users/{user_id}/notifications`

## ⚙️ Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
