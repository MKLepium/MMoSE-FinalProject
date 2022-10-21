import re
from src import task
from src import event
import pytest
from src import financialrequest as fr


def test_insert_financial_request(monkeypatch):
    inputs = iter(["id:0", "9000€", "New Equipment"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    fr.system.insert_request(fr.FinancialRequest())
    assert len(fr.system.requests) == 1

def test_create_financial_request(monkeypatch):
    inputs = iter(["id:0", "9000€", "New Equipment"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    request = fr.FinancialRequest()
    assert request.event == "id:0"
    assert request.money == "9000€"
    assert request.reason == "New Equipment"