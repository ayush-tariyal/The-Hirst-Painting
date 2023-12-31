import turtle
import random

timmy = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)
timmy.speed("fastest")

timmy.penup()
timmy.hideturtle()
timmy.setposition(-200.00, -200.00)

# colors imported with the help of colorgram
color_list = [
    (235, 243, 238),
    (214, 157, 85),
    (33, 105, 151),
    (238, 215, 94),
    (153, 75, 52),
    (125, 168, 199),
    (209, 134, 163),
    (156, 60, 81),
    (22, 39, 54),
    (212, 85, 61),
    (176, 162, 47),
    (200, 85, 119),
    (135, 184, 150),
    (56, 119, 90),
    (240, 213, 4),
    (25, 46, 37),
    (228, 167, 186),
    (64, 46, 34),
    (87, 157, 100),
    (9, 99, 75),
    (34, 166, 189),
    (40, 60, 102),
    (228, 175, 166),
    (179, 189, 213),
    (95, 126, 173),
    (68, 34, 44),
    (105, 42, 60),
    (170, 205, 179),
    (113, 43, 37),
    (156, 206, 217),
    (78, 69, 35),
    (3, 90, 115),
]


def printing_dots():
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


y = 50

for i in range(10):
    printing_dots()
    timmy.setx(-200.00)
    timmy.sety(-200.00 + y)
    y += 50

my_screen.exitonclick()


# import colorgram

# hirst_colors = colorgram.extract(
#     r"C:\Users\HP\Desktop\Python\The Hirst Painting\img.jpg", 40
# )
# # print(hirst_colors[0].rgb.r)

# color_palette = []

# for color in hirst_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_palette.append(rgb)

# print(color_palette)
