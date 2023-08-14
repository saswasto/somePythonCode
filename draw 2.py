import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.tracer(10)
tur.width(4)
tur.bgcolor("black")
def square(x):
    for i in range(3):
        tur.forward(x)
        tur.left(90)
    tur.forward(x)
for j in range(20):