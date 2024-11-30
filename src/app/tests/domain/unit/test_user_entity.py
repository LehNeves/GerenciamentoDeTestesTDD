from uuid import uuid4
import pytest
from domain.user.user_entity import User

class TestUser:

    # Teste para construir o Usuário
    def test_user_initialization(self):
        user_id = uuid4()
        user_name = "Alexandre"

        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name

    # Teste para validação do Id do Usuário
    def test_user_id_validation(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            User(id="id_invalido", name="Gabriel")

    # Teste para validação do nome do Usuário
    def test_user_name_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="name is required"):
            User(id=user_id, name="")
