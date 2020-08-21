import pygame
from settings import Settings
from game_stats import GameStats
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group

# pygame.init()

def run_game():
    """initialize game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a new instance to store game statistics
    stats = GameStats(ai_settings)

    # make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop of the game
    while True:
        # watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
