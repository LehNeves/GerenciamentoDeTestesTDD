from fastapi.testclient import TestClient
from uuid import UUID
from infra.api.main import app

client = TestClient(app)

# Testar se é possível criar um usuário através da API
def test_can_create_user():
    created_user_response = client.post("/users", json={"name":"Emidio"})

    data = created_user_response.json()

    assert created_user_response.status_code == 200
    assert isinstance(UUID(data["id"]), UUID)
    assert data["name"] == "Emidio"