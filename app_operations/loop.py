from typing import List
from pygame import display, event, quit as pg_quit
from gen_surf_rect_list import gen_surf_rect_list
from quit_loop import quit_loop
from restart import restart
from screen import screen


def loop(nums: List[int], idx: int = -1, second_idx: int = -1, pivot: int = -1) -> None:
    # NOTE: Add clock with said FPS if your computer can't handle the heat

    for e in event.get():
        if quit_loop(e):
            pg_quit()
            exit()
        if restart(e):
            raise StopIteration

    screen.fill("#DEBA69")
    surf_rect_array = gen_surf_rect_list(nums, idx, second_idx, pivot)
    for surf, rect in surf_rect_array:
        screen.blit(surf, rect)

    display.update()
