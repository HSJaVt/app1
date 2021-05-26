def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_uart_data_received():
    pass
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

basic.show_icon(IconNames.HEART)
def on_button_pressed_a():
    global 溫度, 整數, 小數
    溫度 = KSRobot_MLX90614.read_temperature(KSRobot_MLX90614.Temperature_State.OBJECT_TEMP_C)
input.on_button_pressed(Button.A, on_button_pressed_a)

小數 = 0
整數 = 0
溫度 = 0
溫度 = 0

def on_forever():
    global 溫度
    if 溫度 >= 30:
        溫度 = 0
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
basic.forever(on_forever)
