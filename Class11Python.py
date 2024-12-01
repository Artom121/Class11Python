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

