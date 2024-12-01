import json, csv, random
from datetime import datetime

def manage_notes():
    while True:
        print("""
Добро пожаловать в Персональный помощник!
Выберите действие:
1. Управление заметками
2. Управление задачами
3. Управление контактами
4. Управление финансовыми записями
5. Калькулятор
6. Выход
        """)
        choice = input("Выберете действие: ")

        if choice = '1':
            ...
        elif choice = '2':
            ...
        elif choice = '3':
            ...
        elif choice = '4':
            ...
        elif choice = '5':
            ...
        elif choice = '6':
            ...
        elif choice = '7':
            break

class Note:
    def __int__(self, title, content):
        self.id = random.randint(1000000000, 9999999999)
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    def from_dict(data):
        note = Note(data['title'], data['content'])
        note.id = data['id']
        note.timestamp = data['timestamp']
        return note

class Task:
    def __int__(self, title, description, priority, due_date):
        self.id = random.randint(1000000000, 9999999999)
        self.title = title
        self.description = description
        self.done = False
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date
        }

    def from_dict(data):
        task = Task(data['title'], data['description'], data['priority'], data['due_date'])
        task.id = data['id']
        task.done = data['done']
        return task

class Contact:
    def __int__(self, name, phone, email):
        self.id = random.randint(1000000000, 9999999999)
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date
        }

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def from_dict(data):
        contact = Contact(data['name'], data['phone'], data['email'])
        contact.id = data['id']
        return contact

class FinanceRecord:
    def __init__(self, amount, category, date, description):
        self.id = random.randint(1000000000, 9999999999)
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    def from_dict(data):
        record = FinanceRecord(data['amount'], data['category'], data['date'], data['description'])
        record.id = data['id']
        return record
