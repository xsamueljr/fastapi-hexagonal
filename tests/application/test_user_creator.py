from typing import cast
import unittest
from unittest.mock import create_autospec, MagicMock

from application.dtos.create_user import CreateUserDTO
from application.user_creator import UserCreator
from domain.user import User
from domain.user_repository import UserRepository


def create_user_dto(name: str = "irrelevant-name") -> CreateUserDTO:
    return CreateUserDTO(name=name)


class TestUserCreator(unittest.TestCase):
    
    def setUp(self) -> None:
        self.repo = cast(MagicMock, create_autospec(UserRepository, spec_set=True))
        self.usecase = UserCreator(self.repo)

    def test_it_calls_save_once(self) -> None:
        self.usecase.run(create_user_dto())
        self.repo.save.assert_called_once()
    
    def test_calls_save_with_right_object(self) -> None:
        user = create_user_dto()
    
        self.usecase.run(user)
        saved: User = self.repo.save.call_args[0][0]

        self.assertEqual(user.name, saved.name)

        # id is generated so we can't check it entirely
        self.assertIsInstance(saved.id, str)
        self.assertGreater(len(saved.id), 6)
