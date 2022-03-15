import requests
from bs4 import BeautifulSoup
import time

def kontrolEt():
    url = "https://www.amazon.com.tr/Acer-AN515-45-R411-Ryzen-5600H-512GB/dp/B09NYFDYDR/ref=Oct_m_onr_12601898031?pd_rd_i=B09NYFDYDR&pd_rd_r=a1026406-abcd-4d9d-93b7-5563f3c0ef1f&pd_rd_w=GeZp5&pd_rd_wg=5XPhE&pf_rd_p=995c0ffa-8ad5-48fd-b7a0-8df850d09eff&pf_rd_r=4Z5Z1FSTCWPENWK1D2B5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    sayfa = requests.get(url, headers=headers)
    icerik = BeautifulSoup(sayfa.content, 'html.parser')

    urun_Adi = icerik.find(id='productTitle').get_text().strip()

    urun_Fiyat = icerik.find(id="corePriceDisplay_desktop_feature_div").get_text()
    urun_Donusen = int(urun_Fiyat[0:9].replace('.', ''))

    if (urun_Donusen < 13000):
        print(f"{urun_Donusen} TL {urun_Adi} fiyat dustu acele et!!")
    else:
        print(f"{urun_Donusen} TL {urun_Adi} Fiyat Dusmedi!!")

while(True):
    kontrolEt()
    time.sleep(3)