from resources.auth_resource import LoginUser, RegisterUser
from resources.cat_resource import CatResource, LostCatsResource, CatDetailsResource, FoundCatsResource
from resources.user_resource import UserResource

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (CatResource, "/cat"),
    (LostCatsResource, "/lost-cats"),
    (FoundCatsResource, "/found-cats"),
    (CatDetailsResource, "/cat/<int:cat_id>"),
    (UserResource, "/user"),
)
