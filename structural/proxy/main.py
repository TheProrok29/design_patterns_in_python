from structural.proxy.image import Image, ProxyImage

my_image = Image('~/Obrazy/image.jpg')
my_image = ProxyImage(my_image)
my_image.display_image()
