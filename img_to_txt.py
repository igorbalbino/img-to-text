'''
Author: Igor E. S. Balbino (Igor B- From Brazil)
Date: 30/05/2021

Info: Created for Daniel. A client from Nigeria that found me through Freelancer.com.
He contracted me to create a app to transform image to txt file.

Needed modules:

PyAutoGUI
pytesseract
'''
import os
import subprocess as sb
from time import sleep
from datetime import date
import PySimpleGUI as sg
from PIL import Image
from pytesseract import *

class Util:
    def waitAMoment(self):
        sleep(1)
    #waitAMoment

    def replaceBars(self, txt):
        txt = str(txt)
        aux = txt.repalce('\\', '/')
        return aux
    #replaceBars
#Util

class convertToTxt:
    def __init__(self, filePath, folderPath):
        sg.Print('Preparing data to conversion...')
        self.util = Util()
        #self.filePath = self.util.replaceBars(filePath)
        #self.folderPath = self.util.replaceBars(folderPath)

        self.filePath = filePath
        self.folderPath = folderPath
        self.util.waitAMoment()
        self.convert(self.filePath, self.folderPath)
    #__init__

    def convert(self, filePath, folderPath):
        sg.Print('Converting...')
        pytesseract.tesseract_cmd = r'C:\Users\igorb\AppData\Local\Programs\Tesseract-OCR\tesseract'
        try:
            img = Image.open(filePath)
            print(img)
            text = pytesseract.image_to_string(img)
            sg.Print('Extracted text: ', text)
            today = date.today()
            today = str(today)
            print(today)
            thePath = str(folderPath+'\\'+'convertedData_'+today+'.txt')
            with open(thePath, 'w') as f:
                f.write(text)
        except Exception as e:
            sg.popup_error('Convert to text error!', e)
            print(e)
    #convert
#convertToTxt

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Image to Text', size=(60, 0))],
            [sg.Text('', size=(60, 0))],
            [sg.Submit('Help', size=(10, 0), key='helpBtn')],
            [sg.Text('', size=(60, 0))],
            [sg.Text('Select the image: '),
             sg.InputText('', size=(40, 5), key='filePath'),
             sg.FileBrowse(target='filePath'),
             sg.Stretch()],
            [sg.Text('Select where the text goes: '),
             sg.InputText('', size=(40, 5), key='folderPath'),
             sg.FolderBrowse(target='folderPath'),
             sg.Stretch()],
            [sg.Submit('Convert', size=(30, 0), key='convertBtn')]
        ]
        self.janela = sg.Window('Image to Text').layout(layout)
    #FECHA __init__

    def Iniciar(self):
        try:
            while True:
                self.event, self.values = self.janela.Read()
                filePath = self.values['filePath']
                folderPath = self.values['folderPath']

                if self.event == 'convertBtn':
                    toText = convertToTxt(filePath, folderPath)
                elif self.event == 'helpBtn':
                    sg.Print(f'{os.linesep}Welcome to the short tutorial of conversion!{os.linesep}'
                             f'Select the image file to be converted and the path where you want your txt to go.{os.linesep}'
                             f'Click the "Convert" button and wait for the conclusion of the process.{os.linesep}'
                             f'A message will be displayed when the process finishes.{os.linesep}{os.linesep}'
                             f'If you have any tesseract problems, consider downloading and installing one of these: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe (for 64bit) {os.linesep}'
                             f'or https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20210506.exe (for 32bit)'
                             f'{os.linesep}{os.linesep}'
                             f'When you close the app, an error may be displayed but you can ignore it. Just close it.{os.linesep}')
        except Exception as e:
            sg.popup_error('Screen values error!', e)
            print(e)
    #Iniciar
#TelaPython

tela = TelaPython()
tela.Iniciar()