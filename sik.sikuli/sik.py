import time

type(Key.ENTER)
with open("save_name_temp.txt") as f:
    save_name = f.read()

with open("current_led_id.txt") as f:
    current_led_id = f.read()

for x in range(20):
    click("1643259379602.png")
    wait("1643338111683.png", FOREVER)
    f = open("lighttrigger.txt", "a")
    f.close()
    wait(2)

click("1643114032360.png")

for x in range(3):
    type(Key.DOWN)

for x in range(3):
    type(Key.ENTER)

type(Key.BACKSPACE)
type(str(save_name))
type(Key.ENTER)

for x in range(4):
    type(Key.ENTER)

click("1643246721983.png")

for x in range(2):
    type(Key.DOWN)

for x in range(3):
    type(Key.ENTER)
