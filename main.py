from guizero import App, Text, PushButton, info
import time

def loading_screen(delays):

    app = App("CoolPyTools Loading")

    text = Text(app, "")
    app.update()

    start_time = time.time()

    while time.time() - start_time < delays[0]:
        for char in ["-", "\\", "|", "/"]:
            text.value = f"Starting... {char}"
            app.update()
            time.sleep(0.1)

    start_time = time.time()


    for tool in ["Text Editor", "Calculator", "Minecraft Pi Mod IDE"]:
        while time.time() - start_time < delays[1]:
            for char in ["-", "\\", "|", "/", "-", "\\", "|", "/", "-"]:
                text.value = f"Loading Tool: {tool} {char}"
                app.update()
                time.sleep(0.1)
        start_time = time.time()


    start_time = time.time()

    while time.time() - start_time < delays[2]:
        for char in ["-", "\\", "|", "/"]:
            text.value = f"Setting Up GUI... {char}"
            app.update()
            time.sleep(0.1)

    app.destroy()

loading_screen([2, 1, 2])

app = App("CoolPyTools Dashboard")

def calculator():
    global app
    import calc
    calc.run(app)

def text_editor():
    global app
    import text_ed
    text_ed.run(app)

def mcpi_mod():
    global app
    import mc_pi_mod
    mc_pi_mod.run(app)

def about():
    global app
    info("ABOUT COOLPYTOOLS", "Creator: Oliver Morandi\nWebsite: hypergamez.my.canva.site/coolpytools\nGUI Library: guizero\nProgramming: Python 3")

def run():

    PushButton(app, text="Calculator", command=calculator)
    PushButton(app, text="Text Editor", command=text_editor)
    PushButton(app, text="Minecraft Pi Mod IDE", command=mcpi_mod)
    PushButton(app, text="Quit", command=app.destroy)
    PushButton(app, text="About CoolPyTools", command=about)


    

    app.display()

run()