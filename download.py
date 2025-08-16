import sys
import yt_dlp

def show_menu():
    print("\n=== Video/Ses İndirme Aracı ===")
    print("1. Sadece ses (MP3)")
    print("2. 480p video")
    print("3. 720p video")
    print("4. 1080p video")
    print("5. 2K video (1440p)")
    print("6. 4K video (2160p)")
    print("7. En yüksek kalite")
    return input("Seçiminizi yapın (1-7): ")

def get_download_options(choice):
    if choice == "1":
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True
        }
    elif choice == "2":
        return {
            'format': 'best[height<=480]',
            'outtmpl': '%(title)s_480p.%(ext)s',
            'noplaylist': True
        }
    elif choice == "3":
        return {
            'format': 'best[height<=720]',
            'outtmpl': '%(title)s_720p.%(ext)s',
            'noplaylist': True
        }
    elif choice == "4":
        return {
            'format': 'best[height<=1080]',
            'outtmpl': '%(title)s_1080p.%(ext)s',
            'noplaylist': True
        }
    elif choice == "5":
        return {
            'format': 'best[height<=1440]',
            'outtmpl': '%(title)s_2K.%(ext)s',
            'noplaylist': True
        }
    elif choice == "6":
        return {
            'format': 'best[height<=2160]',
            'outtmpl': '%(title)s_4K.%(ext)s',
            'noplaylist': True
        }
    elif choice == "7":
        return {
            'format': 'best',
            'outtmpl': '%(title)s_best.%(ext)s',
            'noplaylist': True
        }
    else:
        print("Geçersiz seçim!")
        return None

def download_video(url, options):
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            print(f"\nİndirme başlatılıyor...")
            ydl.download([url])
            print("İndirme tamamlandı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python download.py <video_url>")
        print("Örnek: python download.py https://www.youtube.com/watch?v=xxxxxxx")
        sys.exit(1)
    
    url = sys.argv[1]
    choice = show_menu()
    options = get_download_options(choice)
    
    if options:
        download_video(url, options)
    else:
        print("Program sonlandırılıyor...")