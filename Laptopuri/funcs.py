from datetime import datetime
from unidecode import unidecode
from dicts_lists import laptop_brands


def process_data(item):
    offer = item.get('offer', [])
    feedback = item.get('feedback', [])

    title = item['name']
    if not title.startswith('Laptop'):
        return None
    spec_list = title.split(',')
    brand_model = spec_list[0]
    for i in laptop_brands:
        if i.lower() in brand_model.lower():
            brand = i
            break
    spec_list2 = brand_model.split('cu procesor')
    model = spec_list2[0].removesuffix(f"laptop {brand.lower()}")
    procesor_raw = spec_list2[-1]
    procesor = unidecode(procesor_raw)

    display = next((spec for spec in spec_list[1:] if ), 'n/a')
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
