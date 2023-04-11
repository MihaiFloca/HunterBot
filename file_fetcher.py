
import requests
import pandas as pd
import random

print('https://video.twimg.com/ext_tw_video/1605444560703950848/pu/pl/n1Dr39j9i5pNe0sY.m3u8?tag=12&container=fmp4'.find('.mp4'))

def get_file():
    img_data = requests.get(get_random_image()).content
    return img_data
    # with open('image_name.jpg', 'wb') as handler:
    #     handler.write(img
    
# TODO Delete empty rows from excel
def get_excel_page():
    excel_number = random.randint(1, 3)
    print(excel_number)
    match excel_number:
        case 1:
            return pd.read_excel('HOURLYHUNTY.xlsx')
        case 2:
            return pd.read_excel('HUNTERSEXO.xlsx')
        case 3:
            return pd.read_excel('HUNTERSJPG.xlsx')
        case _:
            return pd.read_excel('HOURLYHUNTY.xlsx')
    
def get_random_image():
    workbook = get_excel_page()    
    max_len = len(workbook)
    line_number = random.randint(0, max_len)
    
    media_type = workbook['Media Type'].iloc[line_number]
    image_url = workbook['Media URLs'].iloc[line_number]

    if image_url is None:
        return None

    if media_type in ['video', 'photo']:
        if media_type == 'video':
            if image_url.find('.mp4') == -1:
                return None
        # TODO Check if media was already sent
        # TODO Add already sent media to a file
        return image_url

