control.onEvent(EventBusSource.MICROBIT_ID_IO_P8, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        if (pins.digitalReadPin(DigitalPin.P2) == 1) {
            writeData()
        }
        sendInstruc()
    }
})
control.onEvent(EventBusSource.MICROBIT_ID_IO_P12, EventBusValue.MICROBIT_EVT_ANY, function () {
    rrLoop()
})
function rrLoop () {
    input_port[0] = pins.digitalReadPin(DigitalPin.P12)
}
control.onEvent(EventBusSource.MICROBIT_ID_IO_P8, EventBusValue.MICROBIT_PIN_EVT_FALL, function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        if (pins.digitalReadPin(DigitalPin.P2) == 0) {
            readData()
        }
        pc = pc + 1
        if (pc == opcode.length) {
            pc = 0
        }
    }
})
function writeData () {
    output_port[ioaddress[pc]] = pins.digitalReadPin(DigitalPin.P0)
}
function readData () {
    pins.digitalWritePin(DigitalPin.P0, input_port[ioaddress[pc]])
}
control.onEvent(EventBusSource.MICROBIT_ID_IO_P1, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    reset()
})
function sendInstruc () {
    instruction = opcode[pc]
    pins.digitalWritePin(DigitalPin.P13, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digitalWritePin(DigitalPin.P14, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digitalWritePin(DigitalPin.P15, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digitalWritePin(DigitalPin.P16, instruction % 2)
}
function reset () {
    pc = 0
    sendInstruc()
    rrLoop()
    readData()
}
let instruction = 0
let pc = 0
let output_port: number[] = []
let input_port: number[] = []
let ioaddress: number[] = []
let opcode: number[] = []
opcode = [3, 1]
ioaddress = [0, 0]
let data_in = pins.digitalReadPin(DigitalPin.P0)
input_port = [0, 0, 0]
output_port = [0, 0, 0]
