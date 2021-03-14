from PIL import Image
import sys

ASCII_CHARS = ['@', '&', '$', '#', '{', '(', '/', '<', ';', '=', '*', '^', '.']


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join(ASCII_CHARS[pix//20] for pix in pixels)
    return characters


def main_funct():
    new_width = int(sys.argv[1])
    path = input('Enter a valid pathname to an image: \n')
    try:
        image = Image.open(path)
    except:
        print(path, ' is not a valid pathname to an image.')
        return -1

    new_image_data = pixel_to_ascii(grayify(resize_image(image, new_width)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:i+new_width] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_image)


if __name__ == '__main__':
    main_funct()
