
import pytest

@pytest.fixture(scope="session")
def credential_of_user(request):
    return request.param