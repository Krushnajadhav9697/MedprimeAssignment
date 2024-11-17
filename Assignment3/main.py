from PIL import Image

def create_collage(image_paths, output_path,output_format="JPEG"):
   
    try:
        
        images = []
        for path in image_paths:
            img = Image.open(path)
            images.append(img)

        
        min_width = min(img.width for img in images)
        min_height = min(img.height for img in images)
        for i in range(len(images)):
            images[i] = images[i].resize((min_width, min_height))

        
        collage_width = min_width * 2
        collage_height = min_height * 2
        collage = Image.new("RGB", (collage_width, collage_height))

        
        collage.paste(images[0], (0, 0))  
        collage.paste(images[1], (min_width, 0))  
        collage.paste(images[2], (0, min_height))  
        collage.paste(images[3], (min_width, min_height))  

       
        collage.save(output_path, format=output_format)
        print(f"Collage saved successfully as '{output_path}' in {output_format} format.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    
    
    image_paths = []
    for i in range(4):
        path = input(f"Enter the path for image {i + 1}: ").strip()
        image_paths.append(path)

    output_format = input("Please specify the output file format (e.g., jpg, png): ").strip().lower()
    output_path = f"collage.{output_format}"

    format_mapping = {"jpg": "JPEG", "jpeg": "JPEG", "png": "PNG", "bmp": "BMP", "tiff": "TIFF"}
    output_format = format_mapping.get(output_format, "JPEG")
    
    create_collage(image_paths, output_path,output_format)

if __name__ == "__main__":
    main()
