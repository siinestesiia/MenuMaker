''' Generate restaurant menu pages. '''
import os

from folder_generator import FolderGenerator
from page_generator import PageGenerator
# from text_generator import TextGenerator


''' Page Settings '''
PAGE_NAME = 'Page_'
FILE_FORMAT = 'tiff'
COLOR_MODE = 'CMYK'
A4_SIZE = (2480, 3508)
WHITE_COLOR = (0, 0, 0, 0)


class MenuMaker():
    def __init__(self):
        pass
    

    ''' Generate n amount of pages. '''
    def pages_generator(self, folder_name, page_name, file_format, n_pages):
        counter = 1
        
        for pages in range(n_pages):
            while True:
                document_name = f'{page_name}_{counter}.{file_format}'
                page_path = os.path.join(folder_name, document_name)

                if not os.path.isfile(page_path):
                    break

                counter += 1
            
            page.generate_page(folder_name, document_name)
            # text_gen =  TextGenerator(folder_name, page_name)
            # add text to each document here.


''' Create the folder that contains the pages. '''
folder_gen = FolderGenerator()
folder_name = folder_gen.generate_name('Menu')
folder_gen.generate_folder(folder_name)


page = PageGenerator(FILE_FORMAT, COLOR_MODE, A4_SIZE, WHITE_COLOR)
menu = MenuMaker()
menu.pages_generator(folder_name, 'Page', FILE_FORMAT, 1)