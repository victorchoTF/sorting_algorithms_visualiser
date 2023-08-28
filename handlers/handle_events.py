from pygame import event
from app_operations.quit_loop import quit_loop


def handle_events() -> bool:
    for e in event.get():
        if quit_loop(e):
            return False
        
    return True
