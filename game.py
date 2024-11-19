from grid import Grid
from blocks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.level = 1  # New feature: Levels for increased difficulty
        self.lines_cleared_total = 0  # New: Tracks total cleared lines for level progression

    def update_score(self, lines_cleared, move_down_points):
        """Updates score based on lines cleared and soft drops."""
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared >= 4:  # New feature: Bonus for clearing 4 lines
            self.score += 800  # Tetris bonus
        self.score += move_down_points

        # Track total lines cleared for level progression
        self.lines_cleared_total += lines_cleared
        self.update_level()

    def update_level(self):
        """Increase level every 10 lines cleared."""
        new_level = 1 + self.lines_cleared_total // 10
        if new_level > self.level:
            self.level = new_level
            print(f"Level Up! You are now at level {self.level}.")

    def get_random_block(self):
        """Fetches a random block, ensuring no repeats until all are used."""
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        """Moves the current block left, ensuring it remains within bounds."""
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        """Moves the current block right, ensuring it remains within bounds."""
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        """Moves the current block down, locking it if it reaches the bottom."""
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """Locks the block in place and checks for cleared rows."""
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)

        # End game if the new block cannot fit
        if not self.block_fits():
            self.game_over = True
            print("Game Over!")

    def reset(self):
        """Resets the game state to start a new game."""
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.level = 1
        self.lines_cleared_total = 0
        self.game_over = False

    def block_fits(self):
        """Checks if the current block fits within the grid."""
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        """Rotates the current block, ensuring it remains valid."""
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()

    def block_inside(self):
        """Checks if the block is fully within the grid boundaries."""
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        """Draws the grid, current block, and next block on the screen."""
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # Improved next block positioning for better visuals
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
