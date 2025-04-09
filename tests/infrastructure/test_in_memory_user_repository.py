from types import NoneType
import unittest

from domain.user import User
from infrastructure.in_memory_user_repository import InMemoryUserRepository


class TestInMemoryUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryUserRepository()
    
    def test_can_add_user(self) -> None:
        user = User(name="gusy")
        
        self.repository.save(user)
        from_repo = self.repository.get_by_id(user.id)

        self.assertNotIsInstance(from_repo, NoneType,
                                 msg=f"Retrieving user with id {user.id} failed right after saving it")

        self.assertDictEqual(user.model_dump(), from_repo.model_dump()) # type: ignore (`from_repo` will not be none)
    
    def test_works_with_multiple_users(self) -> None:
        names = ["Gusy", "Juan", "Ricardo"]
        users = [User(name=name) for name in names]
        users_from_repo = []

        for user in users:
            self.repository.save(user)
            users_from_repo.append(self.repository.get_by_id(user.id))
        
        self.assertListEqual(users, users_from_repo)
        


if __name__ == '__main__':
    unittest.main()
