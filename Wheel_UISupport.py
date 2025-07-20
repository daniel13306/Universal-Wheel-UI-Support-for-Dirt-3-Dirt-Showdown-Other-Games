import pygame
import keyboard
import time
import sys

# Note, this button mapping is for the G29 wheel, if it doesnt align with your buttons
# Toggle the noprint boolean below, then run the script, and press the keys.
# Their ID will be printed, like this you can put the ID in the button mapping below.

# Config
noprint = True # Set this to False to print button ID's, like this you can easily map new keys below.
BUTTON_MAP = {
    0: 'enter',
    1: 'enter',
    2: 'esc',
    7: 'tab',
    8: 'backspace'
}

HAT_MAP = {
    (0, 1): 'up',
    (0, -1): 'down',
    (-1, 0): 'left',
    (1, 0): 'right'
}

HOLD_TIME = 0.05



pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected, closing app.")
    time.sleep(3)
    sys.exit()


js = pygame.joystick.Joystick(0)
js.init()
print(f"Detected device: {js.get_name()} with {js.get_numbuttons()} buttons, {js.get_numhats()} hats")

button_states = {btn: False for btn in range(js.get_numbuttons())}
last_hat = (0, 0)



def press_and_hold(key, log_name):
    key_text = key if key else 'Unmapped'
    print(f"[{log_name}] → '{key_text}' (held {HOLD_TIME * 1000:.0f}ms)")
    if key:
        keyboard.press(key)
        time.sleep(HOLD_TIME)
        keyboard.release(key)


while True:
    pygame.event.pump()
    for btn in range(js.get_numbuttons()):
        pressed = js.get_button(btn)
        if pressed and not button_states[btn]:
            key = BUTTON_MAP.get(btn)
            if noprint == False:
                keystr = str(key)
                if str(key) == "None":
                    keystr = "Unmapped key"
                print(f"[Button {btn}] → '{keystr}' (KeyID: {btn})")
            if key:
                press_and_hold(key, f"Button {btn}")
            button_states[btn] = True
        elif not pressed:
            button_states[btn] = False
    if js.get_numhats() > 0:
        hat = js.get_hat(0)
        if hat != last_hat:
            if hat in HAT_MAP:
                key = HAT_MAP[hat]
                press_and_hold(key, f"D-Pad {hat}")
            last_hat = hat

    time.sleep(0.005)
