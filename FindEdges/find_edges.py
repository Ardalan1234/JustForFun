import numpy as np
import matplotlib.pyplot as plt


def find_edges(image):
    # Convert the image to grayscale
    grayscale = np.mean(image, axis=2)

    # Define the Sobel operators
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Perform convolution with the Sobel operators
    gradient_x = convolution(grayscale, sobel_x)
    gradient_y = convolution(grayscale, sobel_y)

    # Calculate the magnitude of gradients
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

    # Normalize the gradient magnitude to a range of 0-255
    gradient_magnitude *= 255.0 / np.max(gradient_magnitude)

    return gradient_magnitude


def convolution(image, kernel):
    # Get the dimensions of the image and kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding required for 'same' convolution
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Create a padded image with zeros
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)))

    # Perform the convolution
    output = np.zeros_like(image)
    for i in range(image_height):
        for j in range(image_width):
            output[i, j] = np.sum(padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)

    return output


# Load the image
image = plt.imread('path\\to\\your\\image')

# Find edges in the image
edges = find_edges(image)

# Display the original image and the edge map
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')
axes[1].imshow(edges, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Edges')
plt.tight_layout()
plt.show()
