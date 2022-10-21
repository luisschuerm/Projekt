from smbus import SMBus
from RPi.GPIO import RPI_REVISION
import time
from re import findall
from subprocess import check_output
from os.path import exists
try:
 
    import RPi.GPIO as GPIO
    
except RuntimeError:
    print("Error importing RPI.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
class LED():
    def __init__(self,color=None,*args,** kwargs):
        GPIO.setwarnings(False)
        self.pin = int(0)
        self.color = color
        self.state = False
        if self.color == "gruen":
            self.pin = 21
        elif self.color == "gelb":
            self.pin = 20
        elif self.color == "rot":
            self.pin = 26
 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.OUT)
        print(self.color+" aktiviert")
    def aktivieren(self):
        if self.color == "gruen":
            self.pin = 21
        elif self.color == "gelb":
            self.pin = 20
        elif self.color == "rot":
            self.pin = 26
 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.OUT)
        print(self.color+ " aktiviert")
 
    def an(self):
        self.state = True
        GPIO.output(self.pin, True)
        #print(self.color+ " eingeschaltet")
 
    def aus(self):
        self.state = False
        GPIO.output(self.pin, False)
        #print(self.color+ " ausgeschaltet")
 
    def deaktivieren(self):
        GPIO.cleanup(self.pin)
        print(self.color+ " deaktiviert")
 
    def alle_deaktivieren(self):
        GPIO.cleanup(21)
        GPIO.cleanup(22)
        GPIO.cleanup(26)
 
class Sensor():
    def __init__(self,name,*args,**kwargs):
        GPIO.setwarnings(False)
        self.name = name
        self.state = False

    def lesen(self,*args):
        base_dir ='/sys/bus/w1/devices/'
        device_file=base_dir + self.name+'/w1_slave'
        f = open(device_file, 'r')
        filecontent = f.read()
        f.close()
        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000

        #Temperatur ausgeben
        rueckgabewert = '%6.2f' % temperature
        return(rueckgabewert) 

BUS_NUMBER = 0 if RPI_REVISION == 1 else 1

# other commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100  # Enable bit
Rw = 0b00000010  # Read/Write bit
Rs = 0b00000001  # Register select bit

class I2CDevice:
    def __init__(self, addr=None, addr_default=None, bus=BUS_NUMBER):
        GPIO.setwarnings(False)
        if not addr:
            # try autodetect address, else use default if provided
            try:
                self.addr = int('0x{}'.format(
                      
                      findall("[0-9a-z]{2}(?!:)", check_output(['/usr/sbin/i2cdetect', '-y', str(BUS_NUMBER)]).decode())[0]), base=16) \
                    if exists('/usr/sbin/i2cdetect') else addr_default
            except:
                self.addr = addr_default
        else:
            self.addr = addr
        self.bus = SMBus(bus)

    # write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        time.sleep(0.0001)

    # write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)
        time.sleep(0.0001)

    # write a block of data
    def write_block_data(self, cmd, data):
        self.bus.write_block_data(self.addr, cmd, data)
        time.sleep(0.0001)

    # read a single byte
    def read(self):
        return self.bus.read_byte(self.addr)

    # read
    def read_data(self, cmd):
        return self.bus.read_byte_data(self.addr, cmd)

    # read a block of data
    def read_block_data(self, cmd):
        return self.bus.read_block_data(self.addr, cmd)

class LCD:
    def __init__(self, addr=None):
        self.addr = addr
        self.lcd = I2CDevice(addr=self.addr, addr_default=0x27)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x02)
        self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        time.sleep(0.2)

    # clocks EN to latch command
    def lcd_strobe(self, data):
        self.lcd.write_cmd(data | En | LCD_BACKLIGHT)
        time.sleep(.0005)
        self.lcd.write_cmd(((data & ~En) | LCD_BACKLIGHT))
        time.sleep(.0001)

    def lcd_write_four_bits(self, data):
        self.lcd.write_cmd(data | LCD_BACKLIGHT)
        self.lcd_strobe(data)

    # write a command to lcd
    def lcd_write(self, cmd, mode=0):
        self.lcd_write_four_bits(mode | (cmd & 0xF0))
        self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

    # put string function
    def schreiben(self, string, line):
        if line == 1:
            self.lcd_write(0x80)
        if line == 2:
            self.lcd_write(0xC0)
        if line == 3:
            self.lcd_write(0x94)
        if line == 4:
            self.lcd_write(0xD4)
        for char in string:
            self.lcd_write(ord(char), Rs)

   
    

    #clear lcd and set to home
    def loeschen(self):
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_RETURNHOME)

class Luefter():
    def __init__(self):
        GPIO.setwarnings(False)
        self.pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.OUT)
    def an(self):
        GPIO.output(self.pin,True)
    def aus(self):
        GPIO.output(self.pin,False)
