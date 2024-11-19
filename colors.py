# Defined colors to be used in grid.py, main.py, and game.py for a more appealing game
class Colors:
    # Core colors (original)
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)

    # New colors (enhancements)
    pink = (255, 105, 180)
    gold = (255, 215, 0)
    teal = (0, 128, 128)
    light_green = (144, 238, 144)
    light_blue = (173, 216, 230)
    magenta = (255, 0, 255)

    # Define method to get a list of colors for blocks
    @classmethod
    def get_cell_colors(cls):
        """
        Returns a list of colors to use for game blocks.
        The order ensures backward compatibility while adding new options.
        """
        return [
            cls.dark_grey, cls.green, cls.red, cls.orange, 
            cls.yellow, cls.purple, cls.cyan, cls.blue, 
            cls.pink, cls.gold, cls.teal, cls.light_green, 
            cls.light_blue, cls.magenta
        ]
