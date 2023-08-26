from typing import Tuple
from pygame import font, Rect, draw, mouse
from screen import screen

button_font = font.Font(None, 60)


class Button:
    def __init__(self, text: str, pos: Tuple[int, int], width: int = 0, height: int = 0,
                 font: font.Font = button_font):
        self.pressed = False
        self.elevation = 4
        self.dynamic_elevation = 4
        self.original_y_pos = pos[1]

        width = min(350, len(text) * 30) if not width else width

        self.top_rect = Rect(pos, (width, 60 if not height else height))
        self.top_color = "#008080"

        self.bottom_rect = Rect(pos, (width, self.elevation))
        self.bottom_color = "#005050"

        text_surf = font.render(text, True, "#DEBA69")
        text_rect = text_surf.get_rect(center=self.top_rect.center)
        self.text = text_surf, text_rect

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text[1].center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=16)
        draw.rect(screen, self.top_color, self.top_rect, border_radius=16)
        screen.blit(*self.text)

    def is_clicked(self):
        mouse_pos = mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#9FE2BF"
            self.bottom_color = "#8FD2AF"
            if mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            elif self.pressed:
                self.dynamic_elevation = self.elevation
                self.pressed = False
                return True
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = "#008080"
            self.bottom_color = "#005050"

        return False
