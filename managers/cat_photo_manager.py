from db import db
from cloud.nextcloud import upload_base64_image
from models.cat_photo_model import CatPhotoModel


class CatPhotoManager:
    @staticmethod
    def add_cat_photo(base64_photo, cat_id):
        photo_url = upload_base64_image(base64_photo)
        cat_photo = CatPhotoModel(photo_url)
        db.session.add(cat_photo)
        db.session.commit()
        return photo_url
