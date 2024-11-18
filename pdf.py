import os
from PIL import Image

# Directories
output_dir = './PDFs'
source_dir = './Images'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each image in the source directory
for file in os.listdir(source_dir):
    try:
        # Check if the file is an image with a valid extension
        if file.lower().endswith(('png', 'jpg', 'jpeg')):
            # Full path to the image file
            image_path = os.path.join(source_dir, file)
            
            # Open the image
            image = Image.open(image_path)
            
            # Convert image to RGB (required for PDF saving)
            image_converted = image.convert('RGB')
            
            # Extract filename without extension
            filename_without_extension = os.path.splitext(file)[0]
            
            # Define the output PDF path
            pdf_path = os.path.join(output_dir, f"{filename_without_extension}.pdf")
            
            # Save the image as a PDF
            image_converted.save(pdf_path)

            print(f"Converted {file} to {pdf_path}")
    
    except Exception as e:
        print(f"Error processing file {file}: {e}")
