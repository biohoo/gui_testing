import PySimpleGUI as sg
from tkinter import filedialog
import webbrowser
import yaml

with open('ui_run_config.yaml','r') as f:
    ui_config = yaml.load(f)


# Static Variables
WINDOW_TITLE = ui_config.get('window_title',None)
INTRODUCTORY_MESSAGE = ui_config.get('introductory_message',None)
HELP_MESSAGE = ui_config.get('help_message', None)

PRINTERS = ui_config.get('printers')

# Dynamic Variables
filename = None


#   Window settings
sg.change_look_and_feel(ui_config.get('window_theme'))    # Add a touch of color

# All the stuff inside your window.
layout = [
            [sg.Text(INTRODUCTORY_MESSAGE)],
            [sg.Button('Select File...'),sg.Text('               '*80,key='_INPUT_')],
            [sg.Text('Optional: enter custom text for all labels:'), sg.InputText()],
            [sg.Checkbox('no'), sg.Combo(list(PRINTERS.keys()),default_value='Friendlyname 1')],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Special...'), sg.Button('Help'), sg.Button('Open Site')]
            ]


# Create the Window
window = sg.Window(WINDOW_TITLE, layout)

def process_file(file):
    with open(file) as f:
        file_string = f.read()
        sg.popup(file_string)

def call_site(website):
    print('opening...')
    webbrowser.open(website)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break

    elif event in ('Help'):
        sg.popup(HELP_MESSAGE)

    elif event in ('Ok') and (filename == None or not filename.endswith('.csv')):

        if filename == None:
            filename = '.nonexistent'

        sg.popup('The file you selected is a %s file.\nPlease select a csv file.\n\nReport any bugs to Jonathan Rice.' % filename.split('.')[1])


    elif event in ('Ok'):

        process_file(filename)

        if values[1]:
            sg.popup('howdy pardner.',title='You checked the box.',background_color='blue',custom_text='hello there')
            print('the box was checked.  Long live the box.')
        print(PRINTERS[values[2]])
        break

    elif event in ('Select File...'):
        filename = filedialog.askopenfilename()
        print(filename.split('/')[-1])

        window['_INPUT_'].update(filename)
    elif event in ('Special...'):
        sg.popup('You discovered a special button!\n\nGood for you.')
    elif event in ('Open Site'):
        call_site('http://www.google.com')
    else:
        print(window.read())

window.close()