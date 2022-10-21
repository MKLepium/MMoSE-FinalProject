from src import task
from src import event
import pytest


def test_create_task(monkeypatch):
    inputs = iter(["Company Party2", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event(task.system))
    event1 = event.event_system_3000.search_event(0)
    
    inputs = iter(["Scrub the Deck", "Scrubbing the deck using a scrubber and some water"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    new_Task = task.Task(event1)
    assert new_Task.status == "open"
    assert new_Task.title == "Scrub the Deck"
    assert new_Task.desc == "Scrubbing the deck using a scrubber and some water"
    assert new_Task.event == event1

def test_closing_task(monkeypatch):
    inputs = iter(["Company Party2", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event(task.system))
    event1 = event.event_system_3000.search_event(0)
    
    inputs = iter(["Scrub the Deck", "Scrubbing the deck using a scrubber and some water"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    new_Task = task.Task(event1)
    inputs = iter(["y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    new_Task.close()
    assert new_Task.status == "done"

def test_task_system_insert_by_event(monkeypatch):
    inputs = iter(["Company Party2", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event(task.system))
    event1 = event.event_system_3000.search_event(0)
    
    inputs = iter(["Scrub the Deck", "Scrubbing the deck using a scrubber and some water"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.system.insert_task(task.Task(event1))
    inputs = iter(["Scrub the Deck2", "Scrubbing the deck using a scrubber and some water2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.system.insert_task(task.Task(event1))

    task_list = task.system.by_event(event1)
    task.system.tasks = [] # Since I don't have a fixture for the teardown,I clear it by hand
    assert len(task_list) == 2
    task1 = task_list[0]
    task2 = task_list[1]
    assert task1.title == "Scrub the Deck"
    assert task1.desc == "Scrubbing the deck using a scrubber and some water"
    assert task2.title == "Scrub the Deck2"
    assert task2.desc == "Scrubbing the deck using a scrubber and some water2"

def test_task_system_insert_by_status(monkeypatch):
    inputs = iter(["Company Party2", "29.09.2022", "90", "No Preferences", "9000€"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event.event_system_3000.insert_event(event.Event(task.system))
    event1 = event.event_system_3000.search_event(0)
    
    inputs = iter(["Scrub the Deck", "Scrubbing the deck using a scrubber and some water"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.system.insert_task(task.Task(event1))
    inputs = iter(["Scrub the Deck2", "Scrubbing the deck using a scrubber and some water2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.system.insert_task(task.Task(event1))

    task_list = task.system.by_status("open")
    print(task_list)
    assert len(task_list) == 2 
    task1 = task_list[0]
    task2 = task_list[1]
    assert task1.title == "Scrub the Deck"
    assert task1.desc == "Scrubbing the deck using a scrubber and some water"
    assert task2.title == "Scrub the Deck2"
    assert task2.desc == "Scrubbing the deck using a scrubber and some water2"
    inputs = iter(["y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.system.tasks[0].close()

    task_list = task.system.by_status("open")
    assert len(task_list) == 1
    task.system.tasks = []