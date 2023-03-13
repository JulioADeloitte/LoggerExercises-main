import logging


class Logger:
    # LOAD GLOBAL CONFIGURATION FILE
    # CHECK IF CONFIG FOR LOGGER EXISTS IF NOT SET A DEFAULT ONE AND WRITE TO THE CONFIG FILE
    # IF A LOGGER CONFIG IS DEFINED, THEN LOAD IT.

    # Creating the Master log object
    log = logging.getLogger('master_log')
    log.setLevel(logging.DEBUG)

    # Create and configure the master File log handler:
    master_handler = logging.FileHandler('..//logs/MasterLog.log', mode='w')
    master_handler.setLevel(logging.DEBUG)

    # Create the Formatter for the Console Log
    console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname) -8s - %(message)s')

    # Create and configure the master Console log handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_format)

    # Add both handlers to master logger
    log.addHandler(console_handler)
    log.addHandler(master_handler)

    log.debug('Basically any info')
    log.info('Some process info')
    log.warning('A warning message')
    log.error('An Error MESSAGE')
    log.critical('CRITICAL MESSAGE')

#Device Manager Logger
class DevManagerLog:
    log = logging.getLogger('master_log.' + 'DeviceManager')
    log.setLevel(logging.WARNING)
    log_handler = logging.FileHandler('..//logs/DeviceManager.log')
    log.addHandler(log_handler)

#PYTEST LOGGER j
class TestsLogger:
    log = logging.getLogger('Tests')
    log.setLevel(logging.DEBUG)
    log_handler = logging.FileHandler('..//logs/TestsLogger.log')
    test_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname) -8s - %(message)s')
    log_handler.setFormatter(test_format)
    log.addHandler(log_handler)

#Device Logger
def create_device_log(device_id):
    log = logging.getLogger('master_log.' + device_id)
    log.setLevel(logging.DEBUG)
    log_handler = logging.FileHandler('..//logs/device-' + device_id + '.log')
    log.addHandler(log_handler)
    return log


def move_test_report_logs():
    pass


def move_logs():
    pass

class TestReport():
    """
    Replicar lo de estos comandos en los formatos que se pidan

    python -m pytest TestingSeq.py --html=report.html
    python -m pytest TestingSeq.py -q --excelreport=report.xls
    python -m pytest TestingSeq.py --junitxml=result.xml

    para hacer formatos de los resultados de tests
    """
    pass