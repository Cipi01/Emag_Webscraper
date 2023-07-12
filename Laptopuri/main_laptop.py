import requests
from funcs import process_data
from funcs_all import unique_col_inserter
import pandas as pd
import time
from datetime import datetime

date = datetime.now().strftime("%d_%m_%y")
data_list = []

for page in range(1, 2):
    time.sleep(2)
    if page == 1:
        offset = 0
        int_url = '%2Flaptopuri%2Fc'
    else:
        offset += 100
        int_url = f'%2Flaptopuri%2Fp{page}%2Fc'

    url = "https://www.emag.ro/search-by-url?source_id=7&templates%5B%5D=full&is_eab344=false&sortf%5" \
          f"Bpopularity_total_orders_vpatru%5D=desc&listing_display_id=2&page%5Blimit%5D=100&page%5Boffset%5D={offset}"\
          "&fields%5Bitems%5D%5Bimage_gallery%5D%5Bfashion%5D%5Blimit%5D=2&fields%5Bitems%5D%5Bimage%5D" \
          "%5Bresized_images%5D=1&fields%5Bitems%5D%5Bresized_images%5D=200x200%2C350x350%2C720x720&fields%5Bitems%5D" \
          "%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbuying_options%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bflags%5D=1" \
          "&fields%5Bitems%5D%5Boffer%5D%5Bbundles%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bgifts%5D=1&fields%5Bitems%5D" \
          "%5Bcharacteristics%5D=listing&fields%5Bquick_filters%5D=1&search_id=f4916dbf599d7d474965&search_fraze" \
          f"=&search_key=&url={int_url}"

    payload = {}
    headers = {
        'Cookie': 'EMAGROSESSID=7368fbc07d1fef67e36471d788fc64d7; EMAGUUID=1678342939-431973034-98429.266; '
                  'EMAGVISITOR=a%3A1%3A%7Bs%3A7%3A%22user_id%22%3Bi%3A2306730138044991662%3B%7D; '
                  '_pdr_internal=GA1.2.2911788641.1678342939; _pdr_view_id=1689080710-67260.695-8875073036; '
                  'eab1004=b; eab937=na; eab945=b; eab967=b; eab984=b; eab990=b; eab991=b; eab996=c; eab_allocation=; '
                  'ltuid=1678342939.418-88503ab08185d17e29a5404460bb15e52a38eee7; site_version_11=not_mobile'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    for i in data['data']['items']:
        processed_data = process_data(i)
        if processed_data is not None:
            data_list.append(processed_data)
    print(f"Done for page {page}")
    if len(data['data']['items']) != 100:
        break
columns = ['Title', 'Brand', 'Model', 'Price', 'Processor', 'RAM', 'Storage', 'Video', 'Display', 'Windows','Color', 'Rating', 'NoRating', 'URL', 'ScrapedDate']
df = pd.DataFrame(data_list, columns=columns)
df = df.drop_duplicates()
unique_col_inserter("EMAG_LAPTOP", df)

df.to_csv(f'D:/P/Webscrapers/BD/EMAG_LAPTOP/EMAG_LAPTOP_{date}.csv', index=False)
