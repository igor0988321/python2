import keyboard
import webbrowser

print('Press  Ctrl+Shift+V.')

def main():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

keyboard.add_hotkey('Ctrl+Shift+V', main)

keyboard.wait()