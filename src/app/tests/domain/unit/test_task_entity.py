from uuid import uuid4
from domain.task.task_entity import Task
import pytest

class TestTask:
    
    # Teste para verificar o construtor da classe Task
    def test_task_initialization(self):
        task_id = uuid4()
        user_id = uuid4()
        title = "Estudar mais sobre testes unitários."
        description = "Os testes unitários são os mais baratos."
        completed = False

        task = Task(id=task_id, user_id= user_id, title=title, description=description, completed=completed)

        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    # Teste para validação para o Id da Task
    def test_task_id_validation(self):
        user_id = uuid4()

        with pytest.raises(Exception, match="id must be an UUID"):
            Task(id=1, user_id=user_id, title="Título tarefa", description="Descrição tarefa", completed=False)

    # Teste para verificar o Id do usuário válido
    def test_task_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user_id must be an UUID"):
            Task(id=task_id, user_id="invalid_user_id", title="Título tarefa", description="Descrição tarefa", completed=False)

    # Teste para verificar a validação do título da Task
    def test_task_title_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(id=task_id, user_id=user_id, title="", description="Descrição tarefa", completed=False)

    # Teste para verificar a validação da descrição da Task
    def test_task_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(id=task_id, user_id=user_id, title="Título tarefa", description="", completed=False)

    # Teste para verificar a validação do Status "Completed" da Task
    def test_task_completed_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="invalid completed status: must be boolean"):
            Task(id=task_id, user_id=user_id, title="Título tarefa", description="Descrição tarefa", completed="not_boolean")

    # Teste para verificar se uma tarefa foi completada com um função mark_as_completed
    def test_mark_as_completed(self):
        # instanciar a minha classe Task
        task = Task(id=uuid4(), user_id=uuid4(), title="Título tarefa", description="Descrição tarefa", completed=False)

        # marcar a tarefa como concluída
        task.mark_as_completed()

        # verificar se o atríbuto foi atualizado para completed
        assert task.completed is True