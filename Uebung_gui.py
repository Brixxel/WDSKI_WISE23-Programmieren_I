from nicegui import ui

lbl = ui.label('Hello NiceGUI')
ui.button("click me", on_click= lambda btn: lbl.set_text("clicked!"))

ui.run(port = 50886)