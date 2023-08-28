from pygame import display, event, quit
from main_screen import MainScreen
from screen import screen, SCREEN_HEIGHT, clock
from app_operations.transition import transition
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from app_operations.quit_loop import quit_loop
from title_screen import TitleScreen


def main() -> None:
    title_screen = TitleScreen()
    main_screen = MainScreen()

    num_list = [num for num in range(1, 212)]
    surf_rect_list = gen_surf_rect_list(num_list)

    mode = "title_screen"
    run = True
    while run:
        clock.tick(60)
        screen.fill("#DEBA69")

        for e in event.get():
            if quit_loop(e):
                run = False

        match mode:
            case "title_screen":
                title_screen.draw()

                if title_screen.button.is_clicked():
                    mode = "transition"

            case "sorting_screen":
                main_screen.draw(surf_rect_list)
                num_list, surf_rect_list = main_screen.buttons_check(num_list, surf_rect_list)

            case "transition":
                transition(title_screen.draw, 1, "+")
                transition(lambda: main_screen.draw(surf_rect_list), SCREEN_HEIGHT, "-")
                mode = "sorting_screen"

        display.update()

    quit()


if __name__ == "__main__":
    main()
