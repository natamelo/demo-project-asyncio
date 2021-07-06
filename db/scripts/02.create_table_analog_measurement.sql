CREATE TABLE IF NOT EXISTS analog_measurement
  (
     id              INTEGER PRIMARY KEY,
     equipment_id    INTEGER NOT NULL,
     generation_time INTEGER NOT NULL,
     measuremet      INTEGER(4) NOT NULL,
     FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id)
  )