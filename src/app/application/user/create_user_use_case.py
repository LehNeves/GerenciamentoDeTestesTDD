from domain.user.user_repository_interface import UserRepositoryInterface
from dataclasses import dataclass
from uuid import UUID, uuid4
from domain.user.user_entity import User

# Entrada -> DTO
@dataclass
class CreateUserRequest:
    name: str

# Saida -> DTO
@dataclass
class CreateUserResponse:
    id: UUID
    name: str

class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    # Tem o objetivo de executar o caso de uso
    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        # Criando o objeto Usuário
        user = User(id=uuid4(), name=request.name)

        # Salvando Usuário no repositório
        self.repository.save(user)

        # Retornando o novo usuário salvo
        return CreateUserResponse(id=user.id, name=user.name)