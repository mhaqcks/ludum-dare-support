from pyglet.resource import Loader
from pyglet.sprite import Sprite

PATH = ['@game.tiles']
loader = Loader(PATH)


class MapLevel(object):
    def __init__(self, level):
        self.level = level
        self.load_tiles
        self.std_sprite_size = 400
        self.begin(level)

    def begin(self, driver=None):
        self.mode = 'startup'
        self.levelTitle = ""
    	self.columns    = 0
        self.rows       = 0
        self.staticData = []
        self.mobileData = []
        self.background = []
        self.foreground = []
        self.tiles      = []
        self.background_batch = pyglet.graphics.Batch()
        self.foreground_batch = pyglet.graphics.Batch()
        self.main_batch       = pyglet.graphics.Batch()
        self.driver = driver

    def process(self):
        if self.mode == 'startup':
            self.startup()
        self.background_batch.draw()
        self.foreground_batch.draw()
        self.main_batch.draw()

    def load_tiles(self):
        tile_files = os.listdir(r'./tiles')
        for i in tile_files:
            lin = ".".join(i.split('.')[:-1]]
            self.tiles[lin] = i)
            #self.tiles.append(pyglet.resource.image(i))

    def gen_sprite(self, sprite_char, x_val, y_val, Batch=None):
        if not (len(self.tiles)):
           #throw an exception
           pass
        new_block = pyglet.sprite.Sprite(img=self.tiles[sprite_char],
                         x=x_val*self.std_sprite_size, y=y_val*self.std_sprite_size,
                         batch=Batch)
        return new_block

    def change_level(self, filename):
        level_label = pyglet.text.Label(text=levelTitle, x=400, y=575,
                                 anchor_x='center', batch=self.main_batch)
        openLevel = open(filename, 'r')
        self.roomTitle = openLevel.readline().strip()
        # get a recording of the depth
        line = openLevel.readline().strip()
        depth       = "Depth: " + line
        depth_label = pyglet.text.Label(text=depth, x=10, y=575,
                                         batch=self.main_batch)

        # read the static tiles:
        if line == "static":
            line = openLevel.readline().strip()
            while line != "mobile":
                self.staticData.append(line)
                line = openLevel.readline().strip()
            # read the 'mobile' tiles
            while line != "":
                self.mobileData.append(line)
                line = openLevel.readline().strip()
        # CLOSE IT UP
        openLevel.close()
        # we have acquired level data, now lets put this to use
        self.columns = len(self.staticData[0])
        self.rows    = len(self.staticData)

        for i in range(0,len(staticData)):
            for j in range(0,len(staticData[i])):
                background.append(gen_sprite(staticData[i][j], i, j,
                                             self.background_batch))

    def startup(self):
        pass

    @game_window.event
    def on_draw():
        game_window.clear()
        background_batch.draw()
        foreground_batch.draw()
        main_batch.draw()
