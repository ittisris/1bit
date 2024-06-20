input.onButtonPressed(Button.A, function () {
    reset()
})
function clkPosEdge () {
    if (pins.digitalReadPin(DigitalPin.P2) == 1) {
        writeData()
    }
    pins.digitalWritePin(DigitalPin.P1, 1)
    pc = pc + 1
    if (pc == opcode.length) {
        pc = 0
    }
    basic.pause(500)
}
function clkNegEdge () {
    sendInstruc()
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(500)
}
function writeData () {
    output_port[ioaddress[pc]] = pins.digitalReadPin(DigitalPin.P0)
}
function readData () {
    if (pc == 0) {
        input_port[0] = pins.digitalReadPin(DigitalPin.P12)
    }
    pins.digitalWritePin(DigitalPin.P0, input_port[ioaddress[pc]])
}
input.onButtonPressed(Button.B, function () {
    clkNegEdge()
    clkPosEdge()
})
function sendInstruc () {
    instruction = opcode[pc]
    basic.showNumber(instruction)
    pins.digitalWritePin(DigitalPin.P13, instruction % 2)
    instruction = Math.floor(instruction / 2)
    pins.digitalWritePin(DigitalPin.P14, instruction % 2)
    instruction = Math.floor(instruction / 2)
    pins.digitalWritePin(DigitalPin.P15, instruction % 2)
    instruction = Math.floor(instruction / 2)
    pins.digitalWritePin(DigitalPin.P16, instruction % 2)
    readData()
}
function reset () {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pc = 0
    basic.showString("R")
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P8, 0)
}
let instruction = 0
let pc = 0
let output_port: number[] = []
let input_port: number[] = []
let ioaddress: number[] = []
let opcode: number[] = []
led.setBrightness(50)
opcode = [
6,
15,
0,
15,
0
]
ioaddress = [
0,
1,
0,
1,
0
]
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
pins.setPull(DigitalPin.P8, PinPullMode.PullDown)
let tmp = pins.digitalReadPin(DigitalPin.P0)
input_port = [0, 0, 0]
output_port = [0, 0, 0]
reset()
basic.forever(function () {
    basic.pause(100)
})
