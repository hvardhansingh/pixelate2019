from arduino import arduino

def turn(phi):
    arduino('r',-phi)

def stepForward(step):
    arduino('f',step)
