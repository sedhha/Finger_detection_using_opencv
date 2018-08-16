Hi! 
This is an illustration on simple gesture recognition to count number of fingers in front of the camera feed.
Even though code has been calibrated multiple times, but depending upon your camera features and background 
you may need to calibrate it again. Though, there is just a simple concept for performing the calibration

Since Standard deviation provides us the best mean to analyze overall data, the statement:
print(np.std(img))
is used to obtain standard deviation, you will observe definite difference for each time you point your fingers.
Using this you can calibrate your code. A small video is attached on how it actually works, and accuracy level
after calibration, in case you find any other issue, let me know. Good thing about this code is that it requires
just two standard computer vision libraries that is numpy and cv2. Hope you have a good experience with this.

I am working on modyfying the code even more using convexity hull features, ecentricity etc.

Let me know if you face any issues with code.