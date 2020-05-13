import os
import tempfile
import pytest
import server
import json
from server import db
from api.model.signboard import Signboard

@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            # server.init_db()
            pass
        yield client

    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])


def test_index(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["message"] == "hello world"

def test_get_signboard(client):
    """ GET signboard/:customer_code/:signboard_code """
    s = Signboard.query.filter_by(signboard_code='board1', customer_code='customer1').first()
    if (s == None):
        s = Signboard(signboard_code='board1', customer_code='customer1', author='me', signboard_status='verified', url='test.fr', deleteed=True)
        db.session.add(s)
        db.session.commit()

    rv = client.get('signboard/customer1/board1')
    assert rv.status == "200 OK"
    json_resp = json.loads(rv.data)
    assert json_resp["message"] == "hello world"
