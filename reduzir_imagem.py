import sys
import os
from PIL import Image

def reduzir_imagem(input_path, pixel_width, pixel_height, output_path=None):
    img = Image.open(input_path)
    largura, altura = img.size
    novo_tamanho = (largura // pixel_width, altura // pixel_height)
    img_reduzida = img.resize(novo_tamanho, resample=Image.NEAREST)

    if not output_path:
        nome_base, ext = os.path.splitext(input_path)
        output_path = f"{nome_base}_reduzido{ext}"

    img_reduzida.save(output_path)
    print(f"Imagem salva em: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or "x" not in sys.argv[2]:
        print("Uso correto:")
        print("python reduzir_img.py <imagem> <larguraxaltura>")
        print("Exemplo:")
        print("python reduzir_img.py imagem.png 9x9")
        sys.exit(1)

    imagem = sys.argv[1]
    try:
        largura_px, altura_px = map(int, sys.argv[2].lower().split("x"))
    except ValueError:
        print("Erro: tamanho do pixel deve estar no formato LARGURAxALTURA, ex: 9x9")
        sys.exit(1)

    reduzir_imagem(imagem, largura_px, altura_px)