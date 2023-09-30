from typing import Dict
from app_operations.divisors import divisors
from screens.screen_data import SCREEN_WIDTH, SCREEN_HEIGHT


class ListData:
    list_size: int = 0

    def __init__(self) -> None:
        self.divisors_list = divisors()
        ListData.list_size = self.divisors_list[2]

    @staticmethod
    def get_surf_rect_geometry(list_size: int) -> Dict[str, float]:
        return {
            "width": SCREEN_WIDTH / list_size,
            "height_idx": SCREEN_HEIGHT / list_size
        }
