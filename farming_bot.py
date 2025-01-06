import pygetwindow as gw
import pyautogui
import time
import win32gui
import win32con
import random

def focus_game_window(window_title="Heartwood Online"):
    windows = gw.getWindowsWithTitle(window_title)

    if len(windows) > 0:
        game_window = windows[0]
        print(f"Window ditemukan: {game_window.title}")
        game_window.activate()
        return game_window
    else:
        print(f"Window dengan judul '{window_title}' tidak ditemukan.")
        return None

def farming_bot_with_movement(game_window, duration=2):
    x, y, width, height = game_window.left, game_window.top, game_window.width, game_window.height
    print("Mulai farming dan simulasi gerakan...")

    start_time = time.time()
    while time.time() - start_time < duration:
        # pyautogui.press('1')  # Simulasi tombol serangan
        # time.sleep(1)
        # pyautogui.press('2')  # Simulasi skill
        # time.sleep(1)

        pyautogui.press('a')  # Gerakan ke kiri
        time.sleep(0.5)
        pyautogui.press('w')  # Gerakan ke depan
        time.sleep(0.5)
        # pyautogui.press('s')  # Gerakan ke belakang
        # time.sleep(0.5)
        # pyautogui.press('d')  # Gerakan ke kanan
        # time.sleep(0.5)

    print("Farming selesai.")

def move_towards_object(object_image, game_window):
    print("Mencari objek...")
    try:
        object_location = pyautogui.locateCenterOnScreen(object_image, confidence=0.8)
        if object_location:
            print(f"Objek ditemukan di {object_location}. Menggerakkan karakter menuju objek.")
            object_x, object_y = object_location
            window_x, window_y = game_window.left, game_window.top

            # Menghitung posisi karakter relatif terhadap window game
            current_x = window_x + game_window.width // 2
            current_y = window_y + game_window.height // 2

            # Hitung delta (perbedaan posisi)
            delta_x = object_x - current_x
            delta_y = object_y - current_y

            # Menggerakkan karakter berdasarkan delta
            move_to_position(delta_x, delta_y, game_window, object_x, object_y)
        else:
            print("Objek tidak ditemukan di layar.")
    except pyautogui.ImageNotFoundException:
        print("Gambar objek tidak dapat ditemukan di layar.")

def move_to_position(delta_x, delta_y, game_window, object_x, object_y):
    print(f"Mendekati posisi objek dengan delta ({delta_x}, {delta_y})")

    step_size = 5  # Langkah kecil untuk pergerakan yang lebih presisi
    tolerance = 5  # Toleransi untuk menghentikan pergerakan saat cukup dekat

    # Hitung posisi karakter relatif terhadap window
    current_x = game_window.left + game_window.width // 2
    current_y = game_window.top + game_window.height // 2

    # Gerakan menuju objek berdasarkan delta (posisi relatif)
    while abs(delta_x) > tolerance or abs(delta_y) > tolerance:
        if delta_x > 0:  # Gerak ke kanan
            pyautogui.press('d')
            current_x += step_size
        elif delta_x < 0:  # Gerak ke kiri
            pyautogui.press('a')
            current_x -= step_size

        if delta_y > 0:  # Gerak ke bawah
            pyautogui.press('s')
            current_y += step_size
        elif delta_y < 0:  # Gerak ke atas
            pyautogui.press('w')
            current_y -= step_size

        # Update delta dengan posisi baru
        delta_x = object_x - current_x
        delta_y = object_y - current_y

        time.sleep(0.1)

    print(f"Karakter sudah cukup dekat di posisi ({current_x}, {current_y}).")
    print("Karakter telah mencapai posisi objek.")

    # Setelah cukup dekat dengan objek, lakukan klik untuk mengambil/menambang objek
    click_on_object(object_x, object_y)

    # Klik pada pusat layar setelah objek terambil
    click_center_of_display(game_window)

