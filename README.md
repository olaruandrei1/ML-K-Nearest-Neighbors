# K-NN Image Recognition (Face Dataset)

This project implements a **K-Nearest Neighbors (K-NN)** algorithm applied to a `.pgm` image dataset, used for facial recognition. A distance metric (norm) is used to find the closest neighbors to a given image, and the predicted class (person) is determined accordingly.

## 🔍 Description

- Uses a set of images organized in folders `s1` to `s40`, each containing images `1.pgm` to `9.pgm`.
- The first 8 images per person are used for training.
- You can choose the norm: `1`, `2`, `inf`, or `cos`.
- Displays both the input image and the closest matching image found by the algorithm.

## 🧠 K-NN Algorithm

1. Vectorizes the images and stores them in matrix A.
2. Calculates the distance between an unknown image and all training images.
3. Sorts the distances and selects the 3 closest neighbors.
4. Estimates the class using statistical mode.
5. Displays the result.

## ▶️ How to Run

1. Make sure you have the directory structure `m0Poze/s1/.../s40` with `.pgm` files.
2. Run the Python script and enter the desired norm when prompted:
   ```
   python script.py
   ```

## 👤 Author

**Olaru Andrei**  
[LinkedIn](https://www.linkedin.com/in/andrei-olaru-6a471a190/)
