"""
Module d'Analyse Scientifique d'Iris
Basé sur le code de la Phase 1 du Créateur Samuel Cloutier.
Intègre le calcul de la dimension fractale et d'autres métriques.
"""
import numpy as np
import cv2
from scipy.stats import linregress
from scipy.ndimage import gaussian_filter

class IrisAnalyzer:
    """Encapsule les méthodes d'analyse d'image d'iris."""

    def preprocess_image(self, img_array: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Charge et prétraite une image pour l'analyse."""
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        else:
            gray = img_array
        
        smoothed = gaussian_filter(gray, sigma=1)
        # Utiliser un seuillage adaptatif pour une meilleure binarisation
        binary = cv2.adaptiveThreshold(smoothed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY_INV, 11, 2)
        binary = (binary / 255).astype(int)
        return gray, binary

    def box_counting_dimension(self, binary_img: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
        """Calcule la dimension fractale via la méthode Box-Counting."""
        # Limite la taille pour la performance
        max_dim = min(binary_img.shape)
        max_power = int(np.log2(max_dim))
        sizes = 2**np.arange(1, max_power)
        
        counts = []
        for s in sizes:
            # Optimisation: utiliser np.add.reduceat pour compter plus vite
            count = np.sum(np.add.reduceat(np.add.reduceat(binary_img, 
                np.arange(0, binary_img.shape[0], s), axis=0), 
                np.arange(0, binary_img.shape[1], s), axis=1) > 0)
            counts.append(count)
        
        # Filtrer les comptes nuls qui peuvent fausser la régression
        valid_indices = [i for i, c in enumerate(counts) if c > 0]
        if len(valid_indices) < 2:
            return 0.0, np.array([]), np.array([])
            
        valid_counts = np.array(counts)[valid_indices]
        valid_sizes = sizes[valid_indices]

        log_sizes = np.log(valid_sizes)
        log_counts = np.log(valid_counts)
        
        slope, _, _, _, _ = linregress(log_sizes, log_counts)
        return -slope, valid_sizes, valid_counts

    def compute_fft(self, gray_img: np.ndarray) -> np.ndarray:
        """Calcule le spectre de Fourier 2D."""
        f = np.fft.fft2(gray_img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
        return magnitude_spectrum

    def compute_gradient_energy(self, gray_img: np.ndarray) -> np.ndarray:
        """Calcule la carte d'énergie des gradients."""
        sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)
        gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
        return gradient_magnitude