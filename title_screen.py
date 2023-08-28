from typing import List

from pygame import font, Rect, Surface
from button import Button
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT


class TitleScreen:
    FONT = None

    def __init__(self) -> None:
        self.button = Button("Start",
                             (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 100),
                             width=500, height=150,
                             font=font.Font(TitleScreen.FONT, 220))

        self.title_surfs = TitleScreen.create_title_surfaces()
        self.title_rects = self.create_title_rects()

        self.title_screen_title_rects_start_y = [rect.y for rect in self.title_rects]
        self.going_up = True

        self.made_by_text = TitleScreen.create_made_by_surface()
        self.made_by_rect = self.made_by_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))

    @staticmethod
    def create_title_surfaces() -> List[Surface]:
        title_font = font.Font(TitleScreen.FONT, 220)
        title_surfaces = [title_font.render(text, True, "#008080")
                          for text in ("SORTING ALGORITHMS", "VISUALISER")]

        return title_surfaces

    def create_title_rects(self) -> List[Rect]:
        title_rects = [surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (140 * i) - 150))
                       for i, surf in enumerate(self.title_surfs)]

        return title_rects

    @staticmethod
    def create_made_by_surface() -> Surface:
        made_by_font = font.Font(None, 30)
        made_by_surface = made_by_font.render("Made by: Victor L. Georgiev from VHSE \"John Atanasov\"",
                                              True, "#008080")
        return made_by_surface

    def title_animation(self, rect: Rect, init_y: int) -> None:
        if rect.y > init_y - 40 and self.going_up:
            self.going_up = True
            rect.y -= 2
        elif rect.y < init_y and not self.going_up:
            rect.y += 2
        else:
            self.going_up = not self.going_up

    def draw(self) -> None:
        for surf, rect, init_y in zip(self.title_surfs, self.title_rects,
                                      self.title_screen_title_rects_start_y):
            self.title_animation(rect, init_y)

            screen.blit(surf, rect)

        self.button.draw()

        screen.blit(self.made_by_text, self.made_by_rect)
