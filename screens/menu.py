from abc import ABC, abstractmethod
from typing import Tuple, Dict, Callable

from pygame import Surface, Rect
from pygame import font

from screens.button import Button
from screens.screen_data import screen


class Menu(ABC):
    def __init__(self, title: str, title_pos: Tuple[int, int], button_pos: Tuple[int, int], size: Tuple[int, int]) -> None:
        self.title = Menu.create_title(title, *title_pos)

        self.menu_surf, self.menu_rect = Menu.create_surf_rect(*button_pos, *size)

        self.buttons: Tuple[Button] = tuple()

    @staticmethod
    def create_title(title: str, x: int, y: int) -> Tuple[Surface, Rect]:
        title_font = font.Font(None, 100)
        title_surf = title_font.render(title, True, "#008080")
        title_rect = title_surf.get_rect(midtop=(x, y))
        return title_surf, title_rect

    @staticmethod
    def create_surf_rect(x: int, y: int, width: int, height: int) -> Tuple[Surface, Rect]:
        buttons_surf = Surface((width, height))
        buttons_surf.fill("#DEBA69")
        buttons_surf.set_alpha(220)
        buttons_rect = buttons_surf.get_rect(midtop=(x, y))

        return buttons_surf, buttons_rect

    def draw(self) -> None:
        screen.blit(self.menu_surf, self.menu_rect)

        for button in self.buttons:
            button.draw()

    @abstractmethod
    def create_buttons_mapper(self) -> Dict[Button, Callable]:
        pass

    @staticmethod
    @abstractmethod
    def create_buttons(buttons_to_create: Dict[str, Tuple[int, int]]) -> Tuple[Button, ...]:
        pass
