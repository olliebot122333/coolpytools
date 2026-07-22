# 🛠️ CoolPyTools

A collection of Python tools made for Raspberry Pi.

CoolPyTools is a growing software suite created by **Oliver Morandi**. It currently includes useful tools such as a calculator, text editor, and a Minecraft Pi modding IDE.

## ✨ Features

### 🧮 Calculator

A simple calculator with support for:

* Addition
* Subtraction
* Multiplication
* Division
* Decimal numbers
* Clear button

### 📝 Text Editor

A basic text editor with:

* Opening files
* Saving files
* Choosing custom file paths
* `~` home-directory support
* A status display
* Resizable editor area

### 🧱 Minecraft Pi Mod IDE

An IDE for creating Python scripts for **Minecraft: Pi Edition: Reborn**.

Features include:

* Creating new mod files
* Built-in Minecraft Pi setup code
* Opening existing scripts
* Editing Python code
* Saving mod files
* Launching Minecraft Pi
* Running scripts with Minecraft

## 🖥️ Dashboard

CoolPyTools includes a central dashboard that lets you launch each tool from one application.

```text
CoolPyTools
├── Calculator
├── Text Editor
├── Minecraft Pi Mod IDE
├── About CoolPyTools
└── Quit
```

The application also includes a startup loading screen to give CoolPyTools its own application-style startup experience.

## 🐍 Built With

* **Python 3**
* **guizero**
* **Tkinter**
* **Git**
* **GitHub Pages**

## 🖥️ Designed For

CoolPyTools is primarily designed for:

* Raspberry Pi computers
* Raspberry Pi OS
* Python developers
* Minecraft Pi modders
* People learning programming

## 📂 Project Structure

```text
coolpytools/
├── main.py
├── calc.py
├── text_ed.py
├── mc_pi_mod.py
├── index.html
├── .gitignore
└── README.md
```

## 🚀 Running CoolPyTools

Clone the repository:

```bash
git clone https://github.com/olliebot122333/coolpytools.git
```

Enter the project directory:

```bash
cd coolpytools
```

Run CoolPyTools:

```bash
python3 main.py
```

## 🧱 Minecraft Pi Modding

The Minecraft Pi Mod IDE creates Python files with the required Minecraft Pi connection setup.

New mod files are automatically created with code similar to:

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

player = mc.player
```

This allows you to start writing Minecraft Pi scripts immediately.

## 🌐 Website

Visit the CoolPyTools website:

**https://olliebot122333.github.io/coolpytools/**

## 👨‍💻 Creator

Created by **Oliver Morandi**.

CoolPyTools is a personal project created to learn Python, GUI development, Git, GitHub, Linux, and software development on Raspberry Pi.

## 📜 License

This project is currently a personal project. A license may be added in the future.

---

⭐ If you find CoolPyTools interesting, feel free to explore the source code!
