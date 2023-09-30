from typing import Tuple, Dict, Callable, List

from pygame import Surface, Rect

from app_operations.gen_surf_rect_list import gen_surf_rect_list
from screens.list_data import ListData
from screens.button import Button
from screens.menu import Menu
from screens.screen_data import SCREEN_WIDTH, SCREEN_HEIGHT


class ListSizeMenu(Menu):
    LIST_SIZE_MENU_BUTTONS_TO_CREATE: Dict[str, Tuple[int, int]] = {
        f"{button_text}": pos for button_text, pos in
        zip(ListData().divisors_list, (
            (SCREEN_WIDTH - num, SCREEN_HEIGHT - 80) for num in (1050,
                                                                 850,
                                                                 650,
                                                                 450,
                                                                 250)
        ))
    }

    def __init__(self, title: str, title_pos: Tuple[int, int], button_pos: Tuple[int, int],
                 size: Tuple[int, int]) -> None:
        super().__init__(title, title_pos, button_pos, size)

        self.buttons = ListSizeMenu.create_buttons(ListSizeMenu.LIST_SIZE_MENU_BUTTONS_TO_CREATE)

        self.buttons_mapper = self.create_buttons_mapper()

        self.text = None

    @staticmethod
    def create_buttons(buttons_to_create: Dict[str, Tuple[int, int]]) -> Tuple[Button, ...]:
        buttons = tuple(Button(text, position, width=150)
                        for text, position in buttons_to_create.items())

        return buttons

    def create_buttons_mapper(self) -> Dict[Button, Callable]:
        return {button: func for button, func in zip(self.buttons, tuple(lambda: print(1) for _ in range(5)))}

    def buttons_check(self, num_list: List[int],
                      surf_rect_list: List[Tuple[Surface, Rect]]
                      ) -> Tuple[List[int], List[Tuple[Surface, Rect]]]:
        for button in self.buttons:
            if button.is_clicked():
                new_size = int(button.text_as_str)
                num_list = [num for num in range(1, new_size)]
                ListData.list_size = new_size
                surf_rect_list = gen_surf_rect_list(num_list)

        return num_list, surf_rect_list
