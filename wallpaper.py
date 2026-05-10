import os 
import subprocess
import datetime  # Adicionado (estava faltando)

# Configurando os Wallpapers
wallpapers = {
    "madrugada": "/home/dias/Imagens/madrugada.png",
    "manha":     "/home/dias/Imagens/manha.png",
    "tarde":     "/home/dias/Imagens/tarde.png",
    "noite":     "/home/dias/Imagens/noite.jpg"
}

def get_periodo():
    hora = datetime.datetime.now().hour
    if 0 <= hora < 6: return "madrugada"
    if 6 <= hora < 12: return "manha"
    if 12 <= hora < 18: return "tarde"
    return "noite"

def set_wallpaper():
    periodo = get_periodo() # Corrigido de 'priodo' para 'periodo'
    img = wallpapers[periodo]

    # Verifica se a imagem realmente existe antes de tentar mudar
    if os.path.exists(img):
        # Comando do swww com transição suave
        subprocess.run([
            "swww", "img", img,
            "--transition-type", "outer",
            "--transition-step", "90",
            "--transition-fps", "60"
        ])
        
        # Cria o arquivo no tmp para confirmar que funcionou
        with open("/tmp/waybar_wallpaper_periodo", "w") as f:
            f.write(periodo)
    else:
        print(f"Erro: Imagem não encontrada em {img}")

if __name__ == "__main__":
    set_wallpaper()
