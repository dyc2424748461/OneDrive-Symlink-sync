import os
import winshell

def create_shortcut(shortcut_name, interpreter_path, script_path, description):
    # get folder path
    startup_folder = winshell.startup()

    # the shortcut path
    shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")

    # create shortcut
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = interpreter_path
        shortcut.arguments = script_path
        shortcut.description = description
    return shortcut_path



if __name__ == "__main__":
    interpreter_path = "C:\\Path\\To\\python.exe"
    script_path = "C:\\Path\\To\\main.py"
    description = "Your description here"
    create_shortcut("update symlink for OneDrive", interpreter_path, script_path, description)

