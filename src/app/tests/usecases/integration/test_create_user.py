from infra.user.in_memory_user_repository import InMemoryUserRepository
from uuid import UUID
from application.user.create_user_use_case import CreateUserRequest, CreateUserResponse, CreateUserUseCase

class TestCreateUser:

    # Teste para criar um Usuário com dados válidos
    def test_create_user_with_valid_data(self):
        # Repositorio
        repository = InMemoryUserRepository()

        # Caso de uso
        use_case = CreateUserUseCase(repository)

        # Entrada (Requisição)
        request = CreateUserRequest(name="Alexandre")

        # Saida (Resposta)
        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)

        persisted_user = repository.users[0]

        assert persisted_user.id == response.id
        assert persisted_user.name == "Alexandre"