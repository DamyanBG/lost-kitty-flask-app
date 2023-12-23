from managers.cat_photo_manager import CatPhotoManager
from models.cat_model import CatModel
from db import db


class CatManager:
    @staticmethod
    def add_cat(cat_data):
        base64_photos = cat_data.pop("photos")
        cat = CatModel(**cat_data)
        db.session.add(cat)
        db.session.commit()
        for photo in base64_photos:
            CatPhotoManager.add_cat_photo(photo, cat.id)
        return cat

    @staticmethod
    def select_all_cats():
        cats = CatModel.query.all()
        for cat in cats:
            cat.photos_urls = CatPhotoManager.select_cat_photos_urls(cat.id)
        return cats
    
    @staticmethod
    def select_cat_details(cat_id):
        cat_details = CatModel.query.filter_by(id=cat_id).first()
        photos_urls = CatPhotoManager.select_cat_photos_urls(cat_details.id)
        cat_details.photos_urls = photos_urls
        return cat_details
