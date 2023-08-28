from enum import Enum


class AppMode(Enum):
    TITLE_SCREEN: str = "title_screen"
    MAIN_SCREEN: str = "sorting_screen"
    TRANSITION: str = "transition"
