import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w"):
        pass

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=[45,10], enable_events=True)
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="light blue", tooltip="Add Todo", key="Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My to-do app",
                   layout=[[clock],[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    print(event)
    print(values)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                new_todo = values["todo"]
                index = todos.index(values['todos'][0])
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.popup("Please select at least one item", font=("Helvetica", 20))
        case "Complete":
            try:
                todos = functions.get_todos()
                complete_todo = values["todo"]
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['todo'].update(value="")
            except ValueError:
                sg.popup("Please select at least one item", font=("Helvetica", 20))
        case "todos":
            todo_to_edit = values['todos'][0]
            window['todo'].update(value=todo_to_edit)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()


