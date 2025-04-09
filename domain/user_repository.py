from abc import ABC, abstractmethod
from typing import Optional

from domain.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[User]: pass

    @abstractmethod
    def save(self, user: User) -> None: pass
