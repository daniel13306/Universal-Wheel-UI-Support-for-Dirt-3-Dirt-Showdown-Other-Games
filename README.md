# Simple Universal Wheel UI Fix for Dirt 3, Dirt Showdown and Other Games by DeadEagleNL

✅ Converts wheel button presses and D-Pad to keyboard keys for **Dirt 3**, **Dirt Showdown**, and **ANY other game** that lacks proper UI support for wheels.  
✅ Plug-and-play: detects any joystick or wheel automatically, the script will tell you if it detects your wheel.  
✅ Pre-mapped keys:
- **Button 0/1 → Enter**
- **Button 2 → Escape**
- **Button 7 → Tab**
- **Button 8 → Backspace**
- **D-Pad → Arrow keys (Up, Down, Left, Right)**

✅ Works in **ANY game with keyboard-driven menus**, not just Dirt, you can use it anywhere your wheel doesn’t work in UI screens.

✏️ **Customizable:**  
If you want to edit the application yourself, you can download the `.py` file and easily modify the `BUTTON_MAP` or `HAT_MAP` sections to change any button or D-Pad mappings.  

To remap your own buttons, toggle the `noprint` boolean at the top of the file. The app will print the ID of any pressed button so you can easily remap (some wheels swap button numbers, this fixes that quickly).


# How to Use

## ✅ Simple (EXE) Use:
<img width="365" height="120" alt="image" src="https://github.com/user-attachments/assets/f0d8299a-03b8-4d45-8930-67a9ebb4ebd7" />

- Download the `.exe` file and run it.  
- Windows will give a **“Windows protected your PC”** warning because the EXE is unsigned. (This is a common issue with Pyinstaller)
  - Just click **More info → Run anyway** to continue.
- This EXE is ready to go, no need to install Python or any packages.
- ✅ Just **plug in your wheel before running the EXE** and it works.
- If the key mapping isn’t correct for your wheel, download the `.py` script to easily remap it.

## ✅ Python (Script) Use:
<img width="894" height="55" alt="image" src="https://github.com/user-attachments/assets/e6429adb-f37b-458e-8a87-874c647f32f4" />

- Download the `.py` script and run it manually.
- If you don’t have Python:  
   - Install **Python 3.10** (recommended for better pygame compatibility).
   - Install the required packages using:
     ```
     pip install pygame keyboard
     ```
- The `.py` file is the **exact same script as the EXE**, just provided for users who prefer to customize or run it directly.
