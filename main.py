import time
import pyautogui as pg
import webbrowser as web

numbers = []
message: str
first = True

with open("phone_numbers.txt", "r") as file:
    for line in file:
        numbers.append(line.strip())

with open("message.txt", "r") as file1:
    for line in file1:
        message = line.strip()

for number in numbers:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone=" + number + "&text=" + message)
    if first:
        time.sleep(6)
        first = False
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(8)
    pg.click()
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')