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
        cat_photos_urls = []
        for photo in base64_photos:
            cat_photos_urls.append(CatPhotoManager.add_cat_photo(photo))
        cat["photos_urls"] = cat_photos_urls
        return cat

    @staticmethod
    def select_all_cats():
        cats = CatModel.query.all()
        return cats
