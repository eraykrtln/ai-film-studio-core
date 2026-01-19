import time
import json
import requests
import os

# GitHub ayarların (Bilgisayara geçince kullanıcı adını yazacağız)
GITHUB_QUEUE_URL = "https://raw.githubusercontent.com/KULLANICI_ADIN/ai-film-studio-core/main/queue.json"

def process_queue():
    print("Sistem aktif... GitHub kuyruğu kontrol ediliyor.")
    while True:
        try:
            # GitHub'daki kuyruğu oku
            response = requests.get(GITHUB_QUEUE_URL)
            queue = response.json()

            if queue:
                for task in queue:
                    print(f"Yeni İş Bulundu: {task['title']}")
                    # Burada daha önce yazdığımız render fonksiyonlarını çağıracağız
                    # render_video(task['script']) 
                    print("Sahne işleniyor, RTX 3070 devrede...")
                    time.sleep(5) # Simülasyon
            else:
                print("Kuyruk boş, 30 saniye sonra tekrar kontrol edilecek...")
            
            time.sleep(30) # Bilgisayarı yormamak için bekleme süresi
        except Exception as e:
            print(f"Bağlantı bekleniyor... {e}")
            time.sleep(10)

if __name__ == "__main__":
    process_queue()
