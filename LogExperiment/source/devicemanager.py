import logger
import device

log = logger.DevManagerLog.log


class DeviceManager:
    log.info(' WOW A device manager info Message')
    log.error('WOW DEVICE MANAGER ERROR MESSAGE')

    device_1 = device.Device('Raspberry Pi 5')
    device_2 = device.Device('Arduino 15')


if __name__ == '__main__':
    deviceManager = DeviceManager
