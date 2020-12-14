# -*- coding: utf-8 -*-
"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""

import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json

class GoToCommand:
    def __init__(self, x, y, width=1, color='black'):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
    
    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)
    
    def __str__(self):
        return '{"command": "GoTo", "x": %s, "y": %s, "width": %s, "color": "%s" }' % (str(self.x), str(self.y), str(self.width), str(self.color))
        # return '<Command x="' + str(self.x) + '" y="'+ str(self.y) + '" width="'+str(self.width) + '" color="' + self.color + '"> GoTo</Command>'

class CircleCommand:
    def __init__(self, radius, width=1, color='black'):
        self.radius = radius
        self.width = width
        self.color = color
    
    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)
    
    def __str__(self):
        return '{"command": "Circle", "radius": "%s", "width":"%s", "color":"%s"}' % (str(self.radius), str(self.width), self.color)

class BeginFillCommand:
    def __init__(self, color):
        self.color = color
    
    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return '{"command":"BeginFill", "color": "%s"}' % (self.color)

class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        return '{"command":"EndFill"}'

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return '{"command":"PenUp"}'

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return '{"command":"PenDown"}'

class PyList:
    def __init__(self):
        self.gcList = []

    def append(self, item):
        self.gcList = self.gcList + [item]
    
    def removeLast(self):
        self.gcList = self.gcList[:-1]
    
    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)