#!/usr/bin/python2.7
 
import os
import time
from optparse import OptionParser
 
#Defining some constants to keep the code readable
PIN_RED = 2
PIN_GREEN = 5
PIN_BLUE = 6
ON_RED = 1
ON_BLUE = 1
ON_GREEN = 1
OFF = 0
HALF = 0.5
 
#define the main function
def main():
        #this section handles the parameters
        parser = OptionParser("notify.py [Options]")
   
        parser.add_option("-w", "--whatsapp",action="store_true", dest="whatsapp", help="Blink green")
        parser.add_option("-f", "--facebook",action="store_true", dest="facebook", help="Blink blue" )
        parser.add_option("-p", "--phone",action="store_true", dest="phone", help="Blink white")
        parser.add_option("-s", "--sms",action="store_true", dest="sms", help="no clue")
   
        (optionen, args) = parser.parse_args()
       
        #function that handles the flashing, the value of red, green and blue can be
        #between 0 and 1 e.g. 0.5
        def flash(red, green, blue):
                os.system('echo "'+str(PIN_RED)+'='+str(OFF)+'" > /dev/pi-blaster')
                os.system('echo "'+str(PIN_GREEN)+'='+str(OFF)+'" > /dev/pi-blaster')
                os.system('echo "'+str(PIN_BLUE)+'='+str(OFF)+'" > /dev/pi-blaster')
               
                #how often the light flashes
                n = 5
                while n > 0:
                        #turn on
                        os.system('echo "'+str(PIN_RED)+'='+str(red)+'" > /dev/pi-blaster')
                        os.system('echo "'+str(PIN_GREEN)+'='+str(green)+'" > /dev/pi-blaster')
                        os.system('echo "'+str(PIN_BLUE)+'='+str(blue)+'" > /dev/pi-blaster')
                        #wait
                        time.sleep(0.4)
                        #turn off
                        os.system('echo "'+str(PIN_RED)+'='+str(OFF)+'" > /dev/pi-blaster')
                        os.system('echo "'+str(PIN_GREEN)+'='+str(OFF)+'" > /dev/pi-blaster')
                        os.system('echo "'+str(PIN_BLUE)+'='+str(OFF)+'" > /dev/pi-blaster')
                        #wait
                        time.sleep(0.4)
                        #decrement of the flashing value
                        n = n -1               
   
        #handle the different parameters  
        if optionen.whatsapp:
                print "whatsapp"
                flash(0,1,0)   
   
        if optionen.facebook:
                print "facebook"
                flash(0,0,1)  
 
        if optionen.phone:
                print "phone"
                flash(1,1,1)
   
        if optionen.sms:
                print "sms"
                flash(1,1,0)
 
if __name__ == '__main__':
   main()