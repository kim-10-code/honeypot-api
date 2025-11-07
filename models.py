from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Attack(db.Model):
    __tablename__ = 'attacks'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45))
    user_agent = db.Column(db.String(255))
    payload = db.Column(db.Text)
    geolocation = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def convert_to_dict(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'user_agent': self.user_agent,
            'payload': self.payload,
            'geolocation': self.geolocation,
            'timestampt': self.timestamp.isoformat()
        }

