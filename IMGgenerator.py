from PIL import Image, ImageDraw, ImageFont

def generate_images(background_color, text_color, start, end, resolution_x, resolution_y):
    # Loop through the range of numbers
    for number in range(start, end + 1):
        # Create a new image with the specified resolution and background color
        image = Image.new('RGB', (resolution_x, resolution_y), background_color)
        draw = ImageDraw.Draw(image)

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 45)
        except IOError:
            font = ImageFont.load_default()

        # Use binary search to find the largest font size that fits the number within the image
        low, high = 1, resolution_y
        while low < high:
            mid = (low + high + 1) // 2
            temp_font = ImageFont.truetype("arial.ttf", mid)
            bbox = draw.textbbox((0, 0), str(number), font=temp_font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            if text_width > resolution_x or text_height > resolution_y:
                high = mid - 1
            else:
                low = mid

        font = ImageFont.truetype("arial.ttf", low)

        # Calculate the position to center the number both horizontally and vertically
        bbox = draw.textbbox((0, 0), str(number), font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        ascent, descent = font.getmetrics()
        text_top = (resolution_y - (ascent + descent)) / 2
        position = ((resolution_x - text_width) / 2, text_top)

        # Draw the number on the image
        draw.text(position, str(number), fill=text_color, font=font)

        # Save the image with the number as the filename
        image.save(f'imagem-teste-{number}.png')
        print(f"Image for number {number} generated successfully!")

# Example usage
background_color = (255, 255, 255)  # White background
text_color = (0, 0, 0)  # Black text
start = 1
end = 8
resolution_x = 500
resolution_y = 500

generate_images(background_color, text_color, start, end, resolution_x, resolution_y)
