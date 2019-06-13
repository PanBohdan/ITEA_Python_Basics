def rectangle_maker(height, width):
    height = round(height)
    width = round(width)
    if height <= 0 or width <= 0:
        print("Height or width can't be zero or less")
        return
    for i in range(0, height):
        print('*'*width)


if __name__ == '__main__':
    rectangle_maker(5, 13)
