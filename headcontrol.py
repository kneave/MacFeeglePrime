#  head control
import redboard
import curses
import time

def pan(angle):
    redboard.servo21(angle)

def tilt(angle):
    redboard.servo22(angle)

pan_centre = -19
tilt_centre = 28

pan(pan_centre)
tilt(tilt_centre)



stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

print("\r")
print("W = Head Down\r")
print("S = Head Up\r")
print("A = Head Left\r")
print("D = Head Right\r")
print("Spacebar = Reset Centre\r")
print("T = Turbo\r")
print("R = Reverse Steering\r")

time.sleep(3)

def main(stdscr):
    keypress = 0
    up = 0
    stop = 0

    while True:
        
        curses.halfdelay(1)
        c = stdscr.getch()
        #print(c)  # Uncomment to show keypresses
        #print("\r")
        
        if c == ord('w'):
            keypress = 1
            print("Down")
            print("\r")
            stop = 0
            motor1 = -100  # Set motor speed and direction
            motor2 = -100  # Set motor speed and direction

        elif c == ord('s'):
            keypress = 1
            stop = 0
            print("Up")
            print("\r")
            motor1 = 100
            motor2 = 100

        elif c == ord('a'):
            keypress = 1
            stop = 0
            print("Left")
            print("\r")
            motor1 = -100
            motor2 = 100
			
        elif c == ord('d'):
            keypress = 1
            stop = 0
            print("Right")
            print("\r")
            motor1 = 100
            motor2 = -100
                        
        elif c == 32:  # Spacebar
            keypress = 1
            stop = 0
            print("Stop")
            print("\r")    
            motor1 = 0
            motor2 = 0                


        elif c == ord('r') and rSteer == False:
            keypress = 1
            stop = 0
            rSteer = True
            print ("Reverse Steering")
            print("\r")

        elif c == ord('r') and rSteer == True:
            keypress = 1
            stop = 0
            rSteer = False
            print ("Normal Steering")
            print("\r")



        elif c == ord('t') and turbo == False:
            keypress = 1
            stop = 0
            turbo = True
            print ("Turbo on")
            print("\r")

        elif c == ord('t') and turbo == True:
            keypress = 1
            stop = 0
            turbo = False
            print ("Turbo off")
            print("\r")



        # Pressing a key also produces a number of key up events.
        # This block of code only stops the robot moving after at least 4 key up events have been detected.
        # This makes driving the robot smoother but adds a short delay- 
        # -from when you release the key until the robot stops.
  
        if c == -1:  # Check for key release
            stop += 1  # Count the number of key up events          
        if keypress == 1 and stop > 5:  # Min = 4 - If the robot pauses when you hold a key down- 
                                        # -increase this number.
            keypress = 0
            stop = 0
            print("Stop----------------------------------------")
            print("\r")
            motor1 = 0
            motor2 = 0




        # Half the speed if Turbo is off
        if turbo == True:
            m1 = motor1
            m2 = motor2
        
        elif turbo == False:
            m1 = motor1 / 2
            m2 = motor2 / 2

        # Reverse the steering if 'R' has been pressed
        if rSteer == False:
            redboard.M1(m1)
            redboard.M2(m2)

        else:
            redboard.M1(m2)
            redboard.M2(m1)
          
curses.wrapper(main)