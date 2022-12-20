# microbit-bluetooth-uart.py
# Ian Blake
#
# commented Python version of microbit-bluetooth-uart.hex
# file for micro:bit devices for Are You Free?

# start up
busy = 0
call = 0
caller = ""
timer = 0
volume = 0
bluetooth.start_button_service()
bluetooth.start_led_service()
bluetooth.start_uart_service()
basic.show_leds("""
    # . # . #
    # # # # #
    # . # . #
    . . # . .
    . . # . .
""")

# Bluetooth connections
def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# Check volume and report if free/busy
def on_every_interval():
    global volume, timer, busy
    if call == 0:
        volume = input.sound_level()
        if volume >= 32:
            timer += 12
        else:
            timer += -1
        if timer >= 60:
            timer = 60
            busy = 1
        if timer <= 0:
            timer = 0
            busy = 0
        bluetooth.uart_write_value("busy", busy)
loops.every_interval(1000, on_every_interval)

# Check key presses and report if free/busy
def on_button_pressed_a():
    global timer, busy, call
    timer = 0
    busy = 0
    call = 0
    bluetooth.uart_write_value("busy", busy)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global timer, busy, call
    timer = 60
    busy = 1
    call = 0
    bluetooth.uart_write_value("busy", busy)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Check for data received and announce calls
def on_uart_data_received():
    global call, caller
    call = 1
    caller = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    while call == 1:
        basic.show_string(caller)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

