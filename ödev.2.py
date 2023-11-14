import cv2
import numpy as np

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü oku
    ret, frame = cap.read()

    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin HSV aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Kırmızı rengi maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Orijinal görüntüde sadece kırmızı nesneyi göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basılmasını kontrol et
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bağlantıları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
