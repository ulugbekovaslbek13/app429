import os
import shutil

def clean_temp():
    # Windows'ning vaqtinchalik kesh papkalari yo'li
    temp_paths = [
        os.environ.get('TEMP'),
        r"C:\Windows\Temp"
    ]
    
    print("🧹 Kompyuterdagi keraksiz kesh fayllar tozalanmoqda...\n")
    
    for path in temp_paths:
        if path and os.path.exists(path):
            print(f"📁 Joylashuv: {path}")
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print(f"🗑️ O'chirildi: {filename}")
                except Exception as e:
                    # Hozirda tizim tomonidan ishlatilayotgan fayllarni o'chira olmasa, o'tkazib yuboradi
                    continue
    print("\n✅ Tozalash jarayoni yakunlandi!")

if __name__ == "__main__":
    clean_temp()