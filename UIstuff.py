import pygame

class TextBox:
    def __init__(self, x = 0, y= 0, font_size = 64, font_colour = (0, 0, 0), text="Placeholder"):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font_colour = font_colour
    def draw(self, win):
        my_surface = pygame.font.Font(None, self.font_size).render(self.text, True, self.font_colour)
        win.blit(my_surface, (self.x, self.y))  

class Button:
    def __init__(self, x=0, y=0, width=64, height=64, passive_colour=(255, 255, 255), active_colour=(0, 0, 0), font_size=32, active_font=(255, 255, 255), passive_font=(0, 0, 0), border_width=10, icon_type="Text", icon="Demo", item_id="default"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.passive_colour = passive_colour
        self.active_colour = active_colour
        self.colour = passive_colour
        self.border_width = border_width

        self.font_size = font_size
        self.active_font = active_font
        self.passive_font = passive_font
        self.font_colour = passive_font
        self.font = pygame.font.Font(None, self.font_size)

        self.icon_type = icon_type
        self.icon = icon
        self.item_id = item_id
        self.active = False

        text_surface = self.font.render(self.icon, True, self.font_colour)
        text_surface_rect = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse):
            self.active = True
        else:
            self.active = False

        if click[0] and self.rect.collidepoint(mouse):
            return self.item_id

        if self.active:
            self.colour = self.active_colour
            self.font_colour = self.active_font
        else:
            self.colour = self.passive_colour
            self.font_colour = self.passive_font

        text_surface = self.font.render(self.icon, True, self.font_colour)

        text_surface_rect = pygame.Surface((self.width, self.height))
        text_surface_rect.fill(self.colour)
        text_surface_rect.blit(text_surface, (0, 0))
        win.blit(text_surface_rect, (self.x, self.y))
