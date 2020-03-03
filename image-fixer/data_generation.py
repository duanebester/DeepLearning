import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image

project_directory = r'/Users/duanebester/code/DeepLearning/image-fixer/'
datagen = ImageDataGenerator(rotation_range=15,
                             width_shift_range=0.01,
                             height_shift_range=0.1,
                             shear_range=0.1,
                             zoom_range=0.1,
                             horizontal_flip=True,
                             vertical_flip=True,
                             fill_mode='constant')


def generate_images_from_image(fname, save_prefix, save_dir):
    print(fname)
    img = load_img(fname)  # this is a PIL image
    img = img.resize((256, 256), Image.ANTIALIAS)
    x = img_to_array(img)  # this is a Numpy array with shape (3, 256, 256)
    x = x.reshape(
        (1, ) + x.shape)  # this is a Numpy array with shape (1, 3, 256, 256)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for _ in datagen.flow(x,
                          batch_size=1,
                          save_to_dir=save_dir,
                          save_prefix=save_prefix,
                          save_format='jpg'):
        i += 1
        if i > 5:
            break  # otherwise the generator would loop indefinitely


def generate_images_from_dir(input_dir, name, output_dir):
    directory = project_directory + 'raw/' + input_dir + '/' + name
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            generate_images_from_image(os.path.join(directory, filename), name,
                                       output_dir)
        else:
            continue


generate_images_from_dir('train', 'bad', 'data/trainB')
generate_images_from_dir('train', 'good', 'data/trainA')

generate_images_from_dir('validation', 'bad', 'data/testB')
generate_images_from_dir('validation', 'good', 'data/testA')
