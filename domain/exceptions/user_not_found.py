class UserNotFoundException(Exception):
    def __init__(self, id: str) -> None:
        super().__init__(f"There's no user with id {id}")
