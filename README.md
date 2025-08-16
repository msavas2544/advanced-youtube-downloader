# 🎬 Advanced YouTube Downloader

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
[![GitHub stars](https://img.shields.io/github/stars/msavas2544/advanced-youtube-downloader.svg)](https://github.com/msavas2544/advanced-youtube-downloader/stargazers)

**A powerful and user-friendly video/audio downloader that supports YouTube and many other platforms with multiple quality options and batch downloading capabilities.**

[🚀 Quick Start](#-quick-start) • [📖 Features](#-features) • [💻 Installation](#-installation) • [📋 Usage](#-usage) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🎵 **Audio & Video**
- **High-Quality MP3** extraction (192kbps)
- **Multiple Video Qualities**: 480p → 4K
- **YouTube Shorts** full support
- **All YouTube formats** compatible

</td>
<td width="50%">

### 🚀 **Advanced Features**
- **📊 Real-time Progress** with file size
- **📋 Batch Download** multiple videos
- **🚫 Smart Playlist Prevention**
- **� Video Preview** before download

</td>
</tr>
</table>

## 🎯 Quality Options

| Option | Quality | Description |
|--------|---------|-------------|
| 🎵 **1** | Audio Only | MP3 - 192kbps |
| 📺 **2** | 480p | Standard Definition |
| 🎬 **3** | 720p | High Definition |
| 🎭 **4** | 1080p | Full HD |
| 🎪 **5** | 2K | 1440p Quality |
| 🎨 **6** | 4K | 2160p Ultra HD |
| ⭐ **7** | Best | Highest Available |

## 🚀 Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/msavas2544/advanced-youtube-downloader.git
cd advanced-youtube-downloader

# 2️⃣ Create virtual environment
python -m venv venv

# 3️⃣ Activate environment
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Start downloading!
python advanced_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

## 📖 Usage Examples

### 🎥 Single Video Download
```bash
python advanced_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
**Output Preview:**
```
📹 Video bilgileri alınıyor...
📌 Başlık: Rick Astley - Never Gonna Give You Up
⏱️ Süre: 3:33
👤 Kanal: Rick Astley

🚀 İndirme başlatılıyor...
İndiriliyor... %100.0 - 8.5MB/8.5MB
✅ Tamamlandı: Rick Astley - Never Gonna Give You Up_720p.mp4
```

### 📱 YouTube Shorts
```bash
python advanced_downloader.py "https://www.youtube.com/shorts/SHORT_ID"
```

### 📋 Batch Download
```bash
python advanced_downloader.py bulk
```
Then enter URLs one by one:
```
=== Toplu İndirme ===
URL'leri tek tek girin (boş satır ile bitirin):
URL: https://www.youtube.com/watch?v=VIDEO1
URL: https://www.youtube.com/watch?v=VIDEO2
URL: [press Enter]

📋 2 video bulundu
Kalite seçin (1-7): 3

🎯 Video 1/2 indiriliyor...
🎯 Video 2/2 indiriliyor...
🎉 Toplu indirme tamamlandı! 2 video işlendi.
```

## 💻 Installation

<details>
<summary><b>🪟 Windows Installation</b></summary>

```powershell
# Download the repository
git clone https://github.com/msavas2544/advanced-youtube-downloader.git
cd advanced-youtube-downloader

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Optional: Install FFmpeg for audio conversion
# Download from: https://ffmpeg.org/download.html
```

</details>

<details>
<summary><b>🐧 Linux Installation</b></summary>

```bash
# Download the repository
git clone https://github.com/msavas2544/advanced-youtube-downloader.git
cd advanced-youtube-downloader

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install FFmpeg
sudo apt update && sudo apt install ffmpeg  # Ubuntu/Debian
# sudo yum install ffmpeg  # CentOS/RHEL
```

</details>

<details>
<summary><b>🍎 macOS Installation</b></summary>

```bash
# Download the repository
git clone https://github.com/msavas2544/advanced-youtube-downloader.git
cd advanced-youtube-downloader

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install FFmpeg
brew install ffmpeg
```

</details>

## � Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| **Python** | 3.10+ | Core runtime |
| **yt-dlp** | Latest | Video downloading |
| **tqdm** | Latest | Progress bars |
| **FFmpeg** | Latest | Audio conversion |

## 📁 Output Files

```
📂 download folder/
├── 🎵 audio_file.mp3
├── 🎬 video_title_720p.mp4
├── 🎭 another_video_1080p.mp4
└── 🎪 movie_4K.mp4
```

## 🛡️ Safety Features

- ✅ **Playlist Prevention** - Only downloads single videos
- ✅ **Error Handling** - Graceful error recovery
- ✅ **Progress Tracking** - Never lose track of downloads
- ✅ **Quality Validation** - Ensures requested quality exists

## ⚖️ Legal Notice

> [!WARNING]
> - Only download content you have legal rights to download
> - Respect copyright laws and content creators' rights
> - This tool is intended for personal use only
> - Be aware of your local laws regarding media downloading

## 🤝 Contributing

We welcome contributions! Here's how you can help:

<details>
<summary><b>🔧 How to Contribute</b></summary>

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### 🎯 Areas for Contribution
- 🌐 GUI interface development
- 🔄 Resume/pause functionality
- 📱 Mobile app version
- 🌍 Multi-language support
- 🎨 Better progress visualization

</details>

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

<table>
<tr>
<td align="center" width="33%">
<img src="https://avatars.githubusercontent.com/u/79589310?s=200&v=4" width="80px" alt="yt-dlp"/><br>
<b><a href="https://github.com/yt-dlp/yt-dlp">yt-dlp</a></b><br>
<sub>Core downloading engine</sub>
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/tqdm/tqdm/master/images/logo.gif" width="80px" alt="tqdm"/><br>
<b><a href="https://github.com/tqdm/tqdm">tqdm</a></b><br>
<sub>Progress bar library</sub>
</td>
<td align="center" width="33%">
<img src="https://ffmpeg.org/ffmpeg-logo.png" width="80px" alt="FFmpeg"/><br>
<b><a href="https://ffmpeg.org/">FFmpeg</a></b><br>
<sub>Media processing</sub>
</td>
</tr>
</table>

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/msavas2544/advanced-youtube-downloader)
![GitHub last commit](https://img.shields.io/github/last-commit/msavas2544/advanced-youtube-downloader)
![GitHub issues](https://img.shields.io/github/issues/msavas2544/advanced-youtube-downloader)
![GitHub pull requests](https://img.shields.io/github/issues-pr/msavas2544/advanced-youtube-downloader)

## 📞 Support

<div align="center">

**Need help?** 

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github)](https://github.com/msavas2544/advanced-youtube-downloader/issues)
[![GitHub Discussions](https://img.shields.io/badge/GitHub-Discussions-blue?style=for-the-badge&logo=github)](https://github.com/msavas2544/advanced-youtube-downloader/discussions)

</div>

---

<div align="center">

⭐ **Found this useful? Give it a star!** ⭐

**Made with ❤️ by [msavas2544](https://github.com/msavas2544)**

</div>
