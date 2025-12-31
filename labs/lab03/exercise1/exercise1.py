pixels = [100, 120, 200, 150, 180, 160, 140]

def count_bright_spots(pixels):
    for i in range(len(pixels)):
        if i == 0 or 6:
            continue
        else:
            if pixels[i] > pixels[i+1] and pixels[i] > pixels[i-1]:
                print "Bright spot"
            else:
                print "Not a bright spot"



