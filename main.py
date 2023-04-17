# from googletrans import Translator
import mousetracking
import characterrecognition
from PIL import ImageGrab, Image
import ctypes
import time
import winsound

user32 = ctypes.windll.user32
isTriggered = lambda triggerKey: user32.GetKeyState(triggerKey) > 1
mousetracker = mousetracking.MouseTracking()
text_extractor = characterrecognition.CharacterRecognition()

# Key code for printscreen
VK_F10 = 0x79
VK_SNAPSHOT = 0x2C
VK_P = 0x50

# For debouncing
is_key_pressed = {
    VK_SNAPSHOT: False,
    VK_F10: False,
    VK_P: False
}

is_watchdog_loop_enabled = True


img_coord_stack = []
def snip_screen_capture():
    pos = mousetracker.queryMousePosition()
    if len(img_coord_stack) < 1:
        img_coord_stack.append(pos)

    else:
        img_coord_stack.append(pos)
        screen_capture = ImageGrab.grab()
        cropped = screen_capture.crop((
            img_coord_stack[0]['x'],
            img_coord_stack[0]['y'],
            img_coord_stack[1]['x'],
            img_coord_stack[1]['y']
        ))

        img_coord_stack.clear()
        extract_characters(cropped)
        winsound.MessageBeep(winsound.MB_OK)


def extract_characters(img):
    text_extracted = text_extractor.get_text(img, 'ja')
    print(text_extracted)
    return 0


def translate_capture(extracted_text):
    return 0


print('Starting the watchdog')
while (is_watchdog_loop_enabled):
    try:
        # Terminate loop
        if isTriggered(VK_F10):
            if not is_key_pressed[VK_F10]:
                is_watchdog_loop_enabled = False
            is_key_pressed[VK_F10] = True
        else:
            is_key_pressed[VK_F10] = False

        # Snip screen capture
        if isTriggered(VK_P):
            if not is_key_pressed[VK_P]:
                snip_screen_capture()
            is_key_pressed[VK_P] = True
        else:
            is_key_pressed[VK_P] = False

    except Exception as e:
        print(e.args)
        break
