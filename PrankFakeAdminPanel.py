import pyfiglet
import time
import pyautogui

print(pyfiglet.figlet_format("Admin Panel"))
time.sleep(1)
server_name = input("Enter IP Server: ")
time.sleep(1)
print(f"Connecting to server {server_name}...")
time.sleep(2)
login = input("Enter you login: ")
password = input("Enter password to continue: ")

if login == "admin" and password == "root":
    print(f"Welcome, {login}!")
    time.sleep(1)
    adminpanel = input("Enter passcode to open AdminPanel: ")
    if adminpanel == "123":
        pyautogui.alert('We are not responsible for your actions.')
        time.sleep(2)
        print(f"Welcome to AdminPanel, {login}!")
        time.sleep(1)
        want = input("Enter command (/ban all, /op all or /ping): ")
        if want == "/ban all":
            print(f"{login} banned all server!")
        elif want == "/op all":
            print(f"{login} opped all server!")
        if want == "/ping":
            print(f"{login} pinging server...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(1)
            print("Ping...")
            time.sleep(3)
            print("Server has been shut down!")

        else:
            print("Invalid command!")
            time.sleep(2)
            want = input("Enter command (/ban all, /op all or /ping): ")
            if adminpanel == "123":
                pyautogui.alert('We are not responsible for your actions.')
                time.sleep(2)
                print(f"Welcome to AdminPanel, {login}!")
                time.sleep(1)
                want = input("Enter command (/ban all, /op all or /ping): ")
                if want == "/ban all":
                    print(f"{login} banned all server!")
                elif want == "/op all":
                    print(f"{login} opped all server!")
                if want == "/ping":
                    print(f"{login} pinging server...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(1)
                    print("Ping...")
                    time.sleep(3)
                    print("Server has been shut down!")

    else:
        print("Invalid passcode!")
        time.sleep(2)
        adminpanel = input("Enter passcode to open AdminPanel: ")
        if adminpanel == "123":
            pyautogui.alert('We are not responsible for your actions.')
            time.sleep(2)
            print(f"Welcome to AdminPanel, {login}!")
            time.sleep(1)
            want = input("Enter command (/ban all, /op all or /ping): ")
            if want == "/ban all":
                print(f"{login} banned all server!")
            elif want == "/op all":
                print(f"{login} opped all server!")
            if want == "/ping":
                print(f"{login} pinging server...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(3)
                print("Server has been shut down!")

else:
    print("Invalid login or password!")
    time.sleep(2)
    login = input("Enter you login: ")
    password = input("Enter password to continue: ")
    if login == "admin" and password == "root":
        print(f"Welcome, {login}!")
        time.sleep(1)
        adminpanel = input("Enter passcode to open AdminPanel: ")
        if adminpanel == "123":
            pyautogui.alert('We are not responsible for your actions.')
            time.sleep(2)
            print(f"Welcome to AdminPanel, {login}!")
            time.sleep(1)
            want = input("Enter command (/ban all, /op all or /ping): ")
            if want == "/ban all":
                print(f"{login} banned all server!")
            elif want == "/op all":
                print(f"{login} opped all server!")
            if want == "/ping":
                print(f"{login} pinging server...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(1)
                print("Ping...")
                time.sleep(3)
                print("Server has been shut down!")
input("Press Enter to exit")

