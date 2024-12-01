import json
import csv
from datetime import datetime
import random


class Note:
    def __init__(self, title, content):
        self.id = random.randint(1000000000, 9999999999)
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        note = Note(data['title'], data['content'])
        note.id = data['id']
        note.timestamp = data['timestamp']
        return note


class Task:
    def __init__(self, title, description, priority, due_date):
        self.id = random.randint(1000000000, 9999999999)
        self.title = title
        self.description = description
        self.done = False
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['priority'], data['due_date'])
        task.id = data['id']
        task.done = data['done']
        return task


class Contact:
    def __init__(self, name, phone, email):
        self.id = random.randint(1000000000, 9999999999)
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
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

    @staticmethod
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
                save_note_to_json(notes)
                print("Заметка успешно отредактирована!")
            else:
                print("Заметка не найдена.")

        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = load_notes_from_json()
            notes = [n for n in notes if n.id != note_id]
            save_note_to_json(notes)
            print("Заметка успешно удалена!")

        elif choice == '5':
            export_notes_to_csv()

        elif choice == '6':
            import_notes_from_csv()

        elif choice == '7':
            break


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


def manage_tasks():
    while True:
        print("Управление задачами:")
        print("1. Добавить новую задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Экспорт задач в CSV")
        print("7. Импорт задач из CSV")
        print("8. Назад")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            priority = input("Выберите приоритет (Высокий/Средний/Низкий): ")
            due_date = input("Введите срок выполнения (в формате ДД-ММ-ГГГГ): ")
            task = Task(title, description, priority, due_date)
            save_task_to_json(task)
            print("Задача успешно добавлена!")

        elif choice == '2':
            tasks = load_tasks_from_json()
            for task in tasks:
                status = "Выполнена" if task.done else "Не выполнена"
                print(f"{task.id}: {task.title} - {status} (Срок: {task.due_date})")

        elif choice == '3':
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            tasks = load_tasks_from_json()
            task = next((t for t in tasks if t.id == task_id), None)
            if task:
                task.done = True
                save_tasks_to_json(tasks)
                print("Задача отмечена как выполненная!")
            else:
                print("Задача не найдена.")

        elif choice == '4':
            task_id = int(input("Введите ID задачи для редактирования: "))
            tasks = load_tasks_from_json()
            task = next((t for t in tasks if t.id == task_id), None)
            if task:
                task.title = input("Введите новое название задачи: ")
                task.description = input("Введите новое описание задачи: ")
                task.priority = input("Выберите новый приоритет (Высокий/Средний/Низкий): ")
                task.due_date = input("Введите новый срок выполнения (в формате ДД-ММ-ГГГГ): ")
                save_tasks_to_json(tasks)
                print("Задача успешно отредактирована!")
            else:
                print("Задача не найдена.")

        elif choice == '5':
            task_id = int(input("Введите ID задачи для удаления: "))
            tasks = load_tasks_from_json()
            tasks = [t for t in tasks if t.id != task_id]
            save_tasks_to_json(tasks)
            print("Задача успешно удалена!")

        elif choice == '6':
            export_tasks_to_csv()

        elif choice == '7':
            import_tasks_from_csv()

        elif choice == '8':
            break


def save_task_to_json(task):
    tasks = load_tasks_from_json()
    task.id = len(tasks) + 1
    tasks.append(task)
    with open('tasks.json', 'w') as f:
        json.dump([t.to_dict() for t in tasks], f)


