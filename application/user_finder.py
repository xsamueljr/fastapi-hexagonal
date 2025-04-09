from application.dtos.public_user import PublicUser
from domain.exceptions.user_not_found import UserNotFoundException
from domain.user_repository import UserRepository


class UserFinder:

    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository
    
    def run(self, id: str) -> PublicUser:
        """
        Find user by id, or throws error if not found

        :raises UserNotFoundException: if user was not found
        """
        user = self.__user_repository.get_by_id(id)
        if not user:
            raise UserNotFoundException(id)
        return PublicUser(**user.model_dump())
