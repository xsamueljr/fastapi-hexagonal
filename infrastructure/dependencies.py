from application.user_creator import UserCreator
from application.user_finder import UserFinder
from infrastructure.fastapi_users_router import create_users_router
from infrastructure.in_memory_user_repository import InMemoryUserRepository
from infrastructure.users_controller import UserController


user_repository = InMemoryUserRepository()

user_creator = UserCreator(user_repository)
user_finder = UserFinder(user_repository)

user_controller = UserController(user_creator, user_finder)

users_router = create_users_router(user_controller)