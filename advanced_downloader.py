import sys
import yt_dlp

def show_menu():
    print("\n=== Gelişmiş Video/Ses İndirme Aracı ===")
    print("1. Sadece ses (MP3)")
    print("2. 480p video")
    print("3. 720p video")
    print("4. 1080p video")
    print("5. 2K video (1440p)")
    print("6. 4K video (2160p)")
    print("7. En yüksek kalite")
    print("8. Toplu indirme (URL listesi)")
    return input("Seçiminizi yapın (1-8): ")

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes', 0)
        downloaded = d.get('downloaded_bytes', 0)
        if total > 0:
            percent = (downloaded / total) * 100
            print(f"\rİndiriliyor... %{percent:.1f} - {downloaded//1024//1024:.1f}MB/{total//1024//1024:.1f}MB", end='')
    elif d['status'] == 'finished':
        print(f"\n✅ Tamamlandı: {d['filename']}")

def get_video_info(url):
    """Video bilgilerini al"""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Bilinmeyen')
            duration = info.get('duration', 0)
            uploader = info.get('uploader', 'Bilinmeyen')
            
            # Süreyi dakika:saniye formatına çevir
            minutes = duration // 60
            seconds = duration % 60
            duration_str = f"{minutes}:{seconds:02d}"
            
            return {
                'title': title,
                'duration': duration_str,
                'uploader': uploader
            }
    except Exception as e:
        return {'title': 'Bilgi alınamadı', 'duration': '00:00', 'uploader': 'Bilinmeyen'}

def get_download_options(choice):
    base_options = {
        'noplaylist': True,
        'progress_hooks': [progress_hook],
        'ignoreerrors': True
    }
    
    if choice == "1":
        base_options.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s'
        })
    elif choice == "2":
        base_options.update({
            'format': 'best[height<=480]',
            'outtmpl': '%(title)s_480p.%(ext)s'
        })
    elif choice == "3":
        base_options.update({
            'format': 'best[height<=720]',
            'outtmpl': '%(title)s_720p.%(ext)s'
        })
    elif choice == "4":
        base_options.update({
            'format': 'best[height<=1080]',
            'outtmpl': '%(title)s_1080p.%(ext)s'
        })
    elif choice == "5":
        base_options.update({
            'format': 'best[height<=1440]',
            'outtmpl': '%(title)s_2K.%(ext)s'
        })
    elif choice == "6":
        base_options.update({
            'format': 'best[height<=2160]',
            'outtmpl': '%(title)s_4K.%(ext)s'
        })
    elif choice == "7":
        base_options.update({
            'format': 'best',
            'outtmpl': '%(title)s_best.%(ext)s'
        })
    elif choice == "8":
        return "bulk_download"
    else:
        print("Geçersiz seçim!")
        return None
    
    return base_options

def download_single_video(url, options):
    """Tek video indir"""
    try:
        print(f"\n📹 Video bilgileri alınıyor...")
        info = get_video_info(url)
        print(f"📌 Başlık: {info['title']}")
        print(f"⏱️ Süre: {info['duration']}")
        print(f"👤 Kanal: {info['uploader']}")
        
        with yt_dlp.YoutubeDL(options) as ydl:
            print(f"\n🚀 İndirme başlatılıyor...")
            ydl.download([url])
            
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")

def bulk_download():
    """Toplu indirme"""
    print("\n=== Toplu İndirme ===")
    print("URL'leri tek tek girin (boş satır ile bitirin):")
    
    urls = []
    while True:
        url = input("URL: ").strip()
        if not url:
            break
        urls.append(url)
    
    if not urls:
        print("❌ Hiç URL girilmedi!")
        return
    
    print(f"\n📋 {len(urls)} video bulundu")
    
    # Kalite seçimi
    quality_choice = input("Kalite seçin (1-7): ")
    options = get_download_options(quality_choice)
    
    if not options or options == "bulk_download":
        print("❌ Geçersiz kalite seçimi!")
        return
    
    # Tüm videoları indir
    for i, url in enumerate(urls, 1):
        print(f"\n🎯 Video {i}/{len(urls)} indiriliyor...")
        download_single_video(url, options)
    
    print(f"\n🎉 Toplu indirme tamamlandı! {len(urls)} video işlendi.")

def download_video(url, options):
    """Ana indirme fonksiyonu"""
    if options == "bulk_download":
        bulk_download()
    else:
        download_single_video(url, options)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python advanced_downloader.py <video_url>")
        print("Toplu indirme için: python advanced_downloader.py bulk")
        print("Örnek: python advanced_downloader.py https://www.youtube.com/watch?v=xxxxxxx")
        sys.exit(1)
    
    url = sys.argv[1]
    
    if url.lower() == "bulk":
        # Toplu indirme modu
        choice = "8"
        options = get_download_options(choice)
        download_video("", options)
    else:
        # Tek video modu
        choice = show_menu()
        options = get_download_options(choice)
        
        if options:
            download_video(url, options)
        else:
            print("Program sonlandırılıyor...")
