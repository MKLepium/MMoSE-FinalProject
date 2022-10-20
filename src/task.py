import itertools

class Task:
    newid = itertools.count()

    def __init__(self, Event):
        self.event = Event
        self.title = input("Task title: ")
        self.desc = input("Task description: ")
        self.status = "open"
        """
        open
        done
        """
        self.id = next(Task.newid)
    def close(self):
        choice = input(f"Do you want to close task {self.title}? [y/n] ")
        if choice == "y":
            self.status = "done"
            print(self)
        else:
            return
    def __repr__(self):
        return "#" + str(self.id) + " | "+ self.title + ": " + self.desc + " - " + self.status
    def __str__(self):
        return "#" + str(self.id) + " | "+ self.title + ": " + self.desc + " - " + self.status

class TaskSystem:
    def __init__(self):
        print("Initiating the Task System")
        self.tasks = []
    def search_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
            else: 
                continue
        return None
    def insert_task(self, task):
        self.tasks.append(task)
    def by_status(self, status):
        return list(filter( lambda x: x.status == status, self.tasks))
    def by_event(self, event):
        return list(filter( lambda x: x.event.id == event.id, self.tasks))
    def print_all(self):
        if self.tasks == []:
            print("No Tasks available")
        else:
            print("==========================")
            for task in self.tasks:
                print("- " + str(task))
            print("==========================")

system = TaskSystem()