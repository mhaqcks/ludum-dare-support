import pyglet

def main():
    window = pyglet.window.Window(width=1280, height=720)

    level = StartLevel()

    @window.event
    def on_draw():
        window.clear()
        level.process()

    pyglet.app.run()


if __name__ == '__main__':
    main()