def load_tasks_from_json():
    try:
        with open('tasks.json', 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []


def export_tasks_to_csv():
    tasks = load_tasks_from_json()
    with open('tasks_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'Description', 'Done', 'Priority', 'Due Date'])
        for task in tasks:
            writer.writerow([task.id, task.title, task.description, task.done, task.priority, task.due_date])
    print("Задачи успешно экспортированы в CSV.")


def import_tasks_from_csv():
    filename = input("Введите имя CSV-файла для импорта: ")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            task = Task(row['Title'], row['Description'], row['Priority'], row['Due Date'])
            task.done = row['Done'] == 'True'
            save_task_to_json(task)
    print("Задачи успешно импортированы из CSV.")


def manage_contacts():
    while True:
        print("Управление контактами:")
        print("1. Добавить новый контакт")
        print("2. Поиск контакта")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Экспорт контактов в CSV")
        print("6. Импорт контактов из CSV")
        print("7. Назад")
        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите адрес электронной почты: ")
            contact = Contact(name, phone, email)
            save_contact_to_json(contact)
            print("Контакт успешно добавлен!")

        elif choice == '2':
            name = input("Введите имя для поиска: ")
            contacts = load_contacts_from_json()
            found_contacts = [c for c in contacts if name.lower() in c.name.lower()]
            for contact in found_contacts:
                print(f"{contact.id}: {contact.name} - {contact.phone}, {contact.email}")

        elif choice == '3':
            contact_id = int(input("Введите ID контакта для редактирования: "))
            contacts = load_contacts_from_json()
            contact = next((c for c in contacts if c.id == contact_id), None)
            if contact:
                contact.name = input("Введите новое имя: ")
                contact.phone = input("Введите новый номер телефона: ")
                contact.email = input("Введите новый адрес электронной почты: ")
                save_contacts_to_json(contacts)
                print("Контакт успешно отредактирован!")
            else:
                print("Контакт не найден.")

        elif choice == '4':
            contact_id = int(input("Введите ID контакта для удаления: "))
            contacts = load_contacts_from_json()
            contacts = [c for c in contacts if c.id != contact_id]
            save_contacts_to_json(contacts)
            print("Контакт успешно удалён!")

        elif choice == '5':
            export_contacts_to_csv()

        elif choice == '6':
            import_contacts_from_csv()

        elif choice == '7':
            break


def save_contact_to_json(contact):
    contacts = load_contacts_from_json()
    contact.id = len(contacts) + 1
    contacts.append(contact)
    with open('contacts.json', 'w') as f:
        json.dump([c.to_dict() for c in contacts], f)


def load_contacts_from_json():
    try:
        with open('contacts.json', 'r') as f:
            return [Contact.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []


def export_contacts_to_csv():
    contacts = load_contacts_from_json()
    with open('contacts_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'Phone', 'Email'])
        for contact in contacts:
            writer.writerow([contact.id, contact.name, contact.phone, contact.email])
    print("Контакты успешно экспортированы в CSV.")


def import_contacts_from_csv():
    filename = input("Введите имя CSV-файла для импорта: ")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            contact = Contact(row['Name'], row['Phone'], row['Email'])
            save_contact_to_json(contact)
    print("Контакты успешно импортированы из CSV.")


def manage_finances():
    while True:
        print("Управление финансовыми записями:")
        print("1. Добавить новую запись")
        print("2. Просмотреть все записи")
        print("3. Генерация отчёта")
        print("4. Удалить запись")
        print("5. Экспорт финансовых записей в CSV")
        print("6. Импорт финансовых записей из CSV")
        print("7. Назад")
        choice = input("Выберите действие: ")

        if choice == '1':
            amount = float(input("Введите сумму: "))
            category = input("Введите категорию: ")
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            description = input("Введите описание: ")
            record = FinanceRecord(amount, category, date, description)
            save_finance_record_to_json(record)
            print("Финансовая запись успешно добавлена!")

        elif choice == '2':
            records = load_finance_records_from_json()
            for record in records:
                print(f"{record.id}: {record.amount} - {record.category} (Дата: {record.date})")

        elif choice == '3':
            start_date = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
            end_date = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
            generate_financial_report(start_date, end_date)

        elif choice == '4':
            record_id = int(input("Введите ID записи для удаления: "))
            records = load_finance_records_from_json()
            records = [r for r in records if r.id != record_id]
            save_finance_records_to_json(records)
            print("Финансовая запись успешно удалена!")

        elif choice == '5':
            export_finance_records_to_csv()

        elif choice == '6':
            import_finance_records_from_csv()

        elif choice == '7':
            break


def save_finance_record_to_json(record):
    records = load_finance_records_from_json()
    record.id = len(records) + 1
    records.append(record)
    with open('finance.json', 'w') as f:
        json.dump([r.to_dict() for r in records], f)


def load_finance_records_from_json():
    try:
        with open('finance.json', 'r') as f:
            return [FinanceRecord.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []


def generate_financial_report(start_date, end_date):
    records = load_finance_records_from_json()
    filtered_records = [r for r in records if start_date <= r.date <= end_date]
    total_income = sum(r.amount for r in filtered_records if r.amount > 0)
    total_expenses = sum(r.amount for r in filtered_records if r.amount < 0)
    balance = total_income + total_expenses
    report_filename = f'report_{start_date}_{end_date}.csv'
    with open(report_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Общий доход', 'Общие расходы', 'Баланс'])
        writer.writerow([total_income, total_expenses, balance])
    print(f"Финансовый отчёт за период с {start_date} по {end_date} сохранён в {report_filename}.")


def export_finance_records_to_csv():
    records = load_finance_records_from_json()
    with open('finance_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Amount', 'Category', 'Date', 'Description'])
        for record in records:
            writer.writerow([record.id, record.amount, record.category, record.date, record.description])
    print("Финансовые записи успешно экспортированы в CSV.")


def import_finance_records_from_csv():
    filename = input("Введите имя CSV-файла для импорта: ")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = FinanceRecord(float(row['Amount']), row['Category'], row['Date'], row['Description'])
            save_finance_record_to_json(record)
    print("Финансовые записи успешно импортированы из CSV.")


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