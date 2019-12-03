"""The Anaconda: A Game
=== Module Description ===
This module holds the snake player and manages its movement along with how
it will grow.
"""
import pygame
from typing import Tuple

# BODY_HEAD = pygame.Rect((132, 363, 32, 32))
# BODY_PART = pygame.Rect((100, 363, 32, 32))

class Snake:
    def __init__(self, snake_linked_list, dx=1, dy=0):
        self.snake_linked_list = snake_linked_list
        self.dx = dx  # snake moves right as soon as game starts
        self.dy = dy

        # Load in snake head sprite
        # Load in snake tail sprites
        # self.snake_body = linked_list.LinkedList([BODY_HEAD])
        # (dx > 0) = Moves right (index increases)
        # (dx < 0) = Moves left (index decreases)
        # (dy > 0) = Moves down the canvas (index increases)
        # (dy < 0) = Moves up the canvas (index decreases)

    def get_snake_linked_list(self):
        return self.snake_linked_list

    def move_snake(self, event):
        if event.key == pygame.K_w:
            self.dx, self.dy = 0, -1
        elif event.key == pygame.K_a:
            self.dx, self.dy = -1, 0
        elif event.key == pygame.K_s:
            self.dx, self.dy = 0, 1
        elif event.key == pygame.K_d:
            self.dx, self.dy = 1, 0
        else:
            pass

    def update(self):
        curr = self.snake_linked_list._first
        previous_coordinate = curr.item
        new_coord_x = previous_coordinate[0] + self.dy
        new_coord_y = previous_coordinate[1] + self.dx
        new_coord = (new_coord_x, new_coord_y)
        curr.insert_item(new_coord)
        curr = curr.next
        while curr is not None:
            old_coord = curr.item
            curr.insert_item(previous_coordinate)
            previous_coordinate = old_coord
            curr = curr.next

    def get_snake_direction(self) -> Tuple[int, int]:
        return self.dx, self.dy

    def grow(self) -> None:
        """
        Grows the body of the snake whenever food is encountered
        """
        # self.snake_body.insert(len(self.snake_body), BODY_PART)