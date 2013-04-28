from pyglet.resource import Loader
from pyglet.sprite import Sprite
import json
import config
import time

PATH = ['comics']
loader = Loader(PATH)


class ComicLevel(object):
    def __init__(self, comic):
        self.comic = comic
        self.sprite = Sprite(loader.image('{0}.png'.format(self.comic)))
        self.width = self.sprite.width
        self.height = self.sprite.height
        panel_file = loader.file('{0}.json'.format(self.comic))
        self.comic_config = json.loads(panel_file.read())
        self.panels = self.comic_config['panels']

        self.begin()

    def begin(self, driver=None):
        self.sprite.x = self.sprite.y = 0
        self.start = time.time()
        self.mode = 'startup'
        self.panel = 0
        self.driver = driver

    def position(self, x, y):
        x = -(x * self.sprite.scale)
        y = (y - self.height) * self.sprite.scale
        return x, y

    def scale(self, width, height):
        return min(float(config.WIDTH)/width, float(config.HEIGHT)/height)

    def startTransition(self, panel=None):
        self.mode = 'transition'
        self.start = time.time()
        if panel is None:
            self.panel += 1
        else:
            self.panel = panel

        if self.panel >= len(self.panels):
            self.panel = len(self.panels) - 1
            self.driver.change_level(self.comic_config['next_scene'])

    def startup(self):
        if time.time() - self.start < config.INIT_PAUSE:
            self.full_scale = self.sprite.scale = self.scale(
                self.width,
                self.height)
        else:
            self.startTransition(0)

    def transition(self):
        if self.panel == 0:
            prev_x, prev_y = 0, 0
            prev_scale = self.full_scale
        else:
            x_buffer = 0
            y_buffer = 0

            prev_scale = self.scale(
                self.panels[self.panel - 1]['width'],
                self.panels[self.panel - 1]['height'])

            x_buffer = config.WIDTH - self.panels[self.panel - 1]['width'] * prev_scale
            y_buffer = config.HEIGHT - self.panels[self.panel - 1]['height'] * prev_scale

            prev_x, prev_y = self.position(
                self.panels[self.panel - 1]['x'],
                self.panels[self.panel - 1]['y'])

            prev_x += x_buffer / 2
            prev_y += y_buffer / 2

        scale = self.scale(
            self.panels[self.panel]['width'],
            self.panels[self.panel]['height'])

        x_buffer = config.WIDTH - self.panels[self.panel]['width'] * scale
        y_buffer = config.HEIGHT - self.panels[self.panel]['height'] * scale

        x, y = self.position(
            self.panels[self.panel]['x'],
            self.panels[self.panel]['y'])

        x += x_buffer / 2
        y += y_buffer / 2

        if time.time() - self.start > config.TRANSITION_TIME:

            self.sprite.scale = self.scale(
                self.panels[self.panel]['width'],
                self.panels[self.panel]['height'])

            x, y = self.position(
                self.panels[self.panel]['x'],
                self.panels[self.panel]['y'])

            x += x_buffer / 2
            y += y_buffer / 2

            prev_x, prev_y = x, y
            prev_scale = scale

            self.mode = 'sleepy_time'
            self.start = time.time()

        self.sprite.x = config.COMIC_EASE(
            time.time() - self.start,
            prev_x, x - prev_x,
            config.TRANSITION_TIME
            )

        self.sprite.y = config.COMIC_EASE(
            time.time() - self.start,
            prev_y, y - prev_y,
            config.TRANSITION_TIME
            )

        self.sprite.scale = config.COMIC_EASE(
            time.time() - self.start,
            prev_scale, scale - prev_scale,
            config.TRANSITION_TIME
            )


    def sleepy_time(self):
        if time.time() - self.start > self.panels[self.panel]['sleep']:
            self.startTransition()

    def process(self):
        if self.mode == 'startup':
            self.startup()
        elif self.mode == 'transition':
            self.transition()
        elif self.mode == 'sleepy_time':
            self.sleepy_time()

        self.sprite.draw()
