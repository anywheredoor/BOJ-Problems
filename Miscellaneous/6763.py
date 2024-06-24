"""
https://www.acmicpc.net/problem/6763 (Speed fines are not fine!)

Implementation
"""
speed_limit = int(input())
car_speed = int(input())

if car_speed <= speed_limit:
    print("Congratulations, you are within the speed limit!")
elif car_speed > speed_limit:
    difference = car_speed - speed_limit
    if 1 <= difference <= 20:
        print("You are speeding and your fine is $100.")
    elif 21 <= difference <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
