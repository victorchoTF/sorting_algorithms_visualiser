from typing import List
from screens.screen_data import SCREEN_WIDTH


def divisors() -> List[int]:
    result = []
    previous: int = 0

    for num in range(20, min((SCREEN_WIDTH // 2 + 1), 700)):
        if SCREEN_WIDTH % num != 0:
            continue

        if num - 100 < previous:
            continue

        previous = num
        result.append(num)

    result.insert(0, 30)
    result = result[:5] if len(result) >= 5 else result

    return result
