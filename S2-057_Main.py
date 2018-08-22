import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import base64
import os



def Attack(Target):
    lena = mpimg.imread("S2-057_EXP.png")
    lena.shape
    plt.imshow(lena)
    plt.axis('off')
    plt.show()
    os.rename("EXP.png","S2-057_EXP")
if __name__ == '__main__':
    try:
        Target = input("Please Input A Target Host:")
    except:
        pass
    os.rename("EXP","EXP.png")
    Target = "Joker"
    Attack(Target)
