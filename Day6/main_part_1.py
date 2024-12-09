import numpy as np
import time


def count_visited_spots(guarded_area):
    """Counts the number of visited spots"""
    count = sum(row.count("X") for row in guarded_area)
    print(f"Number of visited spots: {count}")


def print_area(area):
    """Prints out the area grid in a nice way"""
    for row in area:
        print("".join(row))
    print()


def find_player(mapped_area):
    """Find the ^ in the 2D-matrix"""
    for x, row in enumerate(mapped_area):
        for y, element in enumerate(row):
            if element == "^":
                print(f"Player found at: ({x}, {y})")
                return x, y
    raise ValueError("Player '^' not found in the area.")


def move(area, start_x, start_y, direction):
    """Moves the player until an obstacle is encountered or bounds are exceeded"""
    rows = len(area)
    cols = len(area[0])

    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

    while True:
        dx, dy = directions[direction]
        new_x, new_y = start_x + dx, start_y + dy

        # Check if the player leaves the bounds
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            area[start_x][start_y] = "X"
            print("Player has left the bounds.")
            break

        # Get the next tile
        tile = area[new_x][new_y]
        #print(f"Checking tile: {tile} at ({new_x}, {new_y})")

        if tile == "#":
            #print("Found obstacle! Turning 90 degrees.")
            area[start_x][start_y] = "^"
            direction = turn_90_degrees(direction)
        else:
            area[start_x][start_y] = "X"
            start_x, start_y = new_x, new_y

        #print_area(area)

    return area


def turn_90_degrees(current_direction):
    """Turns the player 90 degrees clockwise"""
    order = ["up", "right", "down", "left"]
    new_index = (order.index(current_direction) + 1) % 4
    return order[new_index]


if __name__ == "__main__":
    # Read the input file safely
    with open("./Day6/input.txt", 'r') as file:
        content = file.read()

    list_of_content = content.split('\n')
    area = [list(row) for row in list_of_content]

    try:
        # Find the player's initial position
        x, y = find_player(area)

        # Perform the movement logic
        area = move(area, x, y, direction="up")

        # Print the final area
        print_area(area)

        # Count visited spots
        count_visited_spots(area)


    except Exception as e:
        print(f"Error occurred: {e}")
