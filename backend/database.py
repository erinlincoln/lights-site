from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta




# Create the database tables
db = SQLAlchemy()
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direction = db.Column(db.String(3), nullable=False)
    device_ip = db.Column(db.String(20), nullable=False)
    device_name = db.Column(db.String(50), nullable=True)
    message = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'direction': self.direction,
            'device_ip': self.device_ip,
            'device_name': self.device_name,
            'message': self.message,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

# A device
class Device(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    ip = db.Column(db.String(20), nullable=True)
    last_communication = db.Column(db.DateTime, default=datetime(year=1970, month=1, day=1))

    def to_dict(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'last_communication': self.last_communication
        }

class Devices:

    def __init__(self):
        pass

    def get_device_by_ip(ip : str) -> Device | None:
        return Device.query.filter_by(ip=ip).first()
    
    def get_devices():
        return Device.query.all()
        
    def add_device(id, ip) -> Device:
        new_device = Device(id=id, ip=ip)
        db.session.add(new_device)
        db.session.commit()
        return new_device

    def update_device_ip(id, ip) -> Device:
        device = Device.query.get(id)
        if device is None:
            return None
        device.ip = ip
        db.session.commit()
        return device

    def update_communicated(ip):
        device = Devices.get_device_by_ip()
        if device:
            device.last_communication = datetime.now()
            db.session.commit()
            return device
        return None

event_id_counter = 0
class EventHistory:

    def get_new_id() -> int:
        global event_id_counter
        event_id_counter = event_id_counter + 1
        return event_id_counter

    def log_inbound_event(ip, message) -> Event:
        return EventHistory.log_event(ip, message, "IN")
    
    def log_outbound_event(ip, message) -> Event:
        return EventHistory.log_event(ip, message, "OUT")

    def log_event(ip, message, direction) -> None:
        new_id = EventHistory.get_new_id()
        device_name = Devices.get_device_by_ip(ip)
        new_event = Event(id=new_id, direction=direction, device_ip=ip, device_name=device_name, message=message)
        db.session.add(new_event)
        db.session.commit()
        return new_event

    def get_events_by_time(earliest=datetime.now() - timedelta(days=1), latest=datetime.now()):
        events = Event.query.filter(Event.timestamp >= earliest).filter(Event.timestamp <= latest).all()
        return events
    
    def clear():
        count = db.session.query(Event).delete()
        db.session.commit()
        return count
