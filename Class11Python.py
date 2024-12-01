import json, csv, random
from datetime import datetime

def manage_notes():
    while True:
        print("Управление заметками:")
        print("1. Добавить новую заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Экспорт заметок в CSV")
        print("6. Импорт заметок из CSV")
        print("7. Назад")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            note = Note(title, content)
            save_note_to_json(note)
            print("Заметка успешно добавлена!")

        elif choice == '2':
            notes = load_notes_from_json()
            for note in notes:
                print(f"{note.id}: {note.title} - {note.timestamp}")

        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            notes = load_notes_from_json()
            note = next((n for n in notes if n.id == note_id), None)
            if note:
                note.title = input("Введите новый заголовок: ")
                note.content = input("Введите новое содержимое: ")
                save_notes_to_json(notes)
                print("Заметка успешно отредактирована!")
            else:
                print("Заметка не найдена.")

        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = load_notes_from_json()
            notes = [n for n in notes if n.id != note_id]
            save_notes_to_json(notes)
            print("Заметка успешно удалена!")

        elif choice == '5':
            export_notes_to_csv()

        elif choice == '6':
            import_notes_from_csv()

        elif choice == '7':
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


def save_note_to_json(note):
    notes = load_notes_from_json()
    note.id = len(notes) + 1
    notes.append(note)
    with open('notes.json', 'w') as f:
        json.dump([n.to_dict() for n in notes], f)

def load_notes_from_json():
    try:
        with open('notes.json', 'r') as f:
            return [Note.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def export_notes_to_csv():
    notes = load_notes_from_json()
    with open('notes_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'Content', 'Timestamp'])
        for note in notes:
            writer.writerow([note.id, note.title, note.content, note.timestamp])
    print("Заметки успешно экспортированы в CSV.")

def import_notes_from_csv():
    filename = input("Введите имя CSV-файла для импорта: ")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            note = Note(row['Title'], row['Content'])
            note.timestamp = row['Timestamp']
            save_note_to_json(note)
    print("Заметки успешно импортированы из CSV.")

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


def main_menu():
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Управление финансовыми записями")
    print("5. Калькулятор")
    print("6. Выход")

    choice = input("Введите номер действия: ")
    return choice


def calculator():
    while True:
        expression = input("Введите выражение для вычисления (или 'выход' для завершения): ")
        if expression.lower() == 'выход':
            break
        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


def main():
    while True:
        choice = main_menu()
        if choice == '1':
            manage_notes()
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            manage_contacts()
        elif choice == '4':
            manage_finances()
        elif choice == '5':
            calculator()
        elif choice == '6':
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()