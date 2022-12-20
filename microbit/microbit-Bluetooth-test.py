def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

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