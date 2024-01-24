''' Generate the text for the A4 documents. '''
import os
from PIL import Image, ImageDraw, ImageFont

from folder_generator import FolderGenerator


''' Text adder to the blank documents '''
class TextGenerator():
    def __init__(self, folder_name, page_name, ):
        # Open the blank page.
        self.folder = folder_name
        self.page_path = f'{folder_name}/{page_name}'
        page = Image.open(self.page_path)
        
        # Drawing object.
        draw = ImageDraw.Draw(page)
        
        # # Set font and size
        # font_path = 'Fonts/QueensidesMedium-x30zV.ttf'
        # font_size = 200
        # font = ImageFont.truetype(font_path, font_size)
        
        # # Set position and text.
        # text_pos = (1240, 1754)
        # text = 'This is a text!'

        # # Set text color.
        # text_color = (0, 0, 0) # RGB
        
        # # Add the text to the blank page.
        # draw.text(text_pos, text, font=font, fill=text_color)

        # # Save the modified page.
        # output_path = 'Menu - 21-01-2024/Page_1(modified).tiff'
        # page_document.save(output_path)

        # print('Text added successfully!')
        pass
    
    def add_title(self, text, ):
        pass

    def add_item(self, text, ):
        pass

    def add_price(self, text, ):
        pass

    def add_filler_dots(self, ):
        pass

    def add_description(self, text, ):
        pass


''' Using the folder name as placeholder. '''
folder_gen = FolderGenerator()
folder = folder_gen.generate_name('Menu')



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
    directly within Python.
'''