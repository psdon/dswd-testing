from dswd_blog.app import create_app
import pytest


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app(testing=True)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()