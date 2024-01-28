''' Generate the text for the A4 documents. '''
import os
from PIL import Image, ImageDraw, ImageFont

from folder_generator import FolderGenerator


''' Text adder to the blank documents '''
class TextGenerator():
    def __init__(self, folder_name, page_name, font):
        ''' Open the blank page. '''
        self.page_path = f'{folder_name}/{page_name}'
        self.page = Image.open(self.page_path)
        ''' Drawing object. '''
        self.draw = ImageDraw.Draw(self.page)
        self.font_type = font
        
        
    def add_text(self, folder, size, txt_pos, txt, txt_anchor, txt_color):
        ''' Set font and size. '''
        font_path = f'Fonts/{self.font_type}'
        font = ImageFont.truetype(font_path, size)

        ''' Add the text to the blank page. '''
        self.draw.text(txt_pos, txt, font=font, 
                       fill=txt_color, anchor=txt_anchor)

        ''' Save the modified page. '''
        # output_path = self.page_path
        output_path = f'{folder}/Test.tiff'
        self.page.save(output_path, format='TIFF')

        print('Text added successfully!')


''' Using the folder name as placeholder. '''
folder_gen = FolderGenerator()
folder = folder_gen.generate_name('Menu')

FONT = 'QueensidesMedium-x30zV.ttf'
TXT_BLACK = (0, 0, 0)
TITLE_SIZE = 180
TXT_POS = (1240, 180)
ANCHOR = 'mb'
TXT = 'This is a title'

txt_gen = TextGenerator(folder, 'Page_1.tiff', FONT)
''' Title text. '''
txt_gen.add_text(folder, TITLE_SIZE, TXT_POS, TXT, ANCHOR, TXT_BLACK)


# Anchor, text size and position have to be somehow related.

'''
    TextGenerator class must take a document, and therefore, 
    a path to open it.
    It must have a font, size and color (depending on type of text).
    Title, item with filler dots and its price and below
    each item, a description (grey color).
    The position on the X axis must be centered with every title.
    The items must be left-aligned and the prices must be right-aligned.
    Between the item name and its price will be filler dots.
    below each item name, will be a short description.

    The position on the Y axis remains to be defined..

    Consider using freetype or fontforge to load and manipulate fonts
    directly within Python. (With a separate class).

    For the text generation, it would be a good idea to have different
    object that inherit from TextGenerator(), so it can be an object
    title, an object item with dots filler and price, and another 
    object for the description.
'''