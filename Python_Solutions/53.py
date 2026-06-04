from datetime import datetime


class Task:

    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return (
            f"Task: {self.name} | "
            f"Due: {self.due_date.strftime('%Y-%m-%d')} | "
            f"Priority: {self.priority}"
        )


tasks = []

tasks.append(Task("Complete Assignment", "2026-06-10", "High"))
tasks.append(Task("Pay Electricity Bill", "2026-06-02", "Medium"))
tasks.append(Task("Project Submission", "2026-06-15", "High"))
tasks.append(Task("Buy Groceries", "2026-06-05", "Low"))

tasks.sort(key=lambda task: task.due_date)

today = datetime.now()

overdue_tasks = [
    task for task in tasks if task.due_date < today
]

print("----- Task Schedule -----")

for task in tasks:
    print(task)

print("\n----- Overdue Tasks -----")

if overdue_tasks:
    for task in overdue_tasks:
        print(task)
else:
    print("No overdue tasks")