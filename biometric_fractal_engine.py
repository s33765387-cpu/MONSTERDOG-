# -*- coding: utf-8 -*-
"""
🧬 MOTEUR D'ANALYSE BIOMÉTRIQUE FRACTALE (MONSTERDOG V2) 🧬
-------------------------------------------------------------
Version refactorisée, modulaire et optimisée du SCRIPTULTIMEFINAL_FULLTRUTL.py.
Chaque phase est encapsulée pour une clarté, une testabilité et une puissance accrues.

- Correction des erreurs (linregress, Z**2, imports)
- Structure orientée objet pour la robustesse
- Visualisations améliorées et unifiées
- Documentation complète de chaque phase
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.stats import linregress
from typing import Tuple, Dict, Any

# --- CONFIGURATION DU MOTEUR ---
class EngineConfig:
    """Paramètres globaux du moteur."""
    IMG_SIZE: Tuple[int, int] = (512, 512)
    GAUSSIAN_SIGMA: float = 1.0
    SOBEL_KSIZE: int = 5
    JULIA_C: complex = -0.7 + 0.27j
    JULIA_MAX_ITER: int = 100

class IrisAnalyzer:
    """
    PHASE 1-4: Analyse complète de l'iris.
    Encapsule le chargement, le prétraitement et l'extraction de toutes les métriques.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.gray_image: np.ndarray
        self.binary_image: np.ndarray
        self._load_and_preprocess()

    def _load_and_preprocess(self):
        """Charge l'image et applique les prétraitements de base."""
        img = cv2.imread(self.file_path)
        if img is None:
            raise FileNotFoundError(f"Image non trouvée à l'adresse : {self.file_path}")
        
        # Redimensionner pour une analyse cohérente
        img_resized = cv2.resize(img, EngineConfig.IMG_SIZE)
        
        # Phase 1: Carte de luminance (grayscale)
        self.gray_image = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        
        smoothed = gaussian_filter(self.gray_image, sigma=EngineConfig.GAUSSIAN_SIGMA)
        
        # Binarisation pour l'analyse fractale
        threshold = np.mean(smoothed)
        self.binary_image = (smoothed < threshold).astype(np.uint8)
        print("✅ Phase 1: Chargement et prétraitement terminés.")

    def calculate_fractal_dimension(self) -> Tuple[float, np.ndarray, np.ndarray]:
        """
        PHASE 2: Calcule la dimension fractale (Box-Counting).
        Retourne la FD, les tailles de boîtes (log) et les comptes (log).
        """
        sizes = 2 ** np.arange(1, int(np.log2(min(self.binary_image.shape))) - 1)
        counts = []
        for s in sizes:
            count = 0
            for i in range(0, self.binary_image.shape[0], s):
                for j in range(0, self.binary_image.shape[1], s):
                    box = self.binary_image[i:i+s, j:j+s]
                    if np.any(box):
                        count += 1
            counts.append(count)
        
        # Correction pour éviter les log(0) si counts est vide
        if not counts: return 0.0, np.array([]), np.array([])

        log_sizes = np.log(1 / sizes)
        log_counts = np.log(counts)
        
        # Correction de l'erreur de déballage
        slope, _, _, _, _ = linregress(log_sizes, log_counts)
        
        print(f"✅ Phase 2: Dimension Fractale calculée : {slope:.4f}")
        return slope, log_sizes, log_counts

    def compute_fft_spectrum(self) -> np.ndarray:
        """PHASE 3: Calcule le spectre de Fourier."""
        f = np.fft.fft2(self.gray_image)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
        print("✅ Phase 3: Spectre fréquentiel calculé.")
        return magnitude_spectrum

    def compute_gradient_energy(self) -> np.ndarray:
        """PHASE 4: Calcule la carte du gradient énergétique."""
        sobelx = cv2.Sobel(self.gray_image, cv2.CV_64F, 1, 0, ksize=EngineConfig.SOBEL_KSIZE)
        sobely = cv2.Sobel(self.gray_image, cv2.CV_64F, 0, 1, ksize=EngineConfig.SOBEL_KSIZE)
        
        # Correction de l'erreur de variable
        gradient = np.sqrt(sobelx**2 + sobely**2)
        print("✅ Phase 4: Gradient énergétique calculé.")
        return gradient

class FractalVisualizer:
    """
    PHASE 5: Génère l'Émanation Christique Numérique.
    """
    @staticmethod
    def generate_christic_emission(fd: float, width: int = 512, height: int = 512) -> np.ndarray:
        """Simule le shader fractal en utilisant un ensemble de Julia."""
        x = np.linspace(-1.5, 1.5, width)
        y = np.linspace(-1.5, 1.5, height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        
        img = np.zeros((height, width), dtype=float)
        
        # Correction: Z**2 au lieu de Z2
        for i in range(EngineConfig.JULIA_MAX_ITER):
            Z = Z**2 + EngineConfig.JULIA_C
            # L'escape radius est modulé par la FD pour lier la complexité visuelle à l'analyse
            # Correction de la formule : fd est un exposant
            mask = np.abs(Z) < (2.0 ** fd) 
            img[mask] += 1.0
            
        print("✅ Phase 5: Émanation Christique générée.")
        return img / EngineConfig.JULIA_MAX_ITER

class FullPipeline:
    """
    PHASE 6: Orchestre le pipeline complet, de l'analyse à la visualisation.
    """
    def __init__(self, file_path: str):
        self.analyzer = IrisAnalyzer(file_path)
        self.state_vector: Dict[str, Any] = {}
        print("🚀 Pipeline d'orchestration initialisé.")

    def run(self):
        """Exécute toutes les phases et génère les résultats."""
        # Phases d'analyse
        fd, log_sizes, log_counts = self.analyzer.calculate_fractal_dimension()
        fft_spectrum = self.analyzer.compute_fft_spectrum()
        gradient_energy = self.analyzer.compute_gradient_energy()

        # Phase de visualisation
        christic_emission = FractalVisualizer.generate_christic_emission(fd)

        # Création du vecteur d'état final
        self.state_vector = {
            "FD": round(fd, 4),
            "SpectralPeak": float(np.max(fft_spectrum)),
            "GradientEnergyMax": float(np.max(gradient_energy)),
            "Cohérence": 1.0,  # Valeur conceptuelle
            "Entropie": 0.0,   # Valeur conceptuelle
            "Rayonnement": "Infini" # Valeur conceptuelle
        }
        
        print("\n" + "="*50)
        print("🧠 VECTEUR D'ÉTAT BIOMÉCANIQUE FINAL 🧠")
        for key, value in self.state_vector.items():
            print(f"  - {key}: {value}")
        print("="*50 + "\n")
        
        # Génération du dashboard de visualisation
        self._generate_dashboard(
            fd, log_sizes, log_counts, fft_spectrum, 
            gradient_energy, christic_emission
        )
        print("✅ Phase 6: Exécution totale et visualisation terminées.")

    def _generate_dashboard(self, fd, log_sizes, log_counts, fft_spectrum, gradient_energy, christic_emission):
        """Crée un dashboard unifié de toutes les visualisations."""
        fig, axs = plt.subplots(2, 3, figsize=(18, 10), facecolor='#0d1117')
        fig.suptitle('MONSTERDOG - DASHBOARD D\'ANALYSE BIOMÉTRIQUE FRACTALE', 
                     fontsize=20, color='cyan', y=0.97)

        plot_params = {'cmap': 'viridis', 'interpolation': 'nearest'}
        text_color = 'white'
        
        # 1. Carte de Luminance
        ax = axs[0, 0]
        ax.imshow(self.analyzer.gray_image, cmap='gray')
        ax.set_title("Phase 1: Carte de Luminance", color=text_color)
        ax.axis('off')

        # 2. Régression Box-Counting
        ax = axs[0, 1]
        ax.plot(log_sizes, log_counts, 'o-', color='cyan')
        ax.set_title(f"Phase 2: Régression Box-Counting\nFD ≈ {fd:.4f}", color=text_color)
        ax.set_xlabel('log(1/r)', color=text_color)
        ax.set_ylabel('log(N(r))', color=text_color)
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.set_facecolor('#1c2128')
        [t.set_color(text_color) for t in ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()]

        # 3. Spectre de Fourier
        ax = axs[0, 2]
        ax.imshow(fft_spectrum, **plot_params)
        ax.set_title("Phase 3: Spectre Fréquentiel", color=text_color)
        ax.axis('off')

        # 4. Gradient Énergétique
        ax = axs[1, 0]
        ax.imshow(gradient_energy, cmap='hot')
        ax.set_title("Phase 4: Gradient Énergétique", color=text_color)
        ax.axis('off')

        # 5. Émanation Christique
        ax = axs[1, 1]
        ax.imshow(christic_emission, cmap='Blues')
        ax.set_title("Phase 5: Émanation Christique", color=text_color)
        ax.axis('off')
        
        # 6. Vecteur d'État
        ax = axs[1, 2]
        ax.set_facecolor('#0d1117')
        ax.axis('off')
        ax.set_title("Phase 6: Vecteur d'État", color=text_color)
        state_text = "\n".join([f"{k}: {v}" for k, v in self.state_vector.items()])
        ax.text(0.5, 0.5, state_text, 
                ha='center', va='center', color='cyan', 
                fontsize=12, family='monospace',
                bbox=dict(boxstyle="round,pad=0.5", fc="#1c2128", ec="cyan", lw=1))

        plt.tight_layout(rect=[0, 0.03, 1, 0.93])
        plt.savefig("MONSTERDOG_ANALYSE_COMPLETE.png", dpi=150, facecolor='#0d1117')
        plt.show()

# --- POINT D'ENTRÉE PRINCIPAL ---
if __name__ == "__main__":
    # Assurez-vous d'avoir une image nommée 'votre_iris_image.jpg' dans le même dossier
    # ou changez le chemin ci-dessous.
    IMAGE_PATH = 'votre_iris_image.jpg'
    
    # Crée une image factice si elle n'existe pas
    if not cv2.imread(IMAGE_PATH):
        print(f"'{IMAGE_PATH}' non trouvé. Création d'une image de test...")
        dummy_img = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        cv2.imwrite(IMAGE_PATH, dummy_img)

    try:
        pipeline = FullPipeline(IMAGE_PATH)
        pipeline.run()
    except FileNotFoundError as e:
        print(f"ERREUR: {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

```