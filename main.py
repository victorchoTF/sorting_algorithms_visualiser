from pygame import display, Surface, font, event
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT, clock
from button import Button
from sorting_functions import (selection_sort, bubble_sort, insertion_sort, cocktail_sort, quick_sort, merge_sort,
                               tin_sort, heap_sort, radix_sort, shell_sort, shuffle_list)
from app_operations.transition import transition
from app_operations.gen_surf_rect_list import gen_surf_rect_list
from app_operations.quit_loop import quit_loop

FONT = None


def main():
    def buttons_check():
        nonlocal num_list, surf_rect_list

        for button in buttons:
            if button.is_clicked():
                try:
                    num_list = SORTING_MAP[button](num_list)
                except StopIteration:
                    num_list = [num for num in range(1, 212)]

                surf_rect_list = gen_surf_rect_list(num_list)

    def buttons_draw():
        for button in buttons:
            button.draw()

    def sorting_screen_draw():
        for surf, rect in surf_rect_list:
            screen.blit(surf, rect)

        screen.blit(buttons_surf, buttons_rect)

        screen.blit(title_surf, title_rect)

        buttons_draw()

    def title_screen_draw():
        nonlocal going_up

        for surf, rect, init_y in zip(title_screen_title_surfs, title_screen_title_rects,
                                      title_screen_title_rects_start_y):
            if rect.y > init_y - 40 and going_up:
                going_up = True
                rect.y -= 2
            elif rect.y < init_y and not going_up:
                rect.y += 2
            else:
                going_up = not going_up

            screen.blit(surf, rect)

        title_screen_button.draw()

        screen.blit(made_by_text, made_by_rect)

    title_font = font.Font(FONT, 100)
    title_surf = title_font.render("Sorting Algorithms Visualiser", True, "#008080")

    selection_sort_button = Button("Selection Sort", (70, 90))
    bubble_sort_button = Button("Bubble Sort", (440, 90))
    cocktail_sort_button = Button("Cocktail Sort", (790, 90))
    insertion_sort_button = Button("Insertion Sort", (1160, 90))
    merge_sort_button = Button("Merge Sort", (1530, 90))

    quick_sort_button = Button("Quick Sort", (90, 160))
    tin_sort_button = Button("Tin Sort", (410, 160))
    heap_sort_button = Button("Heap Sort", (670, 160))
    radix_sort_button = Button("Radix Sort", (960, 160))
    shell_sort_button = Button("Shell Sort", (1280, 160))
    shuffle_button = Button("Shuffle", (1600, 160))

    buttons = tuple((selection_sort_button, bubble_sort_button, cocktail_sort_button,
                     insertion_sort_button, merge_sort_button, quick_sort_button, tin_sort_button, heap_sort_button,
                     radix_sort_button, shell_sort_button, shuffle_button))

    functions = tuple((selection_sort, bubble_sort, cocktail_sort, insertion_sort, quick_sort, merge_sort,
                       tin_sort, heap_sort, radix_sort, shell_sort, shuffle_list))

    SORTING_MAP = {button: lambda x, func=func: func(x) for button, func in zip(buttons, functions)}

    buttons_surf = Surface((SCREEN_WIDTH, 230))
    buttons_surf.fill("#DEBA69")
    buttons_surf.set_alpha(220)
    buttons_rect = buttons_surf.get_rect(topleft=(0, 0))
    buttons_rect.midtop = SCREEN_WIDTH // 2, 0
    title_rect = title_surf.get_rect(midtop=(buttons_rect.midtop[0], 10))

    title_screen_button = Button("Start",
                                 (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 100),
                                 width=500,
                                 height=150,
                                 font=font.Font(FONT, 220))

    title_screen_title_font = font.Font(FONT, 220)
    title_screen_title_surfs = [title_screen_title_font.render(text, True, "#008080")
                                for text in ("SORTING ALGORITHMS", "VISUALISER")]
    title_screen_title_rects = [surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (140 * i) - 150))
                                for i, surf in enumerate(title_screen_title_surfs)]

    title_screen_title_rects_start_y = [rect.y for rect in title_screen_title_rects]
    going_up = True

    made_by_font = font.Font(None, 30)
    made_by_text = made_by_font.render("Made by: Victor L. Georgiev from VHSE \"John Atanasov\"", True, "#008080")
    made_by_rect = made_by_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))

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
                title_screen_draw()

                if title_screen_button.is_clicked():
                    mode = "transition"

            case "sorting_screen":
                sorting_screen_draw()
                buttons_check()

            case "transition":
                transition(title_screen_draw, 1, "+")
                transition(sorting_screen_draw, SCREEN_HEIGHT, "-")
                mode = "sorting_screen"

        display.update()

    quit()


if __name__ == "__main__":
    main()
