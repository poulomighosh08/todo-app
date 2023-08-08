import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=[45,10], enable_events=True)
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            new_todo = value["todo"] + '\n'
            index = todos.index(value['todos'][0])
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(todos)
        case "todos":
           todo_to_edit = value['todos'][0]
           window['todo'].update(values=todo_to_edit)

        case sg.WIN_CLOSED:
            break
window.close()


