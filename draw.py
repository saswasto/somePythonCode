from turtle import*
bgcolor("black")
speed(0)
hideturtle()
for i in range(200):
    color("blue")
    circle(i)
    color("red")
    circle(i*0.8)
    right(3)
    forward(3)
done()