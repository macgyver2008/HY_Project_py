import pygame
pygame.init()
display_width = 1300
display_height = 800
black = (0, 0, 0)
white = (255, 255, 255)
red = (122, 10, 10)
car_width = 400
car_height = 192
x = 390
y = 300

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('./raccer.png')
def car(carImg, x, y) :
    gameDisplay.blit(carImg, (x, y))

def text_object(text, front):
    textSurface = front.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width / 2), (display_height) / 2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
def crash():
    message_display('You gg')
def game_loop():
    x = (display_width * 0.45) # 10
    y = (display_height * 0.8) # 10
    x_change = 0
    y_change = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_r:
                    x = 0
                    y = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change  # x = x + x_change
        y += y_change
        gameDisplay.fill(white)
        car(carImg, x, y)

        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height or y < 0:
            crash()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
