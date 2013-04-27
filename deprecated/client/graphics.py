import pyglet
from pyglet import font
import os

active_level = None

textures = {}

def set_level(level):
    global active_level
    active_level = level

def setup():
    font.add_directory('fonts')
    window = pyglet.window.Window(width=1280, height=720)

    @window.event
    def on_draw():
        window.clear()
        if active_level:
            active_level.draw()

def go():
    pyglet.app.run()

def text(t, font_size=36):
    return pyglet.text.Label(t, font_name='Sorts Mill Goudy', font_size=font_size)

def texture(path):
    path = os.path.abspath(path)

    try:
        return textures[path]
    except KeyError:
        textures[path] = pyglet.image.load(path)

        return textures[path]


