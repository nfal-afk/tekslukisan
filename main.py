import os, time, random
from PIL import Image
from colorama import init
from rich.console import Console

init(autoreset=True)
console = Console()

# === PENGATURAN ===
IMAGE_PATH = "a.jpg"
WIDTH = 90
DELAY = 0.0100
CHARS = list(" .:-=+*#%@")  # karakter dari gelap ke terang
CODE_WORDS = [
    "import", "def", "return", "if", "for", "while", "try", "except",
    "class", "pass", "break", "continue", "from", "as", "in", "with",
    "print", "range", "len", "data", "process", "file", "open", "read"
]

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def resize_image(img, new_width=WIDTH):
    w, h = img.size
    aspect = h / w / 1.65
    new_height = int(new_width * aspect)
    return img.resize((new_width, new_height))

def pixel_to_char(r, g, b):
    brightness = (0.299 * r + 0.587 * g + 0.114 * b)
    char = CHARS[int(brightness / 256 * len(CHARS))]
    return char

def generate_ascii_paint(image_path):
    os.system("cls" if os.name == "nt" else "clear")
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        console.print(f"[bold red]❌ File '{image_path}' tidak ditemukan![/bold red]")
        return

    img = resize_image(img)
    pixels = img.load()

    console.print("\n[bold cyan]🧠 Melukis ulang foto dengan baris kode...[/bold cyan]\n")

    for y in range(img.height):
        line = ""
        for x in range(img.width):
            r, g, b = pixels[x, y]
            color = rgb_to_hex(r, g, b)
            word = random.choice(CODE_WORDS)
            char = pixel_to_char(r, g, b)
            # kombinasi karakter dan kata biar tetap "kode"
            piece = f"[{color}]{char if random.random() < 0.5 else word[0]}[/{color}]"
            line += piece
        console.print(line)
        time.sleep(DELAY * 5)

    console.print("\n[bold green]✅ Lukisan selesai![/bold green]\n")

if __name__ == "__main__":
    generate_ascii_paint(IMAGE_PATH)
