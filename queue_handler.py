from models import NotificationRequest
from services import process_notification
import threading
import queue

# Simulated message queue
notification_queue = queue.Queue()

def send_notification(notification: NotificationRequest):
    notification_queue.put(notification)

def worker():
    while True:
        notification = notification_queue.get()
        if notification:
            process_notification(notification)
        notification_queue.task_done()

# Start a background thread to process the queue
threading.Thread(target=worker, daemon=True).start()
