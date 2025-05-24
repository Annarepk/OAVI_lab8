# OAVI_lab8
_Текстурный анализ и контрастирование изображений_

### Вариант: 46

Была поставлена следующая задача:

### Текстурный анализ и контрастирование
1. Реализовать расчет матрицы NGTDM (Neighborhood Gray Tone Difference Matrix) с параметром d=2.
2. Вычислить текстурные признаки: COS (Coarseness), CON (Contrast), BUS (Busyness).
3. Применить логарифмическое контрастирование к яркостному каналу L в цветовой модели HSL.
4. Сравнить признаки для исходного и контрастированного изображений.
5. Визуализировать результаты.

***

## Функции

Функции для данной задачи находятся в файле `texture.py`.

- `RGBtoHSI(image: Image) -> list`
  > Конвертирует изображение из RGB в HSL цветовое пространство.
  >
  > _ПАРАМЕТРЫ:_  
  > * **image** - Изображение в формате PIL.Image.  
  >
  > _ВОЗВРАЩАЕТ:_  
  > * Матрицу значений HSL.

- `HSItoRGB(hlsData: list) -> Image`
  > Конвертирует данные HSL обратно в RGB.

- `getLuminanceChannel(hlsData: list) -> np.ndarray`
  > Извлекает канал яркости (L) из HSL данных.

- `LogContrast(lChannel: np.ndarray, factor: float) -> np.ndarray`
  > Применяет логарифмическое контрастирование к каналу яркости.

- `NGTDM(lChannel: np.ndarray, d: int) -> np.ndarray`
  > Вычисляет матрицу NGTDM для заданного расстояния d.

- `textureFeatures(ngtdm: np.ndarray) -> tuple`
  > Вычисляет признаки COS, CON, BUS из матрицы NGTDM.

- `histogram(data: np.ndarray, title: str, ax: plt.Axes) -> None`
  > Строит гистограмму яркости.

---

# Работа программы

## Примеры результатов

### Цветок с текстом

#### Оригинальное изображение:
<img src="Pictures/text_flower/text_flower.png" width="250">

#### Результаты обработки:
<table>
  <tr>
    <td><img src="Pictures/text_flower/text_flowerGrayscale.png" width="250"></td>
    <td><img src="Pictures/text_flower/text_flowerContrast.png" width="250"></td>
  </tr>
  <tr>
    <td><img src="Pictures/text_flower/text_flowerHistOrigin.png" width="400"></td>
    <td><img src="Pictures/text_flower/text_flowerHistContrast.png" width="400"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="Pictures/text_flower/text_flowerTextureFeat.png" width="840"></td>
  </tr>
</table>

## Текстурные признаки

| Тип изображения   | COS (грубость) | CON (контраст) | BUS (загруженность) |
|-------------------|----------------|----------------|---------------------|
| Исходное          | 0.0511         | 384.4933       | 18.5865             |
| Контрастированное | 0.0565         | 547.4494       | 16.7147             |

### Текстура

#### Оригинальное изображение:
<img src="Pictures/texture/texture.png" width="250">

#### Результаты обработки:
<table>
  <tr>
    <td><img src="Pictures/texture/textureGrayscale.png" width="250"></td>
    <td><img src="Pictures/texture/textureContrast.png" width="250"></td>
  </tr>
  <tr>
    <td><img src="Pictures/texture/textureHistOrigin.png" width="400"></td>
    <td><img src="Pictures/texture/textureHistContrast.png" width="400"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="Pictures/texture/textureTextureFeat.png" width="840"></td>
  </tr>
</table>

## Текстурные признаки

| Тип изображения   | COS (грубость) | CON (контраст) | BUS (загруженность) |
|-------------------|----------------|----------------|---------------------|
| Исходное          | 0.1381         | 54.3196        | 6.2417              |
| Контрастированное | 0.2224         | 18.9214        | 3.4966              |

### Рентгеновский снимок

#### Оригинальное изображение:
<img src="Pictures/x_ray/x_ray.png" width="250">

#### Результаты обработки:
<table>
  <tr>
    <td><img src="Pictures/x_ray/x_rayGrayscale.png" width="250"></td>
    <td><img src="Pictures/x_ray/x_rayContrast.png" width="250"></td>
  </tr>
  <tr>
    <td><img src="Pictures/x_ray/x_rayHistOrigin.png" width="400"></td>
    <td><img src="Pictures/x_ray/x_rayHistContrast.png" width="400"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="Pictures/x_ray/x_rayTextureFeat.png" width="840"></td>
  </tr>
</table>

## Текстурные признаки

| Тип изображения   | COS (грубость) | CON (контраст) | BUS (загруженность) |
|-------------------|----------------|----------------|---------------------|
| Исходное          | 0.2401         | 15.0656        | 3.1646              |
| Контрастированное | 0.2235         | 20.2464        | 3.4733              |