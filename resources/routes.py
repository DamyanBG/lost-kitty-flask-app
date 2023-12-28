from resources.auth_resource import LoginUser, RegisterUser
from resources.cat_resource import (
    CatResource,
    LostCatsResource,
    CatDetailsResource,
    FoundCatsResource,
    TotalFoundCats,
    TotalLostCats,
    PaginatedFoundCats,
    PaginatedLostCats,
)
from resources.user_resource import UserResource
from resources.search_resource import MicrochipSearch, PassportIdSearch

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (CatResource, "/cat"),
    (LostCatsResource, "/lost-cats"),
    (PaginatedLostCats, "/lost-cats/<int:offset>/<int:limit>"),
    (FoundCatsResource, "/found-cats"),
    (PaginatedFoundCats, "/found-cats/<int:offset>/<int:limit>"),
    (CatDetailsResource, "/cat/<int:cat_id>"),
    (UserResource, "/user"),
    (MicrochipSearch, "/microchip/<string:microchip>"),
    (PassportIdSearch, "/passport-id/<string:passport_id>"),
    (TotalFoundCats, "/total/found"),
    (TotalLostCats, "/total/lost"),
)
