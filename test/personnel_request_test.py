import re
from src import task
from src import event
import pytest
from src import personnelrequest as pr


def test_insert_financial_request(monkeypatch):
    inputs = iter(["id:0", "9000€", "New Equipment"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pr.system.insert_request(pr.PersonnelRequest())
    assert len(pr.system.requests) == 1

def test_create_financial_request(monkeypatch):
    inputs = iter(["id:0", "9000€", "New Equipment"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    request = pr.PersonnelRequest()
    assert request.jobtitle == "id:0"
    assert request.jobdesc == "9000€"
    assert request.deadline == "New Equipment"