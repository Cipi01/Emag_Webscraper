from datetime import datetime
from unidecode import unidecode
from dicts_lists import laptop_brands


def process_data(item):
    offer = item.get('offer', [])
    feedback = item.get('feedback', [])

    title_raw = item['name']
    title = unidecode(title_raw)
    if not title.startswith('Laptop'):
        return None
    spec_list = title.split(',')
    brand_model = spec_list[0]
    for i in laptop_brands:
        if i.lower() in brand_model.lower():
            brand = i
            break
    spec_list2 = brand_model.split('cu procesor')
    model = extract_word(spec_list2[0], brand, 'cu procesor')
    procesor_raw = spec_list2[-1]
    procesor = unidecode(procesor_raw)

    display = 'n/a'
    ram = 'n/a'
    stocare = 'n/a'
    placa_video = 'n/a'
    windows = 'n/a'
    color = 'n/a'

    if "int kb" not in spec_list[-1].lower() or "3y on-site premium care" not in spec_list[-1].lower() or\
            'premium care' not in spec_list[-1].lower():
        color = spec_list[-1]
    else:
        color = spec_list[-2]
    windows = spec_list[-2]
    for i in spec_list:
        if "nvidia" in i.lower() or "amd" in i.lower() or 'geforce' in i.lower() or 'intel' in i.lower():
            placa_video = i
        if '"' in i:
            display = i
        if 'ips' in i.lower() or 'full hd' in i.lower() or 'WUXGA' in i.lower():
            display += i
        if 'hz' in i.lower():
            display += i
        if 'ssd' in i.lower():
            stocare = i


    # TODO: display consists of 2-3 items in spec_list, integrate with next()




    price = offer['price']['current']
    rating = feedback['rating']
    rating_no = feedback['reviews']['count']
    url = item['url']['desktop_base'] + item['url']['path']
    scraped_date = datetime.now().strftime("%d/%m/%y")
    return [
        title,
        brand,
        model,
        price,
        procesor,
        ram,
        stocare,
        placa_video,
        display,
        windows,
        color,
        rating,
        rating_no,
        url,
        scraped_date
    ]

def extract_word(string, start_substring, end_substring):
    start_index = string.find(start_substring) + len(start_substring)
    end_index = string.find(end_substring, start_index)
    if start_index == -1 or end_index == -1:
        return None
    return string[start_index:end_index]
