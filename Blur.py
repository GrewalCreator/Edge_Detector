import numpy as np
from PIL import Image

class Blur:
    def __init__(self, img, kernel):
        self.img = img
        self.img_array = np.array(img, dtype=int)
        self.height, self.width = self.img.shape[:2]
        self.new_image = Image.new(mode="RGB", size=(self.width, self.height), 
                                       color=(255, 255, 255))
        self.new_image_array = np.array(self.new_image)
        
        self.kernel_size = (2 * kernel + 1)
        self.kernel_area = (2 * kernel + 1) ** 2
    
    def BoxBlur(self):
        
        for i in range(self.height):
            for k in range(self.width):
                pixel_sum = 0
                for x in range(i - self.kernel_size // 2, i + self.kernel_size // 2 + 1):
                    for y in range(k - self.kernel_size // 2, k + self.kernel_size // 2 + 1):
                        pixel_sum += self.img_array[self.bound_i(x)][self.bound_k(y)]
                self.new_image_array[i][k] = pixel_sum // self.kernel_area

        return self.new_image_array


    def GaussianBlur(self):
        pass

    def bound_i(self, value):
        return max(0, min(value, self.height - 1))

    def bound_k(self, value):
        return max(0, min(value, self.width - 1))