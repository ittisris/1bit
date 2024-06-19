def on_microbit_id_io_p8_pin_evt_rise():
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        if pins.digital_read_pin(DigitalPin.P2) == 1:
            writeData()
        sendInstruc()
control.on_event(EventBusSource.MICROBIT_ID_IO_P8,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p8_pin_evt_rise)

def on_microbit_id_io_p8_pin_evt_fall():
    global pc
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        if pins.digital_read_pin(DigitalPin.P2) == 0:
            readData()
        pc = pc + 1
        if pc == len(rom):
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
    instruction = rom[pc]
    pins.digital_write_pin(DigitalPin.P10, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P11, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P12, instruction % 2)
    instruction = Math.round(instruction / 2)
    pins.digital_write_pin(DigitalPin.P13, instruction % 2)
def reset():
    global pc
    pc = 0
    sendInstruc()
    readData()
instruction = 0
pc = 0
output_port: List[number] = []
input_port: List[number] = []
ioaddress: List[number] = []
rom: List[number] = []
rom = [0, 1]
ioaddress = [0, 1]
data_in = pins.digital_read_pin(DigitalPin.P0)
input_port = [0, 0, 0]
output_port = [0, 0, 0]