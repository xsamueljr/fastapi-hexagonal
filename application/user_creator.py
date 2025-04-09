from application.dtos.create_user import CreateUserDTO
from domain.user import User
from domain.user_repository import UserRepository


class UserCreator:

    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository
    
    def run(self, new_user: CreateUserDTO) -> str:
        user = User(**new_user.model_dump())
        self.__user_repository.save(user)
        return user.id
