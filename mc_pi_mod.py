import subprocess
from pathlib import Path

from guizero import (
    App,
    Window,
    Box,
    Text,
    ListBox,
    TextBox,
    PushButton
)


DEFAULT_FOLDER = Path(
    "/home/pi/MinecraftPiCode"
)

MINECRAFT_PATH = (
    "/home/pi/.local/bin/"
    "com.thebrokenrail.MCPIReborn.AppImage"
)


def run(master):

    win = Window(
        master,
        title="Minecraft Pi Mod Tool",
        width=1000,
        height=600
    )

    current_file = None

    DEFAULT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    main_box = Box(
        win,
        width="fill",
        height="fill",
        layout="grid"
    )

    # =====================================
    # LEFT SIDE: FILE EXPLORER
    # =====================================

    file_box = Box(
        main_box,
        grid=[0, 0],
        width="fill",
        height="fill"
    )

    Text(
        file_box,
        text="MINECRAFT PI SCRIPTS",
        size=16
    )

    files = ListBox(
        file_box,
        width="fill",
        height="fill"
    )

    # =====================================
    # RIGHT SIDE: CODE EDITOR
    # =====================================

    editor_box = Box(
        main_box,
        grid=[1, 0],
        width="fill",
        height="fill"
    )

    Text(
        editor_box,
        text="CODE EDITOR",
        size=16
    )

    editor = TextBox(
        editor_box,
        width="fill",
        height="fill",
        multiline=True,
        scrollbar=True
    )

    status = Text(
        editor_box,
        text="Ready"
    )

    # =====================================
    # REFRESH FILES
    # =====================================

    def refresh_files():

        files.clear()

        script_count = 0

        for file in sorted(
            DEFAULT_FOLDER.iterdir()
        ):

            if (
                file.is_file()
                and file.suffix == ".py"
            ):

                files.append(
                    file.name
                )

                script_count += 1

        status.value = (
            f"Loaded {script_count} scripts"
        )

    # =====================================
    # LOAD FILE
    # =====================================

    def load_file():

        nonlocal current_file

        selected = files.value

        if selected is None:

            status.value = (
                "Select a file first"
            )

            return

        file_path = (
            DEFAULT_FOLDER / selected
        )

        try:

            editor.value = (
                file_path.read_text()
            )

            current_file = file_path

            status.value = (
                f"Loaded {selected}"
            )

            print(
                "Opened:",
                file_path
            )

        except Exception as error:

            status.value = (
                f"Error loading file: "
                f"{error}"
            )

    # =====================================
    # SAVE FILE
    # =====================================

    def save_file():

        if current_file is None:

            status.value = (
                "Load a file first"
            )

            return

        try:

            current_file.write_text(
                editor.value
            )

            status.value = (
                f"Saved {current_file.name}"
            )

            print(
                "Saved:",
                current_file
            )

        except Exception as error:

            status.value = (
                f"Error saving file: "
                f"{error}"
            )

    # =====================================
    # CREATE NEW MOD
    # =====================================

    def new_mod():

        subwin = Window(
            win,
            title="Create New Mod",
            width=400,
            height=200
        )

        Text(
            subwin,
            text="Enter a name for the new mod:"
        )

        name_box = TextBox(
            subwin,
            width=40
        )

        def create_file():

            name = name_box.value.strip()

            if name == "":

                status.value = (
                    "Enter a file name"
                )

                return

            if not name.endswith(".py"):

                name += ".py"

            new_file = (
                DEFAULT_FOLDER / name
            )

            if new_file.exists():

                status.value = (
                    "That file already exists"
                )

                return

            try:

                new_file.write_text(
                    """# Mod Setup DO NOT REMOVE!
import collections
import collections.abc
collections.Iterable = collections.abc.Iterable

import time

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

player = mc.player

"""
                )

                status.value = (
                    f"Created {name}"
                )

                print(
                    "Created:",
                    new_file
                )

                subwin.destroy()

                refresh_files()

            except Exception as error:

                status.value = (
                    f"Error creating file: "
                    f"{error}"
                )

        PushButton(
            subwin,
            text="Create Mod",
            command=create_file
        )

    # =====================================
    # RUN SCRIPT
    # =====================================

    def run_script():

        if current_file is None:

            status.value = (
                "Load a file first"
            )

            return

        try:

            subprocess.Popen([
                "/usr/bin/python",
                str(current_file)
            ])

            status.value = (
                f"Running {current_file.name}"
            )

            print(
                "Running:",
                current_file
            )

        except Exception as error:

            status.value = (
                f"Error running script: "
                f"{error}"
            )

    # =====================================
    # LAUNCH MINECRAFT
    # =====================================

    def launch_minecraft():

        try:

            subprocess.Popen([
                MINECRAFT_PATH
            ])

            status.value = (
                "Minecraft Pi Edition Reborn launched"
            )

        except Exception as error:

            status.value = (
                f"Error launching Minecraft: "
                f"{error}"
            )

    # =====================================
    # BUTTONS
    # =====================================

    PushButton(
        file_box,
        text="New Mod",
        command=new_mod
    )

    PushButton(
        file_box,
        text="Load Selected File",
        command=load_file
    )

    PushButton(
        file_box,
        text="Save File",
        command=save_file
    )

    PushButton(
        file_box,
        text="Refresh",
        command=refresh_files
    )

    PushButton(
        file_box,
        text="Run Script",
        command=run_script
    )

    PushButton(
        file_box,
        text="Launch Minecraft",
        command=launch_minecraft
    )

    refresh_files()


if __name__ == "__main__":

    app = App(
        title="Minecraft Pi Mod Tool"
    )

    run(app)

    app.display()