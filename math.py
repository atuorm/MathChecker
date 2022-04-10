import statistics
from lib import cmath

menu = input(
    """Please choose your operation:\n
Press (1) for Mean Mode Range & Median
Press (2) to Exit
Press (3) for Test
"""
    )
if menu == '1':
    print("Opening Mean Mode Range & Median")
    cmath.cmath()
if menu == '2':
    quit()
if menu == '3':
    print("Hip hip hooray")
    quit()