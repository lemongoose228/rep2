import numpy as np
import matplotlib.pyplot as plt

#считаем углы внешние внутренние для определения количества объектов
extern_mask = ([[[0, 0], [0, 1]],
                [[0, 0], [1, 0]],
                [[0, 1], [0, 0]],
                [[1, 0], [0, 0]]])

#меняем 0 на 1 и 1 на 0
intern_mask = np.logical_not(extern_mask).astype("int") #делаем true и falce 1 и 0

cross_mask = np.array([[[0, 1], [1, 0]],
                      [[1, 0], [0, 1]]])

def match(a, masks):
    for mask in masks:
        if np.all(a==mask):
            return True
    return False

def coun_objects(B): #бинарное изображение
    intern = 0
    extern = 0
    for y in range(0, B.shape[0]-1):
        for x in range(0, B.shape[1] - 1):
            sub = B[y:y+2, x:x+2] #Совмещаем по левому верхнему углу
            if match(sub, extern_mask):
                extern += 1
            if match(sub, intern_mask):
                intern += 1
            if match(sub, cross_mask):
                extern += 2
    return (extern - intern)/4


image = np.load("cex2.npy.txt")
#print(coun_objects(image))
print(coun_objects(image[:, :, 0])+
      coun_objects(image[:, :, 1])+
      coun_objects(image[:, :, 2]))

plt.subplot(141)
plt.imshow(image[:, :, 0])
plt.subplot(142)
plt.imshow(image[:, :, 1])
plt.subplot(143)
plt.imshow(image[:, :, 2])
plt.subplot(144)
plt.imshow(image)
plt.show()