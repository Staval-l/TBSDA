import cv2
import numpy as np
import requests


def add_gaussian_noise(image):
    mean = 0
    sigma = 0.36
    gauss = np.random.normal(mean, sigma, image.shape).astype('uint8')
    noisy_image = cv2.add(image, gauss)
    return noisy_image


def main():
    image = cv2.imread('images/07_elaine.tif')

    noisy_image = add_gaussian_noise(image)

    cv2.imwrite('noisy_image.jpg', noisy_image)

    url = 'http://127.0.0.1:5000/upload'
    files = {'file': open('noisy_image.jpg', 'rb')}
    response = requests.post(url, files=files)

    print(response.text)


if __name__ == '__main__':
    main()
