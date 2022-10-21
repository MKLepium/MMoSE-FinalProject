from src import login
import pytest
from src import user_database

def test_login_incorrect_password(monkeypatch):
    inputs = iter(["Johnny", "Hello"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = login.start()
    assert result == "Password not correct"

def test_login_incorrect_username(monkeypatch):
    inputs = iter(["Yoink", "Hello"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = login.start()
    assert result == "Username not found"

def test_login(monkeypatch):
    inputs = iter(["Johnny", "asdf"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = login.start()
    assert result in user_database.users

def test_attempt(monkeypatch):
    inputs = iter(["Johnny", "asde", "Johnny", "asdf"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = login.login()
    assert result in user_database.users