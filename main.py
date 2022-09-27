import random
import pyautogui
import time


def getName():
    with open("data/names.txt", "r") as names:
        allNames = names.read()
        names = list(map(str, allNames.split()))
        return random.choice(names)

def getPhoneNumber(count):
    with open("data/phone_numbers.txt", "r") as numbers:
        allNumbers = numbers.read()
        numbers = list(map(str, allNumbers.split("\n")))
        number = numbers[count][4: 15].replace(" ", "")
        return number

def getEmailID(name):
    name = name.lower()
    number = random.randint(1111,9999)
    providers = ["gmail.com", "yahoo.com", "outlook.com"]
    provider = random.choice(providers)
    return f"{name}.{number}@{provider}"

# main functionality starts here
# initial delay to select the window
print('waiting.', end='')
for _ in range(5):
    time.sleep(0.5)
    print('..', end='')
    time.sleep(0.5)
print('\n')

pyautogui.alert(
    '''                             
    ╔═╗┌─┐┬─┐┌┬┐╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
    ╠╣ │ │├┬┘│││╚═╗├─┘├─┤││││││├┤ ├┬┘
    ╚  └─┘┴└─┴ ┴╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─
    Version 0.1 Alpha 
    '''
)
confirmation = pyautogui.confirm('Start Spammer?')

print(confirmation)
if confirmation != 'OK':
    exit(0)

counter = 1
while counter < 10:
    name = getName()
    phone = getPhoneNumber(counter)
    email = getEmailID(name)

    print(f"Generated Data: {name}, {phone} and {email}")

    for i in range(5):
        pyautogui.press("tab")

    pyautogui.typewrite(name) 
    pyautogui.press("tab")

    pyautogui.typewrite(phone)
    pyautogui.press("tab")

    for i in range(4):
        pyautogui.press("enter")
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")

    pyautogui.typewrite(phone)

    pyautogui.press("tab")
    pyautogui.typewrite(email)

    pyautogui.press("enter")
    counter += 1

    time.sleep(5)
    pyautogui.press("enter")
    
    pyautogui.hotkey('alt', 'left')
    time.sleep(5)

    pyautogui.press("f5")