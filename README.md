
# Steganography - Hide a Message in an Image

## Overview

This project is a **Steganography tool** developed using Python and Tkinter, allowing users to hide and retrieve messages within images by manipulating the least significant bits of the pixel data. The interface is user-friendly and provides basic functionalities for embedding and extracting secret messages from PNG and JPG images.

## Features

- **Hide a Message:** Insert a hidden message inside an image.
- **Extract a Message:** Retrieve the hidden message from an image where the data was previously embedded.
- **Supported Formats:** Works with PNG and JPG image formats.
- **Graphical Interface:** A simple Tkinter-based GUI for easy interaction.

## Requirements

Before running the project, you need to install the required Python libraries:

```bash
pip install pillow opencv-python
```

## How to Use

1. **Open an Image:**
   - Click on the **"Open Image"** button to load an image in which you want to hide or retrieve a message. The image will be displayed

2. **Hide a Message:**
   - Type your secret message in the provided text area.
   - Click on the **"Hide Data"** button to embed the message in the image.
   - The modified image with the hidden message will be saved in the same directory as the original image with the filename + `hidden.png`.

3. **Show the Hidden Message:**
   - Load the image with the hidden message.
   - Click on the **"Show Data"** button to retrieve and display the hidden message.

4. **Save the Image:**
   - Click the **"Save Image"** button if you want to save any modifications or hidden images.

  
## How It Works

- The program splits the image into its RGB channels and hides the message in the blue channel by modifying the least significant bit (LSB) of each pixel.
- When extracting, it reads the LSBs of the blue channel to reconstruct the hidden message.


