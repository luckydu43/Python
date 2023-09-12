# https://www.codingame.com/ide/puzzle/mars-lander-episode-1
# Success: kudos! Perfect landing. Opportunity reached Mars safe and sound!

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
v_precedente = 0
puissance = 0
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    """
    Si ça accélère on augmente
    Sinon on réduit.
    """
    if abs(v_speed) > abs(v_precedente):
        puissance += 1
    if abs(v_speed) < abs(v_precedente):
        puissance -= 1
    
    """
    Permet de rester dans les plages nominales
    """
    if puissance < 0:
        puissance = 0
    if puissance > 4:
        puissance = 4
    
    """
    Gratté à la main
    """
    if puissance > 3 and abs(v_speed) < 20:
        puissance = 3

    v_precedente = v_speed

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print("0 " + str(puissance))
