import cv2
import matplotlib.pyplot as plt 

imagen = cv2.imread(r"HistrogramEqualization_MiltonCruz\19.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

imagen_eqlzd = cv2.equalizeHist(imagen)

# Calcular el histograma de la imagen original
histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])

# Calcular el histograma de la imagen ecualizada
histograma2 = cv2.calcHist([imagen_eqlzd], [0], None, [256], [0, 256])

plt.figure(0)
plt.title("Imagen original")
plt.imshow(imagen, cmap="gray")  # cmap="gray" para imágenes en escala de grises
plt.axis("off")

plt.figure(1)
plt.title("Imagen Ecualizada")
plt.imshow(imagen_eqlzd, cmap="gray")
plt.axis("off")

plt.figure(2)
plt.title("Histograma de la imagen original")
plt.xlabel("Intensidad de píxeles")
plt.ylabel("Número de píxeles")
plt.plot(histograma)
plt.xlim([0, 256])  # Limitar el eje X
plt.grid()

plt.figure(3)
plt.title("Histograma de la imagen ecualizada")
plt.xlabel("Intensidad de píxeles")
plt.ylabel("Número de píxeles")
plt.plot(histograma2)
plt.xlim([0, 256])  # Limitar el eje X
plt.grid()

# Mostrar las figuras
plt.show()



