import sys
from PIL import Image
import os

def hex_para_rgb(cor_hex):
    cor_hex = cor_hex.strip().lstrip('#')
    return tuple(int(cor_hex[i:i+2], 16) for i in (0, 2, 4))

def carregar_paleta(caminho_paleta):
    with open(caminho_paleta, 'r') as arquivo:
        return [hex_para_rgb(linha) for linha in arquivo if linha.strip()]

def cor_mais_proxima(pixel, paleta):
    return min(paleta, key=lambda cor: sum((a - b) ** 2 for a, b in zip(pixel, cor)))

def converter_imagem(caminho_imagem, caminho_paleta):
    paleta = carregar_paleta(caminho_paleta)
    imagem = Image.open(caminho_imagem).convert('RGB')
    pixels = imagem.load()

    for y in range(imagem.height):
        for x in range(imagem.width):
            cor_original = pixels[x, y]
            pixels[x, y] = cor_mais_proxima(cor_original, paleta)

    nome_arquivo = os.path.splitext(os.path.basename(caminho_imagem))[0]
    caminho_saida = os.path.join(
        os.path.dirname(caminho_imagem),
        f"{nome_arquivo}_convertido.png"
    )

    imagem.save(caminho_saida)
    print(f"Imagem convertida salva em: {caminho_saida}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python converter_paleta.py <caminho_imagem> <caminho_paleta.txt>")
    else:
        _, caminho_imagem, caminho_paleta = sys.argv
        converter_imagem(caminho_imagem, caminho_paleta)