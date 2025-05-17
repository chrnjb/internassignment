from typing import List
from models import NotificationRequest

# Simulated DB
user_notifications = {}

def store_notification(notification: NotificationRequest):
    if notification.user_id not in user_notifications:
        user_notifications[notification.user_id] = []
    user_notifications[notification.user_id].append(notification)

def get_user_notifications(user_id: str):
    return user_notifications.get(user_id, [])
