#! /usr/bin/python3

# cricket balls to over

# write a funtion to convert no of balls to overs

ball = int(input("enter ball count: "))
over = ball // 6
over_balls = ball % 6
if over_balls:
    print(f'{over}.{over_balls}')
else:
    print(over)
