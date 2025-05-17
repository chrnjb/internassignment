from models import NotificationRequest
from data_store import store_notification

def process_notification(notification: NotificationRequest):
    # Simulate sending notification
    print(f"Sending {notification.type.upper()} to user {notification.user_id}: {notification.message}")
    
    # Save it to the data store (simulate DB)
    store_notification(notification)
