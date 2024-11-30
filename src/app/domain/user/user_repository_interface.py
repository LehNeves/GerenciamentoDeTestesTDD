from abc import ABC, abstractmethod
from domain.user.user_entity import User
from uuid import UUID

# classe abstrata para setar quais métodos o meu repositório deve implementar
class UserRepositoryInterface(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> None:
        raise NotImplementedError