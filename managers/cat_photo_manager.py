from db import db
from cloud.nextcloud import upload_base64_image
from models.cat_photo_model import CatPhotoModel


class CatPhotoManager:
    @staticmethod
    def add_cat_photo(base64_photo, cat_id):
        photo_url = upload_base64_image(base64_photo)
        cat_photo_data = {"photo_url": photo_url, "cat_id": cat_id}
        cat_photo = CatPhotoModel(**cat_photo_data)
        db.session.add(cat_photo)
        db.session.commit()
        return photo_url

    @staticmethod
    def select_cat_photos_urls(cat_id):
        cat_photos = CatPhotoModel.query.filter_by(cat_id=cat_id).all()
        cat_photos_urls = [cat_photo.photo_url for cat_photo in cat_photos]
        return cat_photos_urls
    
    @staticmethod
    def delete_cat_photos(cat_id):
        cat_photos = CatPhotoModel.query.filter_by(cat_id=cat_id).all()
        for cat_photo in cat_photos:
            db.session.delete(cat_photo)
        db.session.commit()
