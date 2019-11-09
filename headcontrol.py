#  head control
import redboard
import curses
import time

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

def pan(angle):
    redboard.servo21(angle)

def tilt(angle):
    redboard.servo22(angle)

def main(stdscr):
    keypress = 0
    up = 0
    stop = 0
    turbo = 0

    pan_centre = -19
    tilt_centre = 28

    pan_offset = 0
    tilt_offset = 0

    pan_limit = 25
    tilt_limit = 45

    pan(pan_centre)
    tilt(tilt_centre)

    while True:
        
        curses.halfdelay(1)
        c = stdscr.getch()
        #print(c)  # Uncomment to show keypresses
        #print("\r")
        
        if c == ord('w'):
            keypress = 1
            tilt_offset = tilt_offset if tilt_offset == -tilt_limit else tilt_offset - 1

        elif c == ord('s'):
            keypress = 1
            stop = 0
            tilt_offset = tilt_offset if tilt_offset == tilt_limit else tilt_offset + 1

        elif c == ord('a'):
            keypress = 1
            stop = 0
            pan_offset = pan_offset if pan_offset == -pan_limit else pan_offset - 1
			
        elif c == ord('d'):
            keypress = 1
            stop = 0
            pan_offset = pan_offset if pan_offset == pan_limit else pan_offset + 1
                        
        elif c == 32:  # Spacebar
            keypress = 1
            stop = 0                

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
            
        pan(pan_centre - pan_offset)
        tilt(tilt_centre - tilt_offset)
          
curses.wrapper(main)