from app import app

def test_add_expense():
    tester = app.test_client()
    response = tester.post("/add", json={"amount": 25, "category": "food"})
    assert response.status_code == 201

def test_summary():
    tester = app.test_client()
    response = tester.get("/summary")
    assert response.status_code == 200

def test_health():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200
