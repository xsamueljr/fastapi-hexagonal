import unittest
from unittest.mock import create_autospec

from application.user_finder import UserFinder
from domain.exceptions.user_not_found import UserNotFoundException
from domain.user_repository import UserRepository
from domain.user import User


class TestUserFinder(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = create_autospec(UserRepository, spec_set=True)
        self.usecase = UserFinder(self.repo)

    def test_raises_user_not_found(self) -> None:
        self.repo.get_by_id.return_value = None
        
        with self.assertRaises(UserNotFoundException):
            self.usecase.run("irrelevant-id")
    
    def test_returns_expected_user(self) -> None:
        user = User(id="1", name="gusy")
        self.repo.get_by_id.return_value = user

        repo_user = self.usecase.run(user.id)

        self.assertDictEqual(user.model_dump(), repo_user.model_dump())
