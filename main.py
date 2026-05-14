def on_gesture_tilt_left():
    moto.move(-1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_a():
    moto.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    moto.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    moto.move(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

carro: game.LedSprite = None
moto: game.LedSprite = None
moto = game.create_sprite(2, 3)

def on_forever():
    global carro
    carro = game.create_sprite(randint(0, 4), 0)
    basic.pause(100)
    carro.turn(Direction.RIGHT, 90)
    for index in range(4):
        carro.move(1)
        basic.pause(200)
    if carro.is_touching_edge():
        carro.delete()
    music.play(music.string_playable("C5 A B G B F A C5 ", 200),
        music.PlaybackMode.IN_BACKGROUND)
basic.forever(on_forever)
