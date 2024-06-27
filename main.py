import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi
import imageio.v2 as imageio
import os


"""""
use ImageDataset for examples.
For more examples visit:
-Kaggle datasets: https://www.kaggle.com/
"""""
class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RX-TAC Border-Gaussian Analyzer")
        self.root.geometry("800x800")
        self.root.configure(bg='#ADD8E6')  # Color de fondo azul claro

        self.create_widgets()

        self.image = None
        self.image_path = None

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="RX-TAC Border-Gaussian Analyzer", font=("Helvetica", 20, "bold"), bg="#ADD8E6")
        title.pack(pady=20)

        # Buttons
        btn_load = tk.Button(self.root, text="Cargar Imagen", command=self.load_image)
        btn_load.pack(pady=10)

        btn_process = tk.Button(self.root, text="Procesar Imagen", command=self.process_image)
        btn_process.pack(pady=10)

        btn_save = tk.Button(self.root, text="Guardar Imagen con Detección de Bordes", command=self.save_image)
        btn_save.pack(pady=10)

        btn_clear = tk.Button(self.root, text="Limpiar", command=self.clear)
        btn_clear.pack(pady=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.image = imageio.imread(self.image_path)
            messagebox.showinfo("Información", f"Imagen cargada: {os.path.basename(self.image_path)}")

    def process_image(self):
        if self.image is None:
            messagebox.showwarning("Advertencia", "Cargue una imagen primero.")
            return

        def calculate_histogram(image):
            hist, bin_edges = np.histogram(image.flatten(), bins=256, range=(0, 255))
            return hist

        hist = calculate_histogram(self.image)
        plt.figure()
        plt.plot(hist)
        plt.title("Histograma")
        plt.xlabel("Valor de píxel")
        plt.ylabel("Frecuencia")
        plt.show()

        if len(self.image.shape) == 3:
            im_gray = np.dot(self.image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            im_gray = self.image

        weights = np.array([
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1]
        ])

        edges = ndi.convolve(im_gray, weights)
        im_filt = ndi.convolve(im_gray, weights)
        median = ndi.median_filter(im_gray, size=10)
        gaussian = ndi.gaussian_filter(im_gray, sigma=5)

        fig, axes = plt.subplots(1, 3, figsize=(20, 10))

        axes[0].imshow(self.image, cmap='gray', vmin=-150, vmax=150)
        axes[0].set_title('Imagen original')
        axes[0].axis('off')

        axes[1].imshow(im_filt, cmap='gray')
        axes[1].set_title('Imagen filtrada con convolución')
        axes[1].axis('off')

        axes[2].imshow(edges, cmap='seismic', vmin=-150, vmax=150)
        axes[2].set_title('Detección de bordes verticales')
        axes[2].axis('off')

        output_file_name = f"image_analysis_{os.path.basename(self.image_path).replace('.jpg', '')}_Vin_Vmax150.jpg"
        fig.suptitle(output_file_name, fontsize=16)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.colorbar(axes[2].imshow(edges, cmap='seismic', vmin=-150, vmax=150), ax=axes[2])
        plt.show()

        self.processed_image = edges
        self.output_file_name = output_file_name

    def save_image(self):
        if self.image is None:
            messagebox.showwarning("Advertencia", "No hay ninguna imagen procesada para guardar.")
            return

        output_dir = "imageResunts"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        plt.imsave(os.path.join(output_dir, self.output_file_name), self.processed_image, cmap='seismic', vmin=-150, vmax=150)
        messagebox.showinfo("Información", f"Imagen guardada como {self.output_file_name}")

    def clear(self):
        self.image = None
        self.image_path = None
        self.processed_image = None
        self.output_file_name = None
        messagebox.showinfo("Información", "Datos limpiados. Puede cargar una nueva imagen.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
