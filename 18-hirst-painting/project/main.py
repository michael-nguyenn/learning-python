import colorgram

c = colorgram.extract('dots.jpg', 11)


# print(colors[1].rgb[0])

def rgb_extractor(colors):
    palette = []

    for color in colors:
        rgb = color.rgb
        palette.append((rgb[0], rgb[1], rgb[2]))

    palette.pop(0)
    return palette


color_palette = rgb_extractor(c)
