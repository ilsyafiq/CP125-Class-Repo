pixels = [100, 120, 200, 150, 180, 160, 140]

def count_bright_spots(pixels):
    count = 0
    for i in range(len(pixels)):
        if i == 0 or i == len(pixels)-1:
            continue
        else:
            if pixels[i] > pixels[i+1] and pixels[i] > pixels[i-1]:
                count += 1
            else:
                continue
    
    return count

print(count_bright_spots([100, 120, 200, 150, 180, 160, 140]))



