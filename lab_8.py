from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
from texture import RGBtoHSI, getLuminanceChannel, NGTDM, textureFeatures, LogContrast, HSItoRGB, histogram

images = ['text_flower', 'texture', 'x_ray']

for name in images:
    with Image.open(f"Pictures/{name}/{name}.png") as img:
        img = img.convert('RGB')

        hlsData = RGBtoHSI(img)
        lChannel = getLuminanceChannel(hlsData)

        ngtdmOriginal = NGTDM(lChannel, d=2)
        print(f"The NGTDM matrix for image {name}.png is calculated...")
        cosOrig, conOrig, busOrig = textureFeatures(ngtdmOriginal)
        print(f"The features for image {name}.png is counted...\n")

        lChannelContrasted = LogContrast(lChannel, factor=10)

        contrastedHlsData = [[(h, lChannelContrasted[y, x], s) for x, (h, l, s) in enumerate(row)]
                             for y, row in enumerate(hlsData)]

        contrastedImage = HSItoRGB(contrastedHlsData)

        ngtdmContrasted = NGTDM(lChannelContrasted, d=2)
        cosContr, conContr, busContr = textureFeatures(ngtdmContrasted)

        ImageOps.grayscale(img).save(f"Pictures/{name}/{name}Grayscale.png")
        contrastedImage.save(f"Pictures/{name}/{name}Contrast.png")


        # Гистограммы
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        histogram(lChannel, 'Гистограмма яркости (исходная)', ax1)
        fig1.savefig(f"Pictures/{name}/{name}HistOrigin.png", bbox_inches='tight', dpi=150)
        plt.close(fig1)

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        histogram(lChannelContrasted, 'Гистограмма яркости (контрастированная)', ax2)
        fig2.savefig(f"Pictures/{name}/{name}HistContrast.png", bbox_inches='tight', dpi=150)
        plt.close(fig2)

        # NGTDM визуализация (столбчатая диаграмма)
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        x = np.arange(3)
        width = 0.35
        ax3.bar(x - width / 2, [cosOrig, conOrig, busOrig], width, label='Исходное')
        ax3.bar(x + width / 2, [cosContr, conContr, busContr], width, label='Контрастированное', alpha=0.7)
        ax3.set_xticks(x)
        ax3.set_xticklabels(['COS', 'CON', 'BUS'])
        ax3.set_title('Текстурные признаки NGTDM')
        ax3.legend()
        fig3.savefig(f"Pictures/{name}/{name}TextureFeat.png", bbox_inches='tight', dpi=150)
        plt.close(fig3)

        with open(f"Pictures/{name}/{name}Features.txt", 'w', encoding='utf-8') as file:
            print(f"Текстурные признаки (исходное изображение {name}.png):", file=file)
            print(f"COS (Coarseness): {cosOrig:.4f}", file=file)
            print(f"CON (Contrast): {conOrig:.4f}", file=file)
            print(f"BUS (Busyness): {busOrig:.4f}\n", file=file)

            print(f"Текстурные признаки (контрастированное изображение {name}.png):", file=file)
            print(f"COS (Coarseness): {cosContr:.4f}", file=file)
            print(f"CON (Contrast): {conContr:.4f}", file=file)
            print(f"BUS (Busyness): {busContr:.4f}", file=file)

