#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg                        # Part 1 - The import


html_url = 'https://www.bcv.org.ve/seccionportal/tipo-de-cambio-oficial-del-bcv'
html_text = requests.get(html_url).text
soup = BeautifulSoup(html_text, 'html.parser')

t = soup.find("div", {"id": "dolar"})
t = t.find("div", {"class": "col-sm-6 col-xs-6 centrado"})
t = t.getText()
t = t.replace(",",".")
t = float(t)
tasa = round(t,2)
print(tasa)

# Define the window's contents
layout = [  [sg.Image('/home/russo/Documents/codigo/python/tasa_BCV/dollar.png', expand_x=False, expand_y=False, background_color="#ffffff"),
             sg.Text(text=str(tasa) + ' Bs', font=('Arial Bold', 20),text_color="#000000", background_color="#ffffff")
                ]
            ]

# Create the window
window = sg.Window('Tasa BCV', layout, background_color='#ffffff')      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Finish up by removing from the screen
window.close() 