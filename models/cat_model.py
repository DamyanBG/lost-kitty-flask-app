from db import db

from utils.enums import CatStatus


class CatModel(db.Model):
    __tablename__ = "cats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    microchip = db.Column(db.String(255))
    passport_id = db.Column(db.String(255))
    status = db.Column(db.Enum(CatStatus), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
