import pygame
import pyautogui
import os

pygame.init()

path = "C:/bearpaint/images"
try:
    os.makedirs(path)
except:
    pass


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (240, 98, 145)
BLUE = (0, 30, 255)
screen_size = (1920, 1080)

name = input("Name?")
brush_size_width = int(input("Brush size width?"))
brush_size_height = int(input("Brush size height"))
eraser_size_width = int(input("Eraser size width?"))
eraser_size_height = int(input("Eraser size height"))

def draw_pixel_at_mouse(color, brush_size_width, brush_size_height, surface):
    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
    pygame.draw.rect(surface, color, pygame.Rect(mouse_x_pos, mouse_y_pos, brush_size_width, brush_size_height))

def create_custom_color():
    custom_color_R = int(input("Red value?\n"))
    custom_color_G = int(input("Green value?\n"))
    custom_color_B = int(input("Blue value?\n"))


    custom_color = custom_color_R, custom_color_G, custom_color_B

    return custom_color

def get_color_at_mouse():
    return display_surface.get_at((pygame.mouse.get_pos()))[:3]


current_color = BLACK

use_custom_color = input("Use a custom color? (Y/N)")

if use_custom_color == "Y":
    current_color = create_custom_color()

if use_custom_color == "N":
    pass

display_surface = pygame.display.set_mode(screen_size)

pygame.display.set_caption("BearPaint")

display_surface.fill(WHITE)

for i in range(0, 255):
    red = 0 + i
    green = 0 + i
    blue = 0 + i                            #black to white
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(10, 25 + i, 50, 2))

for i in range(0, 255):
    red = 0
    green = 0 + i
    blue = 0                                #black to green
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(10, 280 + i, 50, 2))


for i in range(0, 255):
    red = 0 + i
    green = 0
    blue = 0                                #black to red
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(10, 535 + i, 50, 2))


for i in range(0, 255):
    red = 0
    green = 0
    blue = 0 + i                            #black to blue
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(10, 785 + i, 50, 2))

for i in range(0, 255):
    red = 0
    green = 0 + i                          #black to cyan
    blue = 0 + i
    rgb = red,green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(60, 25 + i, 50, 2))

for i in range(0, 255):
    red = 0 + i
    green = 0                           #black to purple/pink
    blue = 0 + i
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(60, 280 + i, 50, 2))

for i in range(0, 255):
    red = 0 + i
    green = 0 + i                       #black to yellow
    blue = 0
    rgb = red, green, blue
    pygame.draw.rect(display_surface, rgb, pygame.Rect(60, 535 + i, 50, 2))

while True :
    for i in range(0,255):
        rgb = current_color
        pygame.draw.rect(display_surface, rgb, pygame.Rect(60, 785 + i, 50, 2))




    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

        if pygame.mouse.get_pressed(num_buttons=3)[0]:  #LEFT mouse
            draw_pixel_at_mouse(current_color,brush_size_width, brush_size_height, display_surface)

        if pygame.mouse.get_pressed(num_buttons=3)[2]: #RIGHT mouse
            draw_pixel_at_mouse(WHITE, eraser_size_width,eraser_size_height, display_surface)

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_c]:
                current_color = create_custom_color()

            if pressed[pygame.K_p]:
                current_color = get_color_at_mouse()

            if pressed[pygame.K_s]:
                brush_size_width = int(input("Brush size width?"))
                brush_size_height = int(input("Brush size height"))
                eraser_size_width = int(input("Eraser size width?"))
                eraser_size_height = int(input("Eraser size height"))

            if pressed[pygame.K_q]:
                Screenshot = pyautogui.screenshot(region=(110,0, 1810, 1080))
                Screenshot.save('C:/bearpaint/images/' + name + '.png')

            if pressed[pygame.K_m]:
                red = current_color[0]
                green = current_color[1]
                blue = current_color[2]

                color_to_blend_with = get_color_at_mouse()              #rgb mixing
                new_red = (color_to_blend_with[0] + red) / 2
                new_green = (color_to_blend_with[1] + green) / 2
                new_blue = (color_to_blend_with[2] + blue) / 2
                current_color = new_red, new_green, new_blue

            if pressed[pygame.K_l]:
                image_to_load_filename = input("Image to load?")
                loaded_image = pygame.image.load("C:/bearpaint/images/" + image_to_load_filename)
                display_surface.blit(loaded_image, pygame.mouse.get_pos())

    pygame.display.update()


