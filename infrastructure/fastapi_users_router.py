from fastapi import APIRouter
from infrastructure.users_controller import RegisterResponse, UserController


def create_users_router(controller: UserController) -> APIRouter:
    router = APIRouter(prefix="/users", tags=["users"])

    router.add_api_route("", controller.register,
                     methods=["POST"], status_code=201, response_model=RegisterResponse,
                     responses={
                         201: {
                             "description": "User created successfully"
                         }
                     })
    router.add_api_route("/{id}", controller.find_by_id, methods=["GET"])

    return router
