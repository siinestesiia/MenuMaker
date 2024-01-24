''' Generate a folder with current date. '''
import os
from datetime import datetime


class FolderGenerator():
    def __init__(self):
        current_date = datetime.now()
        self.date = current_date.strftime('%d-%m-%Y')
        
    def generate_name(self, folder_title):
        return f'{folder_title} - {self.date}'

    def generate_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print(f'"{folder_name}" folder already exists.')  
        else:
            print(f'"{folder_name}" folder successfully created!')
