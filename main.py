from fastapi import FastAPI, HTTPException
from models import NotificationRequest, Notification
from data_store import store_notification, get_user_notifications
from queue_handler import send_notification

app = FastAPI()

@app.post("/notifications")
def create_notification(notification: NotificationRequest):
    try:
        send_notification(notification)
        return {"message": "Notification sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}/notifications")
def read_user_notifications(user_id: str):
    return get_user_notifications(user_id)
from fastapi import FastAPI, HTTPException
from models import NotificationRequest, Notification
from data_store import store_notification, get_user_notifications
from queue_handler import send_notification

app = FastAPI()

@app.post("/notifications")
def create_notification(notification: NotificationRequest):
    try:
        send_notification(notification)
        return {"message": "Notification sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}/notifications")
def read_user_notifications(user_id: str):
    return get_user_notifications(user_id)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notification Service API!"}
