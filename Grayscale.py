# === Schritt 0: Bibliotheken importieren ===
# Wir benötigen wieder die üblichen Bibliotheken.

import numpy as np  # NumPy ist essenziell, da es uns erlaubt, die mathematischen Formeln
# sehr effizient auf jeden einzelnen Pixel des Bildes anzuwenden.

from PIL import Image  # Pillow zum Laden unseres Bildes.

import matplotlib.pyplot as plt  # Matplotlib zum Anzeigen der Ergebnisse.

# === Schritt 1: Bild laden und vorbereiten ===

try:
    # Wir laden das Bild 'leaves.jpg'.
    image_rgb = Image.open('leaves.jpg')

    # Um mit den Pixelwerten rechnen zu können, wandeln wir das Bild in ein NumPy-Array um.
    # WICHTIG: .astype(np.float64) konvertiert die Pixelwerte (0-255) in Fließkommazahlen.
    # Dies ist notwendig, um korrekte Ergebnisse bei Divisionen und Multiplikationen zu erhalten
    # und um einen "Integer Overflow" (z.B. 250+200 wird nicht 450) zu vermeiden.
    image_array = np.array(image_rgb).astype(np.float64)

    # Wir trennen die drei Farbkanäle Rot, Grün und Blau in separate Variablen.
    # Das Array hat die Form (Höhe, Breite, 3). Die ":, :" bedeuten "nimm alle Pixel in Höhe und Breite".
    # Die letzte Zahl (0, 1, 2) wählt den Farbkanal aus.
    R = image_array[:, :, 0]
    G = image_array[:, :, 1]
    B = image_array[:, :, 2]

except FileNotFoundError:
    print(
        "Fehler: Die Datei 'leaves.jpg' wurde nicht gefunden. Stelle sicher, dass sie sich im selben Ordner wie das Skript befindet.")
    # Wir beenden das Skript, wenn das Bild nicht geladen werden kann.
    exit()

# === Schritt 2: Grayscale-Konvertierungen berechnen ===
# Hier wenden wir die drei Formeln aus der Aufgabenstellung an.

# --- Methode 1: Lightness Method ---
# (min(R,G,B) + max(R,G,B)) / 2
# np.min() und np.max() mit axis=2 finden den minimalen/maximalen Wert entlang der Farbkanal-Achse für jeden Pixel.
grayscale_lightness = (np.min(image_array, axis=2) + np.max(image_array, axis=2)) / 2

# --- Methode 2: Average Method ---
# (R + G + B) / 3
grayscale_average = (R + G + B) / 3

# --- Methode 3: Luminosity Method ---
# 0.2989 * R + 0.5870 * G + 0.1140 * B
grayscale_luminosity = 0.2989 * R + 0.5870 * G + 0.1140 * B

# === Schritt 3: Ergebnisse anzeigen ===

# Wir erstellen ein Fenster mit einer Zeile und drei Spalten für unsere Bilder.
fig, axes = plt.subplots(1, 4, figsize=(18, 6))

# Haupttitel für das gesamte Fenster.
fig.suptitle('RGB zu Grayscale Konvertierungsmethoden', fontsize=16)

# --- Bild 1: Lightness ---
axes[3].imshow(grayscale_lightness, cmap='gray')
axes[3].set_title('Lightness Method')
axes[3].axis('off')  # Achsenbeschriftung ausschalten

# --- Bild 2: Average ---
axes[1].imshow(grayscale_average, cmap='gray')
axes[1].set_title('Average Method')
axes[1].axis('off')

# --- Bild 3: Luminosity ---
axes[2].imshow(grayscale_luminosity, cmap='gray')
axes[2].set_title('Luminosity Method')
axes[2].axis('off')

axes[0].imshow(image_rgb, cmap='gray')
axes[0].set_title('RGB Method')
axes[0].axis('off')

# Abstände anpassen und das Fenster anzeigen.
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
