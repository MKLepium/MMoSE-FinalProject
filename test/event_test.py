
import pytest
from src import event
from datetime import date
from src import menu
from src import task

def test_search_and_approve_event(monkeypatch):
    # Setup EVENT
    inputs = iter(["Company Party2", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event(task.system))
    event1 = event.event_system_3000.search_event(0)

    #Check approval
    inputs = iter(["y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event1.first_approval()
    assert event1.status == "In Financial Review"


def test_create_event(monkeypatch):
    inputs = iter(["Company Party", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event1 = event.Event(task.system)
    assert event1.active == False
    assert event1.budget.budget == "9000€"
    assert event1.date == "29.09.2022"
    assert event1.expected_attendees == "90"
    assert event1.name == "Company Party"
    assert event1.preferences == "No Preferences"
    # assert event1.tasks == []

def test_incremental_id(monkeypatch):
    inputs = iter(["Company Party", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event1 = event.Event(task.system)
    inputs = iter(["Company Party", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event2 = event.Event(task.system)
    assert (event1.id + 1) == event2.id