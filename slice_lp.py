from PIL import Image
import os

def slice_image(image_path, output_dir, slice_height=1200):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        img = Image.open(image_path)
        width, height = img.size
        
        num_slices = (height + slice_height - 1) // slice_height
        
        print(f"Slicing {image_path} ({width}x{height}) into {num_slices} slices of ~{slice_height}px height.")
        
        generated_files = []
        for i in range(num_slices):
            top = i * slice_height
            bottom = min((i + 1) * slice_height, height)
            
            # Crop the slice
            slice_img = img.crop((0, top, width, bottom))
            
            # Save format
            output_filename = f"section_{i+1:02d}.png"
            output_path = os.path.join(output_dir, output_filename)
            slice_img.save(output_path)
            
            print(f"Saved {output_path}")
            generated_files.append(output_filename)
            
        return generated_files
        
    except Exception as e:
        print(f"Error slicing image: {e}")
        return []

if __name__ == "__main__":
    files = slice_image('分析LP.png', 'assets')
    print("Generated slices:", files)
