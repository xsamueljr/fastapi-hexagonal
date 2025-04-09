from typing import TypedDict

from fastapi import HTTPException
from application.dtos.create_user import CreateUserDTO
from application.dtos.public_user import PublicUser
from application.user_creator import UserCreator
from application.user_finder import UserFinder
from domain.exceptions.user_not_found import UserNotFoundException


class RegisterResponse(TypedDict):
    id: str


class UserController:
    def __init__(self, creator: UserCreator, finder: UserFinder) -> None:
        self.__creator = creator
        self.__finder = finder
    
    def register(self, new_user: CreateUserDTO) -> RegisterResponse:
        id = self.__creator.run(new_user)
        return {"id": id}
    
    def find_by_id(self, id: str) -> PublicUser:
        try:
            return self.__finder.run(id)
        except UserNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))