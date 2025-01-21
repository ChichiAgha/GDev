



# Function to create a PNG file


## firstly i installed PILLOW#

from PIL import Image, ImageDraw, ImageFont

# Function to create a PNG file
def create_png():
    # Create a blank image (RGB mode) with a white background
    img = Image.new('RGB', (400, 200), color='white')
    
    # Create a drawing object
    draw = ImageDraw.Draw(img)
    
    # Optional: Add text to the image
    text = "Hello, PNG!"
    text_position = (100, 80)  # Position of the text on the image
    text_color = "black"
    
    # Draw the text on the image (using default font)
    draw.text(text_position, text, fill=text_color)
    
    # Save the image as a PNG file
    img.save("example.png")
    print("PNG file 'example.png' created successfully!")

# Call the function to create the PNG
create_png()
