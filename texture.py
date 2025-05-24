from PIL import Image
import numpy as np
from colorsys import rgb_to_hls, hls_to_rgb


def RGBtoHSI(image):
    hlsData = []
    for y in range(image.height):
        row = []
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))[:3]
            h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)
            row.append((h, l, s))
        hlsData.append(row)
    return hlsData


def HSItoRGB(hlsData):
    width = len(hlsData[0])
    height = len(hlsData)
    rgbImage = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            h, l, s = hlsData[y][x]
            r, g, b = hls_to_rgb(h, l, s)
            rgbImage.putpixel((x, y), (int(r * 255), int(g * 255), int(b * 255)))

    return rgbImage


def getLuminanceChannel(hlsData):
    return np.array([[pixel[1] for pixel in row] for row in hlsData])


def LogContrast(lChannel, factor=1.0):
    # Нормализуем значения яркости и добавляем небольшое значение, чтобы избежать log(0)
    normalized = lChannel / np.max(lChannel)
    normalized = np.clip(normalized, 1e-10, 1.0)

    # Применяем логарифмическое преобразование
    logTransformed = np.log1p(normalized * factor) / np.log1p(factor)

    return logTransformed


def NGTDM(lChannel, d=2):
    height, width = lChannel.shape
    ngtdm = np.zeros_like(lChannel)

    # Квантование яркости до 256 уровней
    quantized = np.floor(lChannel * 255).astype(int)

    for y in range(height):
        for x in range(width):
            currentVal = quantized[y, x]
            neighborhood = []

            # Собираем соседей на расстоянии d
            for dy in range(-d, d + 1):
                for dx in range(-d, d + 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width and (dy != 0 or dx != 0):
                        neighborhood.append(quantized[ny, nx])

            if neighborhood:
                avgNeighbor = np.mean(neighborhood)
                ngtdm[y, x] = abs(currentVal - avgNeighbor)
            else:
                ngtdm[y, x] = 0

    return ngtdm


def textureFeatures(ngtdm):
    flattened = ngtdm.flatten()
    nonZero = flattened[flattened > 0]

    if len(nonZero) == 0:
        return 0, 0, 0  # Если все нули

    # COS (Coarseness)
    cos = 1 / (1 + np.mean(nonZero))

    # CON (Contrast)
    con = np.var(nonZero)

    # BUS (Busyness)
    bus = np.sum(nonZero) / len(nonZero)

    return cos, con, bus


def histogram(data, title, ax):
    ax.hist(data.flatten(), bins=256, range=(0, 1), color='gray')
    ax.set_title(title)
    ax.set_xlabel('Яркость')
    ax.set_ylabel('Частота')