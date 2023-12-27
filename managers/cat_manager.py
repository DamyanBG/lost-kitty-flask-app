from managers.cat_photo_manager import CatPhotoManager
from managers.user_manager import UserManager
from models.cat_model import CatModel
from db import db
from utils.enums import CatStatus


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
    def select_lost_cats():
        cats = CatModel.query.filter_by(status=CatStatus.lost).all()
        for cat in cats:
            cat.photos_urls = CatPhotoManager.select_cat_photos_urls(cat.id)
        return cats

    @staticmethod
    def select_found_cats():
        cats = CatModel.query.filter_by(status=CatStatus.found).all()
        for cat in cats:
            cat.photos_urls = CatPhotoManager.select_cat_photos_urls(cat.id)
        return cats

    @staticmethod
    def select_cat_details(cat_id):
        cat_details = CatModel.query.filter_by(id=cat_id).first()
        photos_urls = CatPhotoManager.select_cat_photos_urls(cat_details.id)
        cat_details.photos_urls = photos_urls
        return cat_details

    @staticmethod
    def select_by_microchip(microchip):
        cat = CatModel.query.filter_by(microchip=microchip).first()
        if not cat:
            return None
        photos_urls = CatPhotoManager.select_cat_photos_urls(cat.id)
        cat.photos_urls = photos_urls
        contact_person = UserManager.select_by_id(cat.owner_id)
        cat.contact_info = {
            "person": f"{contact_person.first_name} {contact_person.last_name}",
            "email": contact_person.email,
            "phone_number": contact_person.phone_number,
        }
        return cat

    @staticmethod
    def select_by_passport_id(passport_id):
        cat = CatModel.query.filter_by(passport_id=passport_id).first()
        if not cat:
            return None
        photos_urls = CatPhotoManager.select_cat_photos_urls(cat.id)
        cat.photos_urls = photos_urls
        contact_person = UserManager.select_by_id(cat.owner_id)
        cat.contact_info = {
            "person": f"{contact_person.first_name} {contact_person.last_name}",
            "email": contact_person.email,
            "phone_number": contact_person.phone_number,
        }
        return cat
