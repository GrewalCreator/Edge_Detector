import cv2
import numpy as np
from PIL import Image
import PIL

class Blur:
    def __init__(self, img):
        self.img = img
        self.img_array = np.array(img, dtype=int)
        self.height, self.width = self.img.shape[:2]
        self.new_image = PIL.Image.new(mode="RGB", size=(self.width, self.height), 
                                       color=(255, 255, 255))
        self.new_image_array = np.array(self.new_image)
        self.total_pixels = self.width * self.height
    
    def BoxBlur(self):
        print(self.img_array)
    
        for i in range(self.height):
            for k in range(self.width):
                pixel_sum = (
                    self.img_array[self.bound_i(i-1)][self.bound_k(k - 1)] + 
                    self.img_array[self.bound_i(i)][self.bound_k(k-1)] +
                    self.img_array[self.bound_i(i + 1)][self.bound_k(k - 1)] +
                    self.img_array[self.bound_i(i - 1)][self.bound_k(k)] +
                    self.img_array[self.bound_i(i)][self.bound_k(k)] +
                    self.img_array[self.bound_i(i + 1)][self.bound_k(k)] +
                    self.img_array[self.bound_i(i - 1)][self.bound_k(k + 1)] +
                    self.img_array[self.bound_i(i)][self.bound_k(k + 1)] +
                    self.img_array[self.bound_i(i + 1)][self.bound_k(k + 1)]
                    )
                self.new_image_array[i][k] = pixel_sum // 9

        return self.new_image_array


    def GaussianBlur(self):
        pass

    def bound_i(self, value):
        return max(0, min(value, self.height - 1))

    def bound_k(self, value):
        return max(0, min(value, self.width - 1))