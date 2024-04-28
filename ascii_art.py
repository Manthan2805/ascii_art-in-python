from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def scale_image(image, new_width=100):
    """Resizes an image preserving a modified aspect ratio for terminal display."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int((aspect_ratio * new_width) / 2.0)  # Adjust height factor for terminal character aspect ratio
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    """Converts the image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range in which it lies."""
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    """Converts an entire image to ASCII."""
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)

    ascii_str = map_pixels_to_ascii_chars(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Split the string based on image width to format it correctly
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    return ascii_img

def handle_image_conversion(image_filepath, new_width=100):
    """Handles the process of image loading, conversion, and display."""
    try:
        image = Image.open(image_filepath)
        ascii_img = convert_image_to_ascii(image, new_width)
        print(ascii_img)
    except Exception as e:
        print(f"Unable to open image file: {e}")

def main():
    """Main function to execute the script logic."""
    image_path = input("Please enter the path to the image file:\n")
    try:
        width = int(input("Please enter the desired width of the ASCII art (default is 100, press Enter for default):\n") or 100)
        handle_image_conversion(image_path, width)
    except ValueError:
        print("Please enter a valid integer for the width.")

if __name__ == '__main__':
    main()

