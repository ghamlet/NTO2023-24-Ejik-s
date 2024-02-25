import cv2
import numpy as np

# Производим загрузку изображения
image = cv2.imread('C2.jpg')


# # Выделяем необходимый фрагмент: image[y1:y2, x1:x2]
# # cropped_11 = image[120:190, 230:290]
# # cropped_10 = image[120:190, 230:290]
# #cropped_9 = image[120:190, 230:290]

# cropped_8 = image[60:130, 280:360]
# cropped_7 = image[120:190, 230:310]
# cropped_6 = image[70:140, 350:430]
# cropped_5 = image[135:205, 305:385]
# cropped_4 = image[100:170, 450:530]
# cropped_3 = image[185:255, 390:470]
# cropped_2 = image[140:210, 545:625]
# cropped_1 = image[220:290, 495:575]
# # # Показываем обрезанное изображение
# cv2.imshow('Обрезанное8', cropped_8)
# cv2.imshow('Обрезанное7', cropped_7)
# cv2.imshow('Обрезанное6', cropped_6)
# cv2.imshow('Обрезанное5', cropped_5)
# cv2.imshow('Обрезанное4', cropped_4)
# cv2.imshow('Обрезанное3', cropped_3)
# cv2.imshow('Обрезанное2', cropped_2)
# cv2.imshow('Обрезанное1', cropped_1)

red = cv2.inRange(image, (143,128,151),(255,255,255))
red_sum = np.sum(red)

orange = cv2.inRange(image, (137,57,168),(255,255,255))
orange_sum=np.sum(orange)

green = cv2.inRange(cropped_1, (0,0,164),(255, 255, 255))
green_sum =np.sum(green)

grey = cv2.inRange(cropped_1, (0, 38, 95),(255, 99, 255 ))
grey_sum = np.sum(grey)

print(red_sum)
print(orange_sum)
print(green_sum)
print(grey_sum)


if red_sum > orange_sum and red_sum > green_sum and red_sum > grey_sum:
    print('Oгнетушитель')
if green_sum > orange_sum and green_sum > grey_sum and green_sum > red_sum:
    print('Aптечка')
if orange_sum > green_sum and orange_sum > grey_sum and orange_sum > red_sum:
    print('Ремонт')
if grey_sum > orange_sum and grey_sum > green_sum and grey_sum > red_sum:
    print('Машина')

im_v = cv2.vconcat([cropped_7, cropped_5, cropped_3, cropped_1])
cv2.imshow('im.v', im_v)
im_v2 = cv2.vconcat([cropped_8, cropped_6, cropped_4, cropped_2])
cv2.imshow('im.v2', im_v2)
im_h = cv2.hconcat([im_v, im_v2])
cv2.imshow('im.h', im_h)
cv2.waitKey(0)
cv2.imwrite('cropped.jpg', cropped_7)