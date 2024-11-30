from domain.user.user_entity import User
from infra.user.in_memory_user_repository import InMemoryUserRepository
from uuid import uuid4

class TestSaveUser:

    # Testar se é possível salvar Usuários no repositório
    def test_can_save_user(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        # salvar usuário 1 no repositório
        repository.save(user1)
        # salvar usuário 2 no repositório
        repository.save(user2)

        # verificar se os usuários estão dentro do repositório e se a lista tem 2 usuários
        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2

class TestGetUserById:

    # Testar se é possível retornar um usuário pelo Id dele
    def test_can_get_user_by_id(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        # retornar o usuário user1 pelo seu id
        user = repository.get_by_id(user1.id)

        # Verifico se eu retorno o mesmo usuário
        assert user.id == user1.id

    # Testar se o método get_by_id retorna um objeto vazio caso não exista o usuário no repositório
    def test_when_user_does_not_exists_should_return_none(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user_id=uuid4())

        assert user is None

class TestUpdateUser:

    # Testa se é possível atualizar um nome de um Usuário
    def test_update_user(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        # Atualizando o nome do Usuário João
        user1.name = "Matheus"

        repository.update(user1)

        updated_user = repository.get_by_id(user_id=user1.id)

        assert updated_user.name == "Matheus"