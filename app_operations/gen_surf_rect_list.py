from collections import deque
from typing import List, Tuple
from pygame import surface, Surface, Rect
from screens.screen_data import SCREEN_HEIGHT
from screens.list_data import ListData


def gen_surf_rect_list(nums: List[int], idx: int = -1,
                       second_idx: int = -1, pivot: int = -1) -> List[Tuple[Surface, Rect]]:
    surf_rect_geometry = ListData.get_surf_rect_geometry(ListData.list_size)

    surf_rect_list = []
    indexes = deque([idx, second_idx, -1])

    for i, num in enumerate(nums):
        surf = surface.Surface((surf_rect_geometry["width"], num * surf_rect_geometry["height_idx"]))
        current_index = indexes.popleft()
        if current_index == -1 or i != current_index:
            surf.fill("#008080")
            indexes.appendleft(current_index)
        else:
            surf.fill("#9FE2BF")

        if pivot != -1 and pivot == i:
            surf.fill("#673147")

        rect = surf.get_rect(
            bottomleft=(i * surf_rect_geometry["width"] + surf_rect_geometry["width"] // 2, SCREEN_HEIGHT)
        )
        surf_rect_list.append((surf, rect))

    return surf_rect_list
