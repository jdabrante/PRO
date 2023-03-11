def tworgb (rgb: str)-> tuple:
    if len(rgb) == 2:
        return int(rgb,16)
    result = f'{int(rgb[:2],16)},{tworgb(rgb[2:])}'
    return result

print(tworgb("A131F7"))