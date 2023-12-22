from db import db


class CatPhotoModel(db.Model):
    __tablename__ = "cat_photos"

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey("cats.id"))