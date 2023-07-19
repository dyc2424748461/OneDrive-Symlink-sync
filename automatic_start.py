import winreg
import sys
from create_shortcut import create_shortcut


def add_startup_registry_entry(name,description):
    # check the register_entry
    key_exists = False
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run")
        value, _ = winreg.QueryValueEx(key, name)
        winreg.CloseKey(key)
        key_exists = True
    except FileNotFoundError:
        pass
    except WindowsError:
        pass

    # if not exits
    if not key_exists:
        # get python executable
        python_executable = sys.executable

        # get current path
        script_path = get_current_script_path()
        print(script_path)
        # create register_entry
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)

            # create shortcut
        start_link=create_shortcut(name,python_executable,script_path,description)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, start_link)
        winreg.CloseKey(key)

        print("Startup registry entry added.")

def get_current_script_path():

    script_path = sys.argv[0]
    return script_path

def remove_from_startup(name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)

    winreg.DeleteValue(key, name)

    winreg.CloseKey(key)

if __name__ == "__main__":
    add_startup_registry_entry("MyProgram","myprogram")
