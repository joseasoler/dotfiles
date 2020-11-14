import subprocess


class ProcessorData:
    """
    Holds the data required to generate one of the processor's values (utilization or temperature).
    """
    def __init__(self, args, thresholds):
        """
        :param args: Arguments to run the subprocess that returns the value. See the documentation of subprocess.
        :param thresholds: Iterable of tuples containing a threshold and a label. If the value is greater than the
        threshold, this label will be used. If the value is lesser than all thresholds, the last label will be used.
        """
        self.args = args
        self.thresholds = thresholds


def _process_data(data):
    value = float(subprocess.run(data.args, check=False, stdout=subprocess.PIPE).stdout.decode('utf-8'))
    for idx in range(0, len(data.thresholds) - 1):
        if value > data.thresholds[idx][1]:
            return data.thresholds[idx][0], value
    return data.thresholds[-1][0], value


def processor_status(util_data, temp_data):
    """
    Generates a string with the processor's utilization and temperature status, using the provided commands and info.
    :param util_data: ProcessorData to obtain the processor's utilization status.
    :param temp_data: ProcessorData to obtain the processor's temperature status.
    :return: String containing the status.
    """
    util_label, util_value = _process_data(util_data)
    temp_label, temp_value = _process_data(temp_data)
    return '{} {}'.format(util_label, temp_label).format(util_value, temp_value)
