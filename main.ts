input.onGesture(Gesture.TiltLeft, function () {
    moto.move(-1)
})
input.onButtonPressed(Button.A, function () {
    moto.move(-1)
})
input.onButtonPressed(Button.B, function () {
    moto.move(1)
})
input.onGesture(Gesture.TiltRight, function () {
    moto.move(1)
})
let carro: game.LedSprite = null
let moto: game.LedSprite = null
moto = game.createSprite(2, 3)
basic.forever(function () {
    carro = game.createSprite(randint(0, 4), 0)
    basic.pause(100)
    carro.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        carro.move(1)
        basic.pause(100)
    }
    if (carro.isTouchingEdge()) {
        carro.delete()
    }
    music.play(music.stringPlayable("C5 A B G B F A C5 ", 200), music.PlaybackMode.InBackground)
})
