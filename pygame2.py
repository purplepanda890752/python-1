import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 700

display_surface = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Adding image and background")
background_image = pygame.transform.scale(
    pygame.image.load('background.jpg').covert(), (SCREEN_HEIGHT, SCREEN_WIDTH)) 

cartoon_image = pygame.transform.scale(
   pygame.image.load('cartoon.png').convert_alpha(), (200,200))
cartoon_rect = cartoon_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))
text = pygame.font.Font(None,30).render("Hello World", True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        display_surface.bilt(background_image, (0,0))
        display_surface.bilt(cartoon_image, cartoon_rect)
        display_surface.bilt(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    
if __name__=='__main__':
    game_loop()