from resources.auth_resource import LoginUser, RegisterUser
from resources.cat_resource import (
    CatResource,
    LostCatsResource,
    CatDetailsResource,
    FoundCatsResource,
)
from resources.user_resource import UserResource
from resources.search_resource import MicrochipSearch, PassportIdSearch

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (CatResource, "/cat"),
    (LostCatsResource, "/lost-cats"),
    (FoundCatsResource, "/found-cats"),
    (CatDetailsResource, "/cat/<int:cat_id>"),
    (UserResource, "/user"),
    (MicrochipSearch, "/microchip/<string:microchip>"),
    (PassportIdSearch, "/passport-id/<string:passport_id>"),
)
