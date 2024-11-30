import cv2
import numpy as np

# Cargar la imagen original
image_Original = cv2.imread(r"BilateralFilter_PabloSosa\Esencia.jpg")

# Validar si la imagen se cargó correctamente
if image_Original is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar filtro bilateral
image_BilateralBlur = cv2.bilateralFilter(image_Original, 100, 100, 75)

# Comparar imágenes lado a lado
image_combined = np.hstack((image_Original, image_BilateralBlur))

# Mostrar las imágenes
cv2.imshow("Original vs Bilateral Filter", image_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la imagen resultante
#cv2.imwrite("cat_1_bilateral.jpg", image_BilateralBlur)