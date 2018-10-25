"""Contract 3."""
import pygame
pygame.init()


class Var:
    """Class that stores all variables."""

    image = [pygame.image.load('./Resources/Background.png'),
             pygame.image.load('./Resources/Asset.png')
             ]
    image_position = [(0, 0), (image[0].get_width()/4, image[0].get_width()/4)]
    image_rotation = [0, 0]
    image_scale = [1, 0.5]
    item_image_transparency = [False, False]
    item_image_transparency_level = [255, 255]
    image_colour_inverted = [False, True]
    exported_image_scale = 2
    exported_file_name = 'Exported_File'


def simple_crafting(image, position, rotation,
                    transparency_allow, scale,
                    transparency, colour_inversion,
                    exported_image_scale, exported_file_name):
    """
    Script processes images, combines and exports edited images to one file.

    :param image:                Array that stores information about all images
    :param position:             Array that stores information about positions
                                 of all images
    :param rotation:             Array that stores information about angle that
                                 image will be rotated
    :param transparency_allow:   Array that stores boolean value that determine
                                 whether transparency will be applied
    :param scale:                Array that stores scales of all images
    :param transparency:         Array that stores transparency values of all
                                 images
    :param colour_inversion:     Array that stores boolean that determine
                                 whether colours are gonna be inverted
    :param exported_image_scale: Variable that stores information on final
                                 image scale
    :param exported_file_name:   Variable that enables user to set name of a
                                 exported image
    :return:                     Exported edited images in one file
    """
    image[0] = image_resize(image[0], scale[0])
    screen = pygame.display.set_mode((image[0].get_width(),
                                      image[0].get_height())
                                     )
    screen.fill((255, 255, 255, 0))

    for i in range(0, len(image)):
        if transparency_allow[i]:
            image_transparency(image[i], transparency[i])
        if not image[i] == image[0]:
            image[i] = image_resize(image[i], scale[i])
        if colour_inversion[i]:
            image_negative(image[i])
        screen.blit(image_rotation(image[i], rotation[i]), position[i])

    screen = image_resize(screen, exported_image_scale)
    pygame.image.save(screen, "./Exported/" + exported_file_name + ".png")


def image_rotation(image, angle):
    """
    Rotate image in a chosen direction.

    :param image:   Image file that will be rotated
    :param angle:   Angle that image file will be rotated by
    :return:        Rotated image
    """
    return pygame.transform.rotate(image, angle)


def image_resize(image, scale_factor):
    """
    Resize exported file resolution by scale factor.

    :param image:          Image screen that will be resize
    :param scale_factor:    Scale factor that increases resolution of an image
                            where 1 = 100%
    :return:                Resize version of an image
    """
    width = image.get_width()
    height = image.get_height()

    return pygame.transform.scale(image, (int(round(width * scale_factor)),
                                          int(round(height * scale_factor)))
                                  )


def image_negative(image):
    """
    Invert all colours.

    :param image:   Image that will have its colours inverted
    :return:        Image with inverted colours
    """
    for y in range(0, image.get_height()):
        for x in range(0, image.get_width()):
            pixel = image.get_at((x, y))
            image.set_at((x, y), (255 - pixel.r, 255 - pixel.g,
                                  255 - pixel.b, pixel.a)
                         )


def image_transparency(image, transparency):
    """
    Change image alpha channel values to make object transparent.

    :param image:           Image that will have its a transparency adjusted
    :param transparency:    Value that image's alpha channel value will be
                            dropped to
    :return:                Transparent image
    """
    for y in range(0, image.get_height()):
        for x in range(0, image.get_width()):
            if image.get_at((x, y)).a > transparency:
                image.set_at((x, y), (image.get_at((x, y)).r,
                                      image.get_at((x, y)).g,
                                      image.get_at((x, y)).b,
                                      transparency)
                             )


simple_crafting(Var.image, Var.image_position, Var.image_rotation,
                Var.item_image_transparency, Var.image_scale,
                Var.item_image_transparency_level, Var.image_colour_inverted,
                Var.exported_image_scale, Var.exported_file_name
                )
