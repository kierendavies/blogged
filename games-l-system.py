#!/usr/bin/python

import turtle

# change these two parameters here
iterations = 100
forwarddistance = 1

cur = "xF"
for iteration in range(iterations):
    nxt = ""
    i = 0
    while i < len(cur):
        if i > 0 and cur[i-1] == "x" and cur[i] == "F":
            nxt += "yF+(30)xF"
        elif cur[i] == "+":
            # i know this is not the best way to do this,
            # but i was in a hurry and it works
            i += 2
            num = ""
            while cur[i] != ")":
                num += cur[i]
                i += 1
            num = int(num) - 2
            nxt += "+(" + str(num) + ")"
        elif i > 0 and cur[i-1] == "y" and cur[i] == "F":
            nxt += "FF"
        else:
            nxt += cur[i]
        i += 1
    cur = nxt

turtle.reset()
turtle.speed(0)
turtle.hideturtle()
i = 0
while i < len(cur):
    if cur[i] == "F":
        turtle.forward(forwarddistance)
        pass
    elif cur[i] == "+":
        i += 2
        num = ""
        while cur[i] != ")":
            num += cur[i]
            i += 1
        num = int(num) - 2
        turtle.left(num)
    i += 1
