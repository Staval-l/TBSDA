import cv2
import numpy as np
import requests

def add_gaussian_noise(image):
    mean = 0
    disp = np.var(image)
    sigma = 0.36
    gauss = np.random.normal(mean, np.sqrt(disp/10), image.shape).astype('uint8')
    noisy_image = cv2.add(image, gauss)
    return noisy_image

# Загрузка изображения
image = cv2.imread('images/07_elaine.tif')

# Добавление гауссовского шума
noisy_image = add_gaussian_noise(image)

# Сохранение зашумленного изображения
cv2.imwrite('noisy_image.jpg', noisy_image)

# Отправка изображения на сервер
url = 'http://127.0.0.1:5000/upload'
files = {'file': open('noisy_image.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.text)
