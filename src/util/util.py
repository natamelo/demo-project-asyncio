from src.model.models import Equipment, AnalogMeasurement, DiscreteMeasurement, EquipmentType
from time import time
import os


class DataUtil:

    @staticmethod
    def _extract_substation_and_code(value):
        if value and '.' in value:
            values = value.split('.')
            return (values[0], values[1])
        return (None, None)

    @staticmethod
    def _build_equipment(values):
        path = values[1]
        substation, code = DataUtil._extract_substation_and_code(path)
        equipment = Equipment(substation=substation, code=code)
        return equipment

    @staticmethod
    def _build_measurement(values):
        type = values[0]
        measurement = values[2]
        generation_time = int(time() * 1000)

        if EquipmentType.is_analog_equipment(type):
            equipment = AnalogMeasurement(measurement=measurement, generation_time=generation_time)
        else:
            equipment = DiscreteMeasurement(measurement=bool(measurement), generation_time=generation_time)
        return equipment

    @staticmethod
    def get_objects(line):
        values = line.replace('\n', '').split(',')
        equipment = DataUtil._build_equipment(values)
        measurement = DataUtil._build_measurement(values)
        return (equipment, measurement)

    @staticmethod
    def is_header(line):
        return line and line.startswith('object_type')


class PathUtil:

    @staticmethod
    def get_files_from_dir(path):
        files = os.listdir(path)
        paths = [os.path.join(path, file) for file in files]
        return paths
