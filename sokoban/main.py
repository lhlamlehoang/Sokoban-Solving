import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
level = ''
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        OPTIONS_BUTTON = Button(image=None, pos=(900, 400), 
                    text_input="OPTIONS", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=None, pos=(640, 600), 
                    text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        OPTIONS_BUTTON.changeColor(PLAY_MOUSE_POS)
        OPTIONS_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    select_Level()
                if OPTIONS_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Solve()

        pygame.display.update()
def select_Level():
    global level
    input_rect = pygame.Rect(800,140,150,50)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        pygame.draw.rect(SCREEN, "white",input_rect,2)
        level_input = get_font(45).render(level,True, "white")
        SCREEN.blit(level_input,(input_rect.x + 40, input_rect.y+5))
        #pygame.display.flip()
        PLAY_TEXT = get_font(45).render("Enter your level", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                    text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_START = Button(image=None, pos=(640, 400), 
                    text_input="START", font=get_font(40), base_color="White", hovering_color="Green")
        
        PLAY_START.changeColor(PLAY_MOUSE_POS)
        PLAY_START.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_START.checkForInput(PLAY_MOUSE_POS):
                    play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    level = level[0:-1]
                else: level += event.unicode 

        pygame.display.flip()
        pygame.display.update()
def Solve():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("green")

        OPTIONS_TEXT = get_font(45).render("Choose your solving algorithm!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        SOLVE_DFS = Button(image = None, pos = (640, 200),
                           text_input="DFS", font =get_font(75), base_color="Black", hovering_color="White")
        SOLVE_BFS = Button(image = None, pos = (640, 300),
                           text_input="BFS", font =get_font(75), base_color="Black", hovering_color="White")
        SOLVE_ASTAR = Button(image = None, pos = (640, 400),
                           text_input="DFS", font =get_font(75), base_color="Black", hovering_color="White")
        SOLVE_UCS = Button(image = None, pos = (640, 500),
                           text_input="DFS", font =get_font(75), base_color="Black", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        SOLVE_DFS.changeColor(OPTIONS_MOUSE_POS)
        SOLVE_DFS.update(SCREEN)

        SOLVE_BFS.changeColor(OPTIONS_MOUSE_POS)
        SOLVE_BFS.update(SCREEN)

        SOLVE_ASTAR.changeColor(OPTIONS_MOUSE_POS)
        SOLVE_ASTAR.update(SCREEN)

        SOLVE_UCS.changeColor(OPTIONS_MOUSE_POS)
        SOLVE_UCS.update(SCREEN)
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    play()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_Level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Solve()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
