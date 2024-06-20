def on_microbit_id_io_p8_pin_evt_rise():
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        if pins.digital_read_pin(DigitalPin.P2) == 1:
            writeData()
        sendInstruc()
control.on_event(EventBusSource.MICROBIT_ID_IO_P8,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p8_pin_evt_rise)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_microbit_id_button_b_pin_evt_rise():
    led.plot(0, 0)
    basic.pause(100)
    led.unplot(0, 0)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_button_b_pin_evt_rise)

def on_microbit_id_io_p12_evt():
    rrLoop()
control.on_event(EventBusSource.MICROBIT_ID_IO_P12,
    EventBusValue.MICROBIT_EVT_ANY,
    on_microbit_id_io_p12_evt)

def rrLoop():
    input_port[0] = pins.digital_read_pin(DigitalPin.P12)

def on_microbit_id_io_p8_pin_evt_fall():
    global pc
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        if pins.digital_read_pin(DigitalPin.P2) == 0:
            readData()
        pc = pc + 1
        if pc == len(opcode):
            pc = 0
control.on_event(EventBusSource.MICROBIT_ID_IO_P8,
    EventBusValue.MICROBIT_PIN_EVT_FALL,
    on_microbit_id_io_p8_pin_evt_fall)

def writeData():
    output_port[ioaddress[pc]] = pins.digital_read_pin(DigitalPin.P0)
def readData():
    pins.digital_write_pin(DigitalPin.P0, input_port[ioaddress[pc]])

def on_microbit_id_io_p1_pin_evt_rise():
    reset()
control.on_event(EventBusSource.MICROBIT_ID_IO_P1,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p1_pin_evt_rise)

def sendInstruc():
    global instruction
    instruction = opcode[pc]
    pins.digital_write_pin(DigitalPin.P13, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P14, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P15, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P16, instruction % 2)
def reset():
    global pc
    pc = 0
    sendInstruc()
    rrLoop()
    readData()
instruction = 0
pc = 0
output_port: List[number] = []
input_port: List[number] = []
ioaddress: List[number] = []
opcode: List[number] = []
opcode = [3, 1]
ioaddress = [0, 0]
data_in = pins.digital_read_pin(DigitalPin.P0)
input_port = [0, 0, 0]
output_port = [0, 0, 0]