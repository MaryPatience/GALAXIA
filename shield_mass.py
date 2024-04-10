def CM_shield(length, width, height):
    ''' 4 sides'''
    volume = length*width*height
    total_volume = 4*volume
    return total_volume

def CM_to_detector_shield(l,b1,b2,h):
    volume = 0.5*(b1+b2)*h*l
    total_volume = 4*volume
    return total_volume

def detector_shield(length, width, height,length_base, width_base, height_base):
    volume = length*width*height
    total_volume = (length_base*width_base*height_base) + (4*volume)
    return total_volume

final = CM_shield(141.42, 0.4, 0.03) + CM_to_detector_shield(0.4,100,141.42,500) + detector_shield(100, 0.4, 0.2,100, 100, 0.4)
mass_of_shield = final*(11.4+7.28+8.92)
print(f"Final volume = {final} cm^3")
print(f"Shielding mass = {mass_of_shield} g")
