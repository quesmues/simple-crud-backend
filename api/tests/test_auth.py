from api.core.auth import get_hashed_password, verify_password


def test_auth():
    hashed_password = get_hashed_password("teste")
    is_password = verify_password("teste", hashed_password)

    assert isinstance(hashed_password, str)
    assert is_password is True
