from typing import List, Tuple
from pygame import display, quit, Surface, Rect

from handlers.handle_presentation_screen import handle_presentation_screen
from screens.list_data import ListData
from screens.main_screen import MainScreen
from screens.presentation_screen import PresentationScreen
from screens.screen_data import screen, clock
from screens.title_screen import TitleScreen
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from handlers.app_mode import AppMode
from handlers.handle_events import handle_events
from handlers.handle_title_screen import handle_title_screen
from handlers.handle_main_screen import handle_main_screen
from handlers.handle_transition import handle_transition


def main() -> None:
    title_screen: TitleScreen = TitleScreen()
    main_screen: MainScreen = MainScreen()
    presentation_screen: PresentationScreen = PresentationScreen()

    num_list: List[int] = [num for num in range(1, ListData.list_size)]
    surf_rect_list: List[Tuple[Surface, Rect]] = gen_surf_rect_list(num_list)

    current_mode: AppMode = AppMode.TITLE_SCREEN
    mode_handlers = {
        AppMode.TITLE_SCREEN: lambda: handle_title_screen(title_screen),
        AppMode.MAIN_SCREEN: lambda: handle_main_screen(main_screen, num_list, surf_rect_list),
        AppMode.PRESENTATION_SCREEN: lambda: handle_presentation_screen(presentation_screen),
        AppMode.TRANSITION: lambda: handle_transition(title_screen, main_screen, surf_rect_list),
    }

    run: bool = True
    while run:
        clock.tick(60)
        screen.fill("#DEBA69")

        run, data = handle_events()
        current_mode = data if data else current_mode

        current_mode, *data = mode_handlers[current_mode]()
        num_list, surf_rect_list = data if data[0] is not None else (num_list, surf_rect_list)

        display.update()

    quit()


if __name__ == "__main__":
    main()
