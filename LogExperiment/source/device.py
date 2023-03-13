import logger


class Device:
    device_id: str = ''

    def __init__(self, device_id):
        self.device_id = device_id
        devicelogger = logger.create_device_log(device_id=self.device_id)
        devicelogger.info('Hi I am ' + device_id)


if __name__ == '__main__':
    device = Device('Raspberry PI')
