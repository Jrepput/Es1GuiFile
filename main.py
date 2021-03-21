import PySimpleGUI as sg
import os

sg.theme("DarkAmber")


layout = [[sg.Text('Nome', size=(10, 1)),
            sg.InputText(key='-NAME-')],
          [sg.Text('Cognome', size=(10, 1)), sg.InputText(key='-COGNOME-')],
          [sg.Text('Età', size=(10, 1)), sg.InputText(key='-ETA-')],
          [sg.Button('Aggiungi al file'), sg.Button('Annulla')],
          [sg.Text('NOME SALVATO SUL FILE:'), sg.Text(size=(15,1), key='-OUTPUTNOME-')],
          [sg.Text('COGNOME SALVATO SUL FILE:'), sg.Text(size=(15,1), key='-OUTPUTCOGNOME-')],
          [sg.Text('ETÁ SALVATO SUL FILE:'), sg.Text(size=(15,1), key='-OUTPUTETA-')]]


window=sg.Window("GESTIONALE DONATORI SANGUE", layout, grab_anywhere=True)

if os.path.exists("File.csv"):
  pass
else:
  file=open("File.csv","x")
  file.close()

while True:
  event, values=window.read()

  print(event, values)

  if event==sg.WIN_CLOSED:
    break

  elif event=="Annulla":
    window["-NAME-"].update("")
    window["-COGNOME-"].update("")
    window["-ETA-"].update("")

  elif event=="Aggiungi al file":
    if 18<=int(values["-ETA-"])<70:
      window["-OUTPUTNOME-"].update(values["-NAME-"], text_color="red")
      window["-OUTPUTCOGNOME-"].update(values["-COGNOME-"], text_color="red")
      window["-OUTPUTETA-"].update(values["-ETA-"], text_color="red")
      
      file=open("File.csv","a")
      file.write(f'{values["-NAME-"]};{values["-COGNOME-"]};{values["-ETA-"]}\n')
      file.close()

      sg.popup('Donatore salvato')

    else:
      window["-ETA-"].update("")

      sg.popup('ERRORE  >>valore età inserito non valido<<')
  
window.close()
