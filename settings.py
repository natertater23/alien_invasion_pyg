class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        # Laser settings
        self.laser_speed = 3
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (255, 0, 0)
        self.lasers_allowed = 4
        # Alien settings
        self.alien_speed = 1
        self.fleet_speed = 10
        self.fleet_direction = 1  # 1 is right -1 is left
