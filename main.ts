bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Hash), function () {
    溫度 = KSRobot_MLX90614.read_temperature(KSRobot_MLX90614.Temperature_State.ObjectTempC)
})
let 溫度 = 0
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (溫度 >= 30) {
        溫度 = 0
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
    }
})
