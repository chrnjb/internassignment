from pydantic import BaseModel
from typing import List

class NotificationRequest(BaseModel):
    user_id: str
    type: str  # "email", "sms", or "in-app"
    message: str

class Notification(BaseModel):
    user_id: str
    type: str
    message: str
