from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()


class Equipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True)
    substation = Column(String)
    code = Column(String)


class Measurement(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    generation_time = Column(Integer)


class AnalogMeasurement(Measurement):
    __tablename__ = "analog_measurement"
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    measurement = Column(Integer)

    def set_equipment_id(self, equipment_id):
        self.equipment_id = equipment_id


class DiscreteMeasurement(Measurement):
    __tablename__ = "discrete_measurement"
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    measurement = Column(Boolean)

    def set_equipment_id(self, equipment_id):
        self.equipment_id = equipment_id


class EquipmentType(Enum):
    POWER_SWITCH = 'POWER_SWITCH'
    POWER_BREAKER = 'POWER_BREAKER'
    POWER_TERMINAL = 'POWER_TERMINAL'

    @staticmethod
    def is_analog_equipment(type):
        return type and type.upper() == EquipmentType.POWER_TERMINAL.value
