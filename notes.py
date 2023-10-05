import os
import json
import datetime
print(os.getcwd())
notes = []

def add_note():
  title = input("Введите заголовок заметки: ")
  body = input("Введите тело заметки: ")

  note = {
    "id": len(notes) + 1, 
    "title": title,
    "body": body,
    "created": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  }

  notes.append(note)
  print("Заметка добавлена")

def edit_note():
  id = int(input("Введите ID заметки для редактирования: "))
  
  note = next((note for note in notes if note['id'] == id), None)
  if note:
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новое тело заметки: ")

    note['title'] = title
    note['body'] = body

    print("Заметка обновлена")
  else:
    print("Заметка с таким ID не найдена")

def delete_note():
  id = int(input("Введите ID заметки для удаления: "))

  note = next((note for note in notes if note['id'] == id), None)
  if note:
    notes.remove(note)
    print("Заметка удалена")
  else:
    print("Заметка с таким ID не найдена")

def show_notes(date=None):
  if date:
    filtered_notes = [note for note in notes if note["created"].startswith(date)]
  else:
    filtered_notes = notes

  for note in filtered_notes:
    print(f"ID: {note['id']}")
    print(f"Заголовок: {note['title']}") 
    print(f"Тело: {note['body']}")
    print(f"Дата создания: {note['created']}")
    print("-"*40)

def save_notes():
    with open("notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
     
def load_notes():
    global notes
    if os.path.exists("notes.json"):  
        with open("notes.json", encoding="utf-8") as f:
            notes_str = f.read()
            if notes_str:
                notes_list = notes_str.split("\n")
    
                for note_str in notes_list:
                    if note_str:
                        try:
                            note = json.loads(note_str)
                            notes.append(note)
                        except json.JSONDecodeError:
                            print(f"Ошибка при загрузке заметки: {note_str}")

def main():

  while True:
    command = input("Введите команду (add, edit, delete, show, save, exit): ")

    if command == "add":
      add_note()
    elif command == "edit":
      edit_note()
    elif command == "delete":
      delete_note()
    elif command == "show":
      date = input("Введите дату для фильтрации в формате дд-мм-гггг (Нажмите Enter для показа всех): ")
      show_notes(date)
    elif command == "save":
      save_notes() 
    elif command == "exit":
      save_notes()
      break
    else:
      print("Неизвестная команда")

if __name__ == "__main__":
  load_notes()
  main()