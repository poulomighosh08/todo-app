#from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add , show, edit, complete  or exit :")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(f"{todo}\n")

        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for i, todo in enumerate(new_todos):
            row = f"{i+1}-{todo}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter new to do item:")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("This command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todos.pop(number-1)

            functions.write_todos(todos)
        except IndexError:
            print("This item number doesn't exist")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("command not valid")

print("Bye!")