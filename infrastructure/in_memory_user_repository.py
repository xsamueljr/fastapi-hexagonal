from typing import Dict, Optional
from domain.user import User
from domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self) -> None:
        self.__users: Dict[str, User] = {}

    def get_by_id(self, id: str) -> Optional[User]:
        return self.__users.get(id)

    def save(self, user: User) -> None:
        existing_user = self.get_by_id(user.id)
        if existing_user:
            raise Exception(f"There's already a user with id {user.id}")
        
        self.__users[user.id] = user