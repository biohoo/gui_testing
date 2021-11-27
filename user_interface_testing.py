
import PySimpleGUI as sg
from tkinter import filedialog
import yaml

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.

# TODO: preserve state with yaml instead of hard-coding...
printers = {
    'Friendlyname 1':'11.2.3.4.5',
    'Friendlyname 2':'11.2.2.333.4'
}

layout = [
            [sg.Button('Select File...'),sg.Text('               '*80,key='_INPUT_')],
            [sg.Text('Optional: enter custom text for all labels:'), sg.InputText()],
            [sg.Checkbox('no'), sg.Combo(list(printers.keys()),default_value='Friendlyname 1')],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Special...')]
            ]

# Create the Window
window = sg.Window('Window Title', layout)

filename = None

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break

    elif event in ('Ok') and filename == None:
        sg.popup('You MUST select a file.\n\nPretty please...\n')


    elif event in ('Ok'):
        if filename == None:
            sg.popup('You MUST select a file in order to print.\n\nMake sure it is a CSV file.')

        elif values[1]:
            sg.popup('howdy pardner.',title='You checked the box.',background_color='blue',custom_text='hello there')
            print('the box was checked.  Long live the box.')
        print(printers[values[2]])
        break

    elif event in ('Select File...'):
        filename = filedialog.askopenfilename()
        print(filename.split('/')[-1])

        window['_INPUT_'].update(filename)
    elif event in ('Special...'):
        sg.popup('You discovered a special button!\n\nGood for you.')

window.close()