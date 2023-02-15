from PIL import Image
import os

# Set the path to the folder containing the WebP images
webp_folder_path = "path/to/webp/folder/"

# Set the path to the folder where the JPEG images will be saved
jpeg_folder_path = "path/to/jpeg/folder/"

# Get a list of all the WebP images in the folder
webp_files = [f for f in os.listdir(webp_folder_path) if f.endswith(".webp")]

# Convert each WebP image to JPEG and save it
for i, webp_file in enumerate(webp_files):
    # Open the WebP image
    webp_image = Image.open(os.path.join(webp_folder_path, webp_file))

    # Convert the WebP image to JPEG
    jpeg_image = webp_image.convert("RGB")

    # Set the path to save the JPEG image
    jpeg_file = os.path.splitext(webp_file)[0] + ".jpg"
    jpeg_path = os.path.join(jpeg_folder_path, jpeg_file)

    # Save the JPEG image
    jpeg_image.save(jpeg_path)

    # Print a message to show the progress
    print("Converted image {}/{}: {} -> {}".format(i+1, len(webp_files), webp_file, jpeg_file))
