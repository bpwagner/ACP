import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

#variables
gameW = 400
gameH = 400

dotSize = 10
totalDots = (gameW *gameH )/(dotSize*dotSize)

#list of colors
bgColor = (0,0,0)
snekColor =  (0,255,0)
snekBorderColor =  (255,255,0)
appleColor =  (255,0,0)
appleBorderColor =  (255,255,255)
dots = 3

#snake direction
leftDirection = False
rightDirection = True
upDirection = False
downDirection = False

#random apple place
applePoint = (random.randint(2, gameW/dotSize-2) * 10, random.randint(2, gameH/dotSize-2) * 10)
print(applePoint)
segments = []

#add snake segments
for i in range(0, dots):
    segments.append((150 - i * dotSize, 150))

# Set up the window.
windowSurface = pygame.display.set_mode((gameW, gameH), 0, 32)
pygame.display.set_caption('Snek')

gameOver = False

def checkApple():
    global dots
    global applePoint

    #snakes head == apple
    #print(segments[0])
    #print(applePoint)
    if segments[0][0] == applePoint[0] and segments[0][1] == applePoint[1]:
        for i in range(1):
            segments.append((0,0))
            dots = dots+1
        applePoint = (random.randint(2, gameW / dotSize-2) * 10, random.randint(2, gameH / dotSize-2) * 10)
        print("apple collision")

def checkCollision():
    #return true or false if we hit something
    #x component of head of snake
    if segments[0][0] < 0 or segments[0][0] > gameW:
        return True

    if segments[0][1] < 0 or segments[0][1] > gameH:
        return True

    #see if we bite ourselves
    for i in range(dots-1, 1, -1):
        if segments[i][0] == segments[0][0] and segments[i][1] == segments[0][1]:
            return True

    return False


# Set up the music.
#pickUpSound = pygame.mixer.Sound('pickup.wav')
#pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=4096,
#                  allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.music.load('./game/background.mid')
pygame.mixer.music.play(-1, 0.0)
#musicPlaying = True

appleImage = pygame.image.load('cherry.png')
appleImage = pygame.transform.scale(appleImage, (10, 10))

font = pygame.font.SysFont("comicsansms", 72)

# Run the game loop.
while not gameOver:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                leftDirection = True
                rightDirection = False
                upDirection = False
                downDirection = False

            if event.key == K_RIGHT or event.key == K_d:
                leftDirection = False
                rightDirection = True
                upDirection = False
                downDirection = False

            if event.key == K_UP or event.key == K_w:
                leftDirection = False
                rightDirection = False
                upDirection = True
                downDirection = False

            if event.key == K_DOWN or event.key == K_s:
                leftDirection = False
                rightDirection = False
                upDirection = False
                downDirection = True

    # Draw the background onto the surface.
    windowSurface.fill(bgColor)

    #draw apple
    player = pygame.Rect(applePoint[0], applePoint[1],dotSize , dotSize)
    windowSurface.blit(appleImage, player)

    #ygame.draw.ellipse(windowSurface, appleColor,
    #            Rect(applePoint[0], applePoint[1],
    #                 dotSize , dotSize))

    # draw snake
    pygame.draw.ellipse(windowSurface, snekColor,
                Rect(segments[0][0], segments[0][1],
                     dotSize, dotSize))

    for i in range(1,dots):
        pygame.draw.rect(windowSurface, snekColor,
                    Rect(segments[i][0], segments[i][1],
                    dotSize, dotSize))

    #the body
    for i in range(dots - 1, 0, -1):
        segments[i] = (segments[(i - 1)][0], segments[(i - 1)][1])

    #the head
    if leftDirection:
        segments[0] = (segments[0][0] - dotSize, segments[0][1])

    if rightDirection:
        segments[0] = (segments[0][0] + dotSize, segments[0][1])

    if upDirection:
        segments[0] = (segments[0][0] , segments[0][1] - dotSize)

    if downDirection:
        segments[0] = (segments[0][0] , segments[0][1] + dotSize)

    checkApple()
    gameOver = checkCollision()

    text = font.render(str(len(segments)), True, (0, 128, 255))
    windowSurface.blit(text, (100,100))


    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick_busy_loop(12);

#end of game loop

print("game over")