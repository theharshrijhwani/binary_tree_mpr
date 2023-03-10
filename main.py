import pygame
from sys import exit
import node

pygame.init()
clock = pygame.time.Clock()


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y = pos[1]
        # top-rectangle
        self.top_rect = pygame.Rect((pos), (width, height))
        self.top_color = '#484848'

        # bottom-rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#8C8C8C'
        # text
        self.text_surface = button_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(
            center=self.top_rect.center)

    def draw(self):
        # elevation_logic
        self.top_rect.y = self.original_y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color,
                         self.bottom_rect, border_radius=15)

        pygame.draw.rect(screen, self.top_color,
                         self.top_rect, border_radius=15)
        screen.blit(self.text_surface, self.text_rect)
        self.check_clicks()

    def check_clicks(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # self.top_color = '#BEBEBE'
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    # print('clicked')
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#484848'


# just the screen width and height stored in variables
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 720

# setting the title of application window
pygame.display.set_caption('Binary Tree')

# main display surface which contains animatiion frame, buttons, input bar, etc.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((33, 33, 33))

# the animation surface
main_surface = pygame.Surface((900, 600))
main_surface.fill((66, 66, 66))

# heading font
heading_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 35)
title_text_surface = heading_font.render(
    "Binary Search Tree and Operations", True, (255, 255, 255))

# button font
button_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 15)

# creating required buttons

# insert, search, delete and depth
insert_button = Button('Insert', 150, 40, (1000, 140), 3)
search_button = Button('Search', 150, 40, (1000, 210), 3)
delete_button = Button('Delete', 150, 40, (1000, 280), 3)
depth_button = Button('Depth',150,40,(1170,140),3)
clear_button = Button('Clear', 150, 40, (1170,210), 3)

# traversal heading
traversal_font = pygame.font.Font(
    'fonts\helvetica\Helvetica_CE_Medium.ttf', 30)
traversal_heading_surface = traversal_font.render('Traversal', True, '#FFFFFF')
# tfont_rect = traversal_heading_surface.get_rect(centerx = insert_button.top_rect.centerx) .... failed attempt

# traversal buttons
inorder_button = Button('InOrder', 150, 40, (1000, 430), 3)
preorder_button = Button('PreOrder', 150, 40, (1000, 500), 3)
postorder_button = Button('PostOrder', 150, 40, (1000, 570), 3)

# flip
# main_surface.blit((50,50))

screen.blit(main_surface, (50, 55))
screen.blit(title_text_surface, (200, 10))

result_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 30)
result_surface = result_font.render('',True,'#FFFFFF')

# drawing buttons
# insert_button.draw()
# search_button.draw()
# delete_button.draw()
# search_button.draw()
# delete_button.draw()

# traversal-heading
screen.blit(traversal_heading_surface, (1015, 360))

# traversal buttons
# inorder_button.draw()
# preorder_button.draw()
# postorder_button.draw()
# inorder_button.draw()
# preorder_button.draw()
# postorder_button.draw()


# Inserting Input-box and Label using rectangle
text_input = ""

# Define textbox dimensions and position
textbox_width = 300
textbox_height = 40
textbox_position = (1000, 60)

# Define textbox color and border
textbox_color = (255, 255, 255)
textbox_border_color = (0, 0, 0)
textbox_border_width = 2
textbox_rect = pygame.Rect(
    textbox_position[0], textbox_position[1], textbox_width, textbox_height)
pygame.draw.rect(screen, textbox_color, textbox_rect)

# update using flip
pygame.display.flip()

# drawing the node

def draw_bubble(screen, x, y, radius, label, bg_color):
    # define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # draw circle
    pygame.draw.circle(screen, bg_color, (x, y), radius)

    # draw label
    font = pygame.font.SysFont(None, 30)
    text = font.render(label, True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def search_node(s_node):
    elapsed_time = 0
    # s_node = search_node(val)
    while (elapsed_time <= 10):
        if(s_node==None):
            result_surface = result_font.render('Not found',True,'#FFFFFF')
            screen.blit(result_surface,(50,680))
        else:
            if elapsed_time%2==0:
                draw_bubble(screen, s_node.x_pos, s_node.y_pos,20, str(s_node.val), '#808000')
                pygame.display.update()
                pygame.time.delay(500)
            else:
                draw_bubble(screen, s_node.x_pos, s_node.y_pos,20, str(s_node.val), '#800080')
                pygame.display.update()
                pygame.time.delay(500)
        elapsed_time += 1

def depth(s_node):
    if(s_node==None):
        result_surface = result_font.render('Not found', True, '#FFFFFF')
        screen.blit(result_surface, (50,680))
    else:
        result_surface = result_font.render('The depth of node is {}'.format(s_node.level), True, '#FFFFFF')
        screen.blit(result_surface, (50,680))
# main event loop


root = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        insert_button.draw()
        search_button.draw()
        delete_button.draw()
        inorder_button.draw()
        preorder_button.draw()
        postorder_button.draw()
        depth_button.draw()
        clear_button.draw()
        if event.type == pygame.MOUSEBUTTONDOWN and insert_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked insert')
            print(f'{text_input}')
            n = node.Node(int(text_input))
            prev = node.give_coordinates(n)
            if (root == None):
                root = n
            else:
                print(prev)
                pygame.draw.line(screen, '#FFFFFF',
                                 (prev[0], prev[1]), (n.x_pos, n.y_pos), 2)
                draw_bubble(screen, prev[0], prev[1],
                            20, str(prev[2]), '#808000')

            print(f'X: {n.x_pos}, Y: {n.y_pos}')
            draw_bubble(screen, n.x_pos, n.y_pos, 20, text_input, '#808000')

            text_input = ''

        elif event.type == pygame.KEYDOWN and textbox_rect.collidepoint(pygame.mouse.get_pos()):
            if event.unicode.isalnum():
                text_input += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
        elif event.type == pygame.MOUSEBUTTONDOWN and search_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked search')
            print(f'{text_input}')
            # s_node = node.search_node(int(text_input))
            search_node(node.search_node(int(text_input)))
        elif event.type == pygame.KEYDOWN and textbox_rect.collidepoint(pygame.mouse.get_pos()):
            if event.unicode.isalnum():
                text_input += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
        elif event.type == pygame.MOUSEBUTTONDOWN and delete_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked delete')
        elif event.type == pygame.MOUSEBUTTONDOWN and inorder_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked inorder')
        elif event.type == pygame.MOUSEBUTTONDOWN and preorder_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked preorder')
        elif event.type == pygame.MOUSEBUTTONDOWN and postorder_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked postorder')
        elif event.type == pygame.MOUSEBUTTONDOWN and depth_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked depth')
            print(f'{text_input}')
            depth(node.search_node(int(text_input)))
        elif event.type == pygame.MOUSEBUTTONDOWN and clear_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            root = None
            node.binary_tree = []
            # screen.fill((33, 33, 33))
            main_surface.fill('#424242')
            
            

    # Rendering the Text
    pygame.draw.rect(screen, textbox_color, textbox_rect)
    font = pygame.font.Font('fonts/helvetica/Helvetica_CE_Medium.otf', 30)
    text_surface = font.render(text_input, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=textbox_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)
