from typing import List, Tuple
from pygame import display, quit, Surface, Rect
from main_screen import MainScreen
from screen import screen, clock
from title_screen import TitleScreen
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from handlers.app_mode import AppMode
from handlers.handle_events import handle_events
from handlers.handle_title_screen import handle_title_screen
from handlers.handle_main_screen import handle_main_screen
from handlers.handle_transition import handle_transition


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
