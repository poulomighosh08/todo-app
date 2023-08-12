import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=[45,10], enable_events=True)
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            new_todo = values["todo"]
            index = todos.index(values['todos'][0])
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(todos)
        case "Complete":
            todos = functions.get_todos()
            complete_todo = values["todo"]
            todos.remove(complete_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)
            window['todo'].update(value="")
        case "todos":
            todo_to_edit = values['todos'][0]
            window['todo'].update(value=todo_to_edit)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()


