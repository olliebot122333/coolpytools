from guizero import (
    Window,
    TextBox,
    PushButton,
    Box,
    select_file,
    yesno
)

from pathlib import Path


def run(master):

    win = Window(
        master,
        title="Text Editor",
        width=800,
        height=500
    )

    current_file = None
    changed = False

    # -------------------------
    # Top menu bar
    # -------------------------

    menu_bar = Box(
        win,
        width="fill",
        height=40,
        layout="grid"
    )

    status = TextBox(
        menu_bar,
        text="Ready",
        grid=[4, 0],
        width=40
    )

    # -------------------------
    # Editor
    # -------------------------

    editor = TextBox(
        win,
        width="fill",
        height="fill",
        multiline=True,
        scrollbar=True
    )

    # -------------------------
    # Track changes
    # -------------------------

    def text_changed():
        nonlocal changed
        changed = True
        status.value = "Unsaved changes"

    editor.when_key_pressed = text_changed

    # -------------------------
    # Open
    # -------------------------

    def open_file():

        nonlocal current_file
        nonlocal changed

        path = select_file(
            title="Open File",
            filetypes=[
                ["Text files", "*.txt"],
                ["Python files", "*.py"],
                ["Markdown files", "*.md"],
                ["All files", "*.*"]
            ]
        )

        if path:

            current_file = Path(path)

            editor.value = current_file.read_text()

            changed = False

            status.value = f"Loaded: {current_file.name}"

    # -------------------------
    # Save As
    # -------------------------

    def save_as():

        nonlocal current_file
        nonlocal changed

        path = select_file(
            title="Save File",
            save=True,
            filetypes=[
                ["Text files", "*.txt"],
                ["Python files", "*.py"],
                ["Markdown files", "*.md"],
                ["All files", "*.*"]
            ]
        )

        if path:

            current_file = Path(path)

            current_file.write_text(editor.value)

            changed = False

            status.value = f"Saved: {current_file.name}"

    # -------------------------
    # Save
    # -------------------------

    def save_file():

        nonlocal changed

        if current_file is None:

            save_as()

            return

        current_file.write_text(editor.value)

        changed = False

        status.value = f"Saved: {current_file.name}"

    # -------------------------
    # New File
    # -------------------------

    def new_file():

        nonlocal current_file
        nonlocal changed

        if changed:

            answer = yesno(
                "Unsaved Changes",
                "Save before creating a new file?"
            )

            if answer:

                save_file()

        editor.clear()

        current_file = None

        changed = False

        status.value = "New file"

    # -------------------------
    # Window closing
    # -------------------------

    def close_editor():

        if changed:

            answer = yesno(
                "Unsaved Changes",
                "Save before closing?"
            )

            if answer:

                save_file()

        win.destroy()

    win.when_closed = close_editor

    # -------------------------
    # Buttons
    # -------------------------

    PushButton(
        menu_bar,
        text="Open",
        grid=[0, 0],
        command=open_file
    )

    PushButton(
        menu_bar,
        text="Save",
        grid=[1, 0],
        command=save_file
    )

    PushButton(
        menu_bar,
        text="Save As",
        grid=[2, 0],
        command=save_as
    )

    PushButton(
        menu_bar,
        text="New",
        grid=[3, 0],
        command=new_file
    )


# -------------------------
# Standalone testing
# -------------------------

if __name__ == "__main__":

    from guizero import App

    app = App()

    run(app)

    app.display()