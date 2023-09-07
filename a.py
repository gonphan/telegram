import pyscreenshot as ImageGrab
from os import listdir
dem = 0
while True:
# Capture a partial screenshot
    screenshot = ImageGrab.grab(bbox=(145, 2, 1743, 937))
    #screenshot.show()
    dem = dem +1
    # Save the screenshot to a file
    if dem <5 :
        screenshot.save(' bb/'+str(dem) +".png")
    else:
        break
