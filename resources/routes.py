from resources.auth_resource import LoginUser, RegisterUser
from resources.cat_resource import CatResource, CatsResource, CatDetailsResource

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (CatResource, "/cat"),
    (CatsResource, "/cats"),
    (CatDetailsResource, "/cat/<int:cat_id>"),
)
