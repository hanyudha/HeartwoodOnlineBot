import cv2
import pyautogui
import numpy as np
import time

# Fungsi untuk menemukan objek di layar
def find_object(template_path, threshold=0.8):
    # Ambil screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    # Baca gambar template
    template = cv2.imread(template_path, 0)
    h, w = template.shape

    # Cocokkan template dengan screenshot
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    # Jika ditemukan, kembalikan koordinat
    for pt in zip(*loc[::-1]):
        return pt[0] + w // 2, pt[1] + h // 2
    return None

# Fungsi untuk melakukan mining
def mining_bot(template_path, duration=30):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Temukan objek
        position = find_object(template_path)
        if position:
            print(f"Objek ditemukan di: {position}")
            
            # Gerakkan mouse ke objek
            pyautogui.moveTo(position)
            time.sleep(0.5)  # Beri jeda

            # Klik kiri untuk menambang
            pyautogui.click()
            time.sleep(3)  # Tunggu proses mining selesai
        else:
            print("Objek tidak ditemukan. Mencari kembali...")
            time.sleep(1)  # Delay sebelum mencoba lagi

# Jalankan bot
if __name__ == "__main__":
    # Ganti "image.png" dengan path ke gambar objek
    mining_bot("image.png")
