import os
from PIL import Image
import glob

def compress_images(directory):
    print("Starting compression...")
    search_path = os.path.join(directory, "*.webp")
    for file_path in glob.glob(search_path):
        original_size = os.path.getsize(file_path)
        if original_size < 1024 * 1024:
            continue # Skip images already under 1MB
            
        try:
            with Image.open(file_path) as img:
                print(f"Processing {os.path.basename(file_path)} ({(original_size/1024/1024):.2f} MB)...")
                
                # Resize if image is too large (max 1920x1920)
                max_size = (1920, 1920)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Save with compression
                img.save(file_path, "WEBP", quality=75, method=4)
                
            new_size = os.path.getsize(file_path)
            print(f" -> Done! New size: {(new_size/1024/1024):.2f} MB")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    compress_images(r"d:\AMORA_Online\AnhChu")
    print("Compression complete!")
