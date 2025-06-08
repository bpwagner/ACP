import pygame
from pygame.locals import *

class Snek:
    def __init__(self):
        self.bgColor = "black"
        self.snekColor = "green"
        self.snekBorderColor = "yellow"
        self.appleColor = "red"
        self.appleBorderColor = "white"
        self.segs = 3
        self.segSize = 10
        self.totalSegs = (640 * 400) / (self.segSize * self.segSize)

        self.segments = []
        # add snake segments
        for i in range(0, segs):
            self.segments.append((150 - i * segSize, 150))



class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        print("really cool")

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(pygame.Color("white"))

        color = pygame.Color("red")
        pygame.draw.rect(self._display_surf, color, pygame.Rect(20, 20, 30, 23))
        pygame.display.update()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    #create the app object and call on_execute
    print("mitchel is cool")
    theApp = App()
    theApp.on_execute()