def click_on_object(object_x, object_y):
    print(f"Melakukan klik pada objek di {object_x}, {object_y}")
    
    # Offset klik untuk presisi lebih tinggi (menyesuaikan dengan posisi objek)
    offset_x = 5  # Menggeser klik sedikit di sumbu X
    offset_y = 5  # Menggeser klik sedikit di sumbu Y
    
    # Klik di posisi objek dengan offset
    # pyautogui.click(object_x + offset_x, object_y + offset_y)
    # print("Klik berhasil dilakukan!")

def click_center_of_display(game_window):
    # Menghitung posisi tengah dari jendela game
    x_center = game_window.left + game_window.width // 2
    y_center = game_window.top + game_window.height // 2

    # Klik pada posisi tengah karakter (center of display)
    pyautogui.click(x_center, y_center)
    time.sleep(3)  # Tunggu sebentar setelah klik
    print(f"Klik pada pusat layar (center of display) di ({x_center}, {y_center})")
    
    # Tekan tombol spasi 2 kali berturut-turut dengan jeda 1 detik
    pyautogui.press('space')
    time.sleep(1)  # Tunggu 1 detik
    pyautogui.press('space')


# Fungsi untuk menggerakkan karakter sedikit menjauh (untuk memastikan objek tidak tertutup)
def move_away_from_object(game_window, move_distance=30):
    # Menggerakkan karakter sedikit menjauh dari objek (untuk membuka area pencarian)
    print(f"Gerakkan karakter menjauh sedikit (menarik mundur) untuk pencarian objek ulang...")
    pyautogui.press('w')  # Gerak ke atas
    time.sleep(0.1)
    pyautogui.press('a')  # Gerak ke kiri
    time.sleep(0.1)
    # Kembali ke posisi semula (hanya jika perlu)
    pyautogui.press('s')  # Gerak ke bawah
    time.sleep(0.1)
    pyautogui.press('d')  # Gerak ke kanan

# Fungsi utama untuk melakukan loop dengan delay 20 detik
def loop_with_delay(object_image_path, game_window, delay=5):
    #start_time = time.time()
    #while time.time() - start_time < loop_duration:
    while True:
        # Step 1: Gerakkan karakter sejauh 10 ke arah atas
        
        
        directions = ['w']  # w: atas (naik), a: kiri, s: bawah (turun), d: kanan
        direction = random.choice(directions)  # Memilih arah secara acak
        for _ in range(3):  # Menggerakkan karakter sebanyak 15 langkah
            pyautogui.press(direction)  # Menekan tombol sesuai arah
            time.sleep(0.1)  # Memberikan sedikit jeda antara tiap langkah
            print(f"Gerakkan karakter sejauh 15 langkah ke arah {direction}.")

        # Step 2: Tunggu selama 5 detik
        print("Menunggu selama 5 detik...")
        time.sleep(4)

        # Step 3: Mulai lagi fungsi move_towards_object untuk mencari objek
        object_coordinates = move_towards_object(object_image_path, game_window)
        
        # Periksa apakah objek ditemukan sebelum melanjutkan
        if object_coordinates is not None:
            object_x, object_y = object_coordinates
            click_on_object(object_x, object_y)
            time.sleep(4)  # Tunggu sebentar setelah mengambil objek
            # Menekan tombol spasi 3 kali berturut-turut
            for _ in range(3):
                pyautogui.press('space')
                time.sleep(0.1)
            
            # Gerakkan sedikit menjauh untuk menghindari objek tertutup
            move_away_from_object(game_window)
        
        # Tunggu 10 detik sebelum melakukan loop lagi
        print(f"Menunggu {delay} detik sebelum iterasi berikutnya...")
        time.sleep(delay)


# Contoh penggunaan
game_window = focus_game_window()

if game_window:
    farming_bot_with_movement(game_window)
    object_image_path = r'C:\Users\hanyu\OneDrive\Desktop\berry_1.png'
    loop_with_delay(object_image_path, game_window, delay=5)
else:
    print("Gagal menemukan window game.")
