from math import sin
from typing import List, Tuple
from pygame import font, Rect, Surface, time
from button import Button
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT


class TitleScreen:
    FONT = None

    def __init__(self) -> None:
        self.button = Button("Start",
                             (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 100),
                             width=500, height=150,
                             font=font.Font(TitleScreen.FONT, 220))

        self.title_surfs, self.title_rects = TitleScreen.create_title()

        self.title_screen_title_rects_start_y = [rect.y for rect in self.title_rects]
        self.going_up = True

        self.made_by_text, self.made_by_rect = TitleScreen.create_made_by_text()

    @staticmethod
    def create_title() -> Tuple[List[Surface], List[Rect]]:
        title_font = font.Font(TitleScreen.FONT, 220)
        title_surfaces = [title_font.render(text, True, "#008080")
                          for text in ("SORTING ALGORITHMS", "VISUALISER")]

        title_rects = [surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (140 * i) - 150))
                       for i, surf in enumerate(title_surfaces)]

        return title_surfaces, title_rects

    @staticmethod
    def create_made_by_text() -> Tuple[Surface, Rect]:
        made_by_font = font.Font(None, 30)
        made_by_surface = made_by_font.render("Made by: Victor L. Georgiev from VHSE \"John Atanasov\"",
                                              True, "#008080")

        made_by_rect = made_by_surface.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))

        return made_by_surface, made_by_rect

    @staticmethod
    def title_animation(rect: Rect, init_y: int) -> None:
        amplitude = 30
        frequency = 0.005

        displacement = amplitude * sin(frequency * time.get_ticks())

        rect.y = init_y + int(displacement)

    def draw(self) -> None:
        for surf, rect, init_y in zip(self.title_surfs, self.title_rects,
                                      self.title_screen_title_rects_start_y):
            TitleScreen.title_animation(rect, init_y)

            screen.blit(surf, rect)

        self.button.draw()

        screen.blit(self.made_by_text, self.made_by_rect)
