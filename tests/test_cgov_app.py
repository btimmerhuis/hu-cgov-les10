from project import create_app


def test_index():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Robert Lansing en Bram Timmerhuis" in response.data
