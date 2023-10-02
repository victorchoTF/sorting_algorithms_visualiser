from typing import Optional, Tuple
from pygame import event
from app_operations.presentation_mode import presentation_mode
from app_operations.quit_loop import quit_loop
from handlers.app_mode import AppMode


def handle_events() -> Tuple[bool, Optional[AppMode]]:
    for e in event.get():
        if quit_loop(e):
            return False, None
        if presentation_mode(e):
            return True, AppMode.PRESENTATION_SCREEN
        
    return True, None
