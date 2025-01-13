from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Konfigurasi Selenium
options = Options()
options.add_argument("--headless")  # Jalankan tanpa membuka browser
options.add_argument("--disable-gpu")  # Untuk performa lebih baik di headless mode
options.add_argument("--no-sandbox")  # Untuk sistem Linux
options.add_argument("--disable-dev-shm-usage")  # Menghindari masalah memori

# Inisialisasi driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL target
url = "https://liquipedia.net/dota2/The_International/2024/Statistics"
driver.get(url)

# Tunggu halaman selesai memuat
time.sleep(5)

# Temukan tabel dengan kelas spesifik
table = driver.find_element(By.CSS_SELECTOR, "table.wikitable.table-striped.sortable.jquery-tablesorter")

# Ambil semua baris dari tbody
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr.dota-stat-row")

# Persiapkan data untuk disimpan
data = []

# Iterasi melalui semua baris tabel
for row in rows:
    # Ambil semua kolom dalam baris
    cols = row.find_elements(By.TAG_NAME, "td")

    # Memastikan ada kolom yang cukup dalam baris
    if len(cols) >= 19:  # Memastikan ada kolom yang cukup (misalnya 6 kolom yang relevan)
        row_data = {
            "id": cols[0].text.strip() if cols[0].text.strip() else None,
            "hero": cols[1].text.strip() if cols[1].text.strip() else None,
            "t_picks": cols[2].text.strip() if cols[2].text.strip() else None,
            "t_wins": cols[3].text.strip() if cols[3].text.strip() else None,
            "t_losses": cols[4].text.strip() if cols[4].text.strip() else None,
            "t_wr": cols[5].text.strip() if cols[5].text.strip() else None,
            "percent_t": cols[6].text.strip() if cols[6].text.strip() else None,
            "t_picks_r": cols[7].text.strip() if cols[7].text.strip() else None,
            "t_wins_r": cols[8].text.strip() if cols[8].text.strip() else None,
            "t_losses_r": cols[9].text.strip() if cols[9].text.strip() else None,
            "t_wr_r": cols[10].text.strip() if cols[10].text.strip() else None,
            "t_picks_d": cols[11].text.strip() if cols[11].text.strip() else None,
            "t_wins_d": cols[12].text.strip() if cols[12].text.strip() else None,
            "t_losses_d": cols[13].text.strip() if cols[13].text.strip() else None,
            "t_wr_d": cols[14].text.strip() if cols[14].text.strip() else None,
            "t_bans": cols[15].text.strip() if cols[15].text.strip() else None,
            "bans_percent": cols[16].text.strip() if cols[16].text.strip() else None,
            "t_p_b": cols[17].text.strip() if cols[17].text.strip() else None,
            "percent_p_b": cols[18].text.strip() if cols[18].text.strip() else None,
        }

        # Hanya tambahkan jika ada data yang relevan
        if any(value is not None for value in row_data.values()):
            data.append(row_data)

# Simpan data ke dalam JSON dalam format array (bukan per baris)
with open("data/statistik_main_tournament.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data telah disimpan ke data_ti2024.json")

# Tutup driver
driver.quit()
