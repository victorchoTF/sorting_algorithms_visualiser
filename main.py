from typing import List, Tuple
from pygame import display, event, quit, Surface, Rect
from main_screen import MainScreen
from screen import screen, SCREEN_HEIGHT, clock
from app_operations.transition import transition
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from app_operations.quit_loop import quit_loop
from title_screen import TitleScreen
from enum import Enum


class AppMode(Enum):
    TITLE_SCREEN: str = "title_screen"
    MAIN_SCREEN: str = "sorting_screen"
    TRANSITION: str = "transition"


def handle_events() -> bool:
    for e in event.get():
        if quit_loop(e):
            return False
    return True


def handle_title_screen(title_screen: TitleScreen) -> Tuple[AppMode, None]:
    title_screen.draw()

    if title_screen.button.is_clicked():
        return AppMode.TRANSITION, None

    return AppMode.TITLE_SCREEN, None


def handle_main_screen(main_screen: MainScreen, num_list: List[int],
                       surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[AppMode, List[int],
                                                                            List[Tuple[Surface, Rect]]]:
    main_screen.draw(surf_rect_list)
    num_list, surf_rect_list = main_screen.buttons_check(num_list, surf_rect_list)

    return AppMode.MAIN_SCREEN, num_list, surf_rect_list


def handle_transition(title_screen: TitleScreen, main_screen: MainScreen,
                      surf_rect_list: List[Tuple[Surface, Rect]]) -> Tuple[AppMode, None]:
    transition(title_screen.draw, 1, "+")
    transition(lambda: main_screen.draw(surf_rect_list), SCREEN_HEIGHT, "-")

    return AppMode.MAIN_SCREEN, None


def main() -> None:
    title_screen: TitleScreen = TitleScreen()
    main_screen: MainScreen = MainScreen()

    num_list: List[int] = [num for num in range(1, 212)]
    surf_rect_list: List[Tuple[Surface, Rect]] = gen_surf_rect_list(num_list)

    current_mode: AppMode = AppMode.TITLE_SCREEN
    mode_handlers = {
        AppMode.TITLE_SCREEN: lambda: handle_title_screen(title_screen),
        AppMode.MAIN_SCREEN: lambda: handle_main_screen(main_screen, num_list, surf_rect_list),
        AppMode.TRANSITION: lambda: handle_transition(title_screen, main_screen, surf_rect_list),
    }

    run: bool = True
    while run:
        clock.tick(60)
        screen.fill("#DEBA69")

        run = handle_events()

        current_mode, *data = mode_handlers[current_mode]()
        num_list, surf_rect_list = data if data[0] is not None else (num_list, surf_rect_list)

        display.update()

    quit()


if __name__ == "__main__":
    main()
