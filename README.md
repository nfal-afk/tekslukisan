# 🧠 Lukisan Kode (Foto ke ASCII Art)

project ini bisa ubah foto jadi lukisan teks berwarna di termux.  
langsung aja gas dari awal sampe jadi, tanpa ribet.

---

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install python libjpeg-turbo libpng libwebp unzip -y
pip install --no-cache-dir pillow colorama rich
cd /sdcard/Download
python foto.py
