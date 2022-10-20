
import pytest
from src import event
from datetime import date
from src import menu

def test_search_and_approve_event(monkeypatch):
    # Setup EVENT
    inputs = iter(["29.09.2022", "Company Party2", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event())
    event1 = event.event_system_3000.search_event(0)

    #Check approval
    inputs = iter(["y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    menu.check_approval(event1)
    assert event1.status == "Approval Given"


def test_create_event(monkeypatch):
    inputs = iter(["29.09.2022", "Company Party", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event1 = event.Event()
    assert event1.active == False
    assert event1.budget.budget == "9000€"
    assert event1.date == "29.09.2022"
    assert event1.expected_attendees == "90"
    assert event1.name == "Company Party"
    assert event1.preferences == "No Preferences"
    assert event1.tasks == []

def test_incremental_id(monkeypatch):
    inputs = iter(["29.09.2022", "Company Party", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event1 = event.Event()
    inputs = iter(["29.09.2022", "Company Party", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event2 = event.Event()
    assert (event1.id + 1) == event2.id