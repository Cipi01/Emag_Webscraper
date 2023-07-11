from datetime import datetime


def process_data(item):
    offer = item.get('offer', [])
    feedback = item.get('feedback', [])

    title = item['name']
    if not title.startswith('Telefon mobil'):
        return None
    spec_list = title.split(',')
    if spec_list[0] == 'Telefon mobil':
        brand = spec_list[1]
        model = spec_list[2]
    else:
        phone = spec_list[0].replace('Telefon mobil', '').strip()
        phone_brand = phone.split(" ", maxsplit=1)
        brand = phone_brand[0]
        model = phone_brand[-1]
    color = spec_list[-1]
    NoSim = 'n/a'
    storage = 'n/a'
    ram = 'n/a'
    internet = 'n/a'
    for i in spec_list[1:]:

        if 'sim' in i or 'Sim' in i or 'SIM' in i:
            NoSim = i
        elif i.endswith('GB'):
            storage = i
        elif 'RAM' in i:
            ram = i
        elif i.endswith("G"):
            internet = i
    price = offer['price']['current']
    rating = feedback['rating']
    rating_no = feedback['reviews']['count']
    url = item['url']['desktop_base'] + item['url']['path']
    scraped_date = datetime.now().strftime("%d/%m/%y")
    return [
        title,
        brand,
        model,
        NoSim,
        storage,
        ram,
        internet,
        color,
        price,
        rating,
        rating_no,
        url,
        scraped_date
    ]
