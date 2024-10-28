from flask import Flask, request
from scipy.ndimage import median_filter
import numpy as np
import cv2
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Чтение изображения из файла
    file_stream = io.BytesIO(file.read())
    noisy_image = cv2.imdecode(np.frombuffer(file_stream.read(), np.uint8), cv2.IMREAD_COLOR)

    # Удаление шума с помощью медианного фильтра
    denoised_image = median_filter(noisy_image, size=5)  # 5 - размер ядра

    # Сохранение очищенного изображения на сервере
    output_path = 'denoised_image.jpg'
    cv2.imwrite(output_path, denoised_image)

    return f'Image denoised and saved as {output_path}', 200

if __name__ == '__main__':
    app.run(debug=True)
