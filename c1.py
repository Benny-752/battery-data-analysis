from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CellData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cell_id = db.Column(db.String(10))
    discharge_capacity = db.Column(db.Float)
    nominal_capacity = db.Column(db.Float)
    current_data = db.Column(db.Float)
    voltage_data = db.Column(db.Float)
    capacity_data = db.Column(db.Float)
    temperature_data = db.Column(db.Float)
    time_data = db.Column(db.Float)
