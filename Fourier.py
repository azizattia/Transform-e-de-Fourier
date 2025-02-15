# Importation des modules pertinents ici. 
# Assurez-vous d'inclure toute autre fonction que vous
# jugez nécessaires ici

import numpy as np
import imageio
import matplotlib.pyplot as plt
# Exercice 1 : Transformée de Fourier
# lire l image
img = imageio.imread('tp2_ex1.tif')

# Faire la transformé de Fourier des images suivante
img_fft = np.fft.fft2(img)
img_fft_shift = np.fft.fftshift(img_fft)
def display_fft(img_fft):
    """Affichage de l'amplitude et de la phase d'une transformée de Fourier
    
    Parameters
    ----------
    img_fft : ndarray
        Transformée de Fourier d'une image
    """
    # afficher l’amplitude de la transformée de Fourier
    plt.subplot(1,2,1)
    plt.imshow(np.log(np.abs(img_fft) + 1e-6), extent=(-0.5, 0.5, -0.5, 0.5))
    plt.title('Amplitude sous echelle logarithmique')

    # afficher la phase de la transformée de Fourier
    plt.subplot(1,2,2)
    plt.imshow(np.angle(img_fft), extent=(-0.5, 0.5, -0.5, 0.5))
    plt.title('Phase')

    plt.show()

# Appeler la fonction display_fft pour visualiser la transformee de Fourier
display_fft(img_fft_shift)
