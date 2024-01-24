''' Generate A4 blank documents. '''
import os
from PIL import Image, ImageDraw, ImageFont


class PageGenerator:
    def __init__(self, file_format, color_mode, page_size, white_color):
        self.file_format = file_format
        self.color_mode = color_mode
        self.page_size = page_size
        self.white_color = white_color

    def generate_page(self, folder_name, page_name):
        page_path = os.path.join(folder_name, page_name)

        page = Image.new(self.color_mode, self.page_size, self.white_color)
        page.save(page_path)
        print(f'{page_name} created successfully!')
