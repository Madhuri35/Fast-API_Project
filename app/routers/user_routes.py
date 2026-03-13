from fastapi APIRouter
from ..Schemas import Users

router=APIRouter()

@router.get("/user")
def get_users():
    return [{"id":1,"name":"john","email":"john@gmail.com"}]


@router.post("/users")
def create_user(user:user):
    return {"message":" created","user":user}
