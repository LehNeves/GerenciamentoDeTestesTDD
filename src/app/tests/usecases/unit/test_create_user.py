from unittest.mock import MagicMock
from domain.user.user_repository_interface import UserRepositoryInterface
from uuid import UUID
from application.user.create_user_use_case import CreateUserRequest, CreateUserResponse, CreateUserUseCase

class TestCreateUser:

    # Teste para criar um Usuário com dados válidos
    def test_create_user_with_valid_data(self):
        # Repositorio
        mock_repository = MagicMock(UserRepositoryInterface)

        # Caso de uso
        use_case = CreateUserUseCase(mock_repository)

        # Entrada (Requisição)
        request = CreateUserRequest(name="Alexandre")

        # Saida (Resposta)
        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True