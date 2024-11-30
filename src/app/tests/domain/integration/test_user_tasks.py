from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4

class TestUserWithTasks:

    # Teste para adicionar Tasks ao Usuário
    def test_collect_tasks(self):
        user = User(id=uuid4(), name="Willian Salvador da Pátria")
        task1 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes de integração", description="Descrição 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes unitários", description="Descrição 2", completed=True)

        user.collect_tasks([task1, task2])

        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks

    # Teste para contabilizar Tasks pendentes de um Usuário
    def teste_count_pending_tasks(self):
        user = User(id=uuid4(), name="Willian Salvador da Pátria")
        task1 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes de integração", description="Descrição 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes unitários", description="Descrição 2", completed=False)
        task3 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes e2e", description="Descrição 3", completed=False)

        task1.mark_as_completed()

        user.collect_tasks([task1, task2, task3])

        pending_count = user.count_pending_tests()

        assert pending_count == 2

    # Teste a quantidade de tarefas pendentes quando o Usuário é criado.
    def test_count_pending_taks_empty(self):
        user = User(id=uuid4(), name="Alexandre")
        count_pending_tasks = user.count_pending_tests()
        assert count_pending_tasks == 0

    # Teste quando todas as minhas tarefas estão completadas
    def test_all_tasks_completed(self):
        user = User(id=uuid4(), name="Willian Salvador da Pátria")

        # Criando duas tarefas
        task1 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes de integração", description="Descrição 1", completed=False)
        task2 = Task(id=uuid4(), user_id=user.id, title="Estudar sobre testes unitários", description="Descrição 2", completed=False)

        # setando as tasks para o usuário
        user.collect_tasks([task1, task2])

        # marcando como completed
        user.tasks[0].mark_as_completed()
        user.tasks[1].mark_as_completed()

        # pegando o número de tarefas pendentes
        pending_count = user.count_pending_tests()

        # validando se a quantidade de tarefas pendentes é 0
        assert pending_count == 0