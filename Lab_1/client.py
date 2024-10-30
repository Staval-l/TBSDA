import cv2
import numpy as np
import requests


# def add_gaussian_noise(image):
#     mean = 0
#     sigma = 0.36
#     gauss = np.random.normal(mean, sigma, image.shape).astype('uint8')
#     noisy_image = cv2.add(image, gauss)
#     return noisy_image


def add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = np.copy(image)
    num_salt = np.ceil(salt_prob * image.size)
    coordinates = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coordinates[0], coordinates[1], :] = 1

    num_pepper = np.ceil(pepper_prob * image.size)
    coordinates = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coordinates[0], coordinates[1], :] = 0

    return noisy_image


def main():
    image = cv2.imread('images/07_elaine.tif')

    noisy_image = add_salt_and_pepper_noise(image)

    cv2.imwrite('noisy_image.jpg', noisy_image)

    url = 'http://127.0.0.1:5000/upload'
    files = {'file': open('noisy_image.jpg', 'rb')}
    response = requests.post(url, files=files)

    print(response.text)


if __name__ == '__main__':
    main()
