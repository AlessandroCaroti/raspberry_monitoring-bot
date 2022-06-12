from enum import Enum
from typing import List

class User:
    def __init__(self, uid: int, name: str, telegram_id: str, permissions: List[str]):
        self.id: int = uid
        self.name: str = name
        self.telegram_id: str = str(telegram_id)
        self.permissions: List[str] = permissions
