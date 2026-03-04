from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    #Initial Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    player = Player(x, y) 



    while True: 
        dt = clock.tick(60) / 1000.0   
        log_state()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        

      
            

    
if __name__ == "__main__":
    main()
