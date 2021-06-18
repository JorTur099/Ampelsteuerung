import RPi.GPIO as GPIO
import time
from functools import partial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

AMPEL1_ROT = 8
ampel1_rot = partial(GPIO.output, AMPEL1_ROT)
AMPEL1_GELB = 10
ampel1_gelb = partial(GPIO.output, AMPEL1_GELB)
AMPEL1_GRUEN = 12
ampel1_gruen = partial(GPIO.output, AMPEL1_GRUEN)
FUSS1_ROT = 19
fuss1_rot = partial(GPIO.output, FUSS1_ROT)
FUSS1_GRUEN = 21
fuss1_gruen = partial(GPIO.output, FUSS1_GRUEN)

AMPEL2_ROT = 11
ampel2_rot = partial(GPIO.output, AMPEL2_ROT)
AMPEL2_GELB = 13
ampel2_gelb = partial(GPIO.output, AMPEL2_GELB)
AMPEL2_GRUEN = 15
ampel2_gruen = partial(GPIO.output, AMPEL2_GRUEN)
FUSS2_ROT = 16
fuss2_rot = partial(GPIO.output, FUSS2_ROT)
FUSS2_GRUEN = 18
fuss2_gruen = partial(GPIO.output, FUSS2_GRUEN)

GPIO.setup(36, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)

#Definition der einzelnen Autos
AMPEL1_AUTO1= 29
ampel1_auto1 = partial(GPIO.input, AMPEL1_AUTO1)
AMPEL1_AUTO2= 31
ampel1_auto2 = partial(GPIO.input, AMPEL1_AUTO2)
AMPEL2_AUTO1= 33
ampel2_auto1 = partial(GPIO.input, AMPEL2_AUTO1)
AMPEL2_AUTO2= 35
ampel2_auto2 = partial(GPIO.input, AMPEL2_AUTO1)

#rot -> out2
GPIO.setup(AMPEL1_ROT,GPIO.OUT)
#gelb -> out1
GPIO.setup(AMPEL1_GELB,GPIO.OUT)
#greun -> out0
GPIO.setup(AMPEL1_GRUEN,GPIO.OUT)
#fussgaenger rot -> out10
GPIO.setup(FUSS1_ROT,GPIO.OUT)
#fussgaenger gruen -> out9
GPIO.setup(FUSS1_GRUEN,GPIO.OUT)

#rot2 -> out8
GPIO.setup(AMPEL2_ROT,GPIO.OUT)
#gelb2 -> out7
GPIO.setup(AMPEL2_GELB,GPIO.OUT)
#greun2 -> out6
GPIO.setup(AMPEL2_GRUEN,GPIO.OUT)
#fussgaenger2 rot -> out4
GPIO.setup(FUSS2_ROT,GPIO.OUT)
#fussgaenger2 gruen -> out3
GPIO.setup(FUSS2_GRUEN,GPIO.OUT)

ampel1_gruen(True)
ampel1_gelb(False)
ampel1_rot(True)
ampel2_gruen(False)
ampel2_gelb(False)
ampel2_rot(True)
fuss1_gruen(False)
fuss2_gruen(False)
fuss1_rot(True)
fuss2_rot(True)

 
while True:

  GPIO.setup(8,GPIO.OUT)
  GPIO.setup(10,GPIO.OUT)
  GPIO.setup(12,GPIO.OUT)
  GPIO.setup(19,GPIO.OUT)
  GPIO.setup(21,GPIO.OUT)
  GPIO.setup(11,GPIO.OUT)
  GPIO.setup(13,GPIO.OUT)
  GPIO.setup(15,GPIO.OUT)
  GPIO.setup(16,GPIO.OUT)
  GPIO.setup(18,GPIO.OUT)
  GPIO.setup(36,GPIO.IN)
  GPIO.setup(37,GPIO.IN)
  GPIO.setup(38,GPIO.IN)
  GPIO.setup(40,GPIO.IN)

  inputInt0 = GPIO.input(36)#GPIO 25
  inputInt1 = GPIO.input(37)#GPIO 8
  inputInt4 = GPIO.input(38)#GPIO 7
  inputInt5 = GPIO.input(40)#GPIO 12
  


  ampel1_rot(True)
  time.sleep(2)
  ampel2_gelb(True)
  time.sleep(2)
  ampel2_rot(False)
  ampel2_gelb(False)
  fuss2_rot(False)
  fuss1_gruen(False)
  ampel2_gruen(True)
  fuss2_gruen(True)
  time.sleep(3)
  print("a")  

  while (inputInt0)==0 and (inputInt1)==0:
    time.sleep(0.5)
    print(str(inputInt0))
    print(str(inputInt1)) 
    inputInt0 = GPIO.input(36)#GPIO 25
    inputInt1 = GPIO.input(37)#GPIO 8   

  fuss2_gruen(False)
  time.sleep(0.5)
  fuss2_gruen(True)
  time.sleep(0.5)
  fuss2_gruen(False)
  time.sleep(0.5)
  fuss2_gruen(True)
  time.sleep(0.5)
  fuss2_gruen(False)
  fuss2_rot(True)
  ampel2_gruen(False)
  time.sleep(0.5)
  ampel2_gruen(True)
  time.sleep(0.5)
  ampel2_gruen(False)
  time.sleep(0.5)
  ampel2_gruen(True)
  time.sleep(0.5)
  ampel2_gruen(False)
  time.sleep(0.5)
  ampel2_gruen(True)
  time.sleep(0.5)
  ampel2_gruen(False)
  time.sleep(0.5)
  ampel2_gruen(True)
  time.sleep(0.5)
  ampel2_gruen(False)
  ampel2_gelb(True)
  time.sleep(3) 
  ampel2_rot(True)
  ampel2_gelb(False)

  time.sleep(2)
  ampel1_gelb(True)
  time.sleep(2)
  ampel1_rot(False)
  ampel1_gelb(False)
  fuss1_rot(False)
  ampel1_gruen(True)
  fuss1_gruen(True)
  time.sleep(3)

  print("b")
  print(inputInt4)
  

  while (inputInt4)==0 and (inputInt5)==0:
    time.sleep(0.5)
    print("Test2")
    inputInt4 = GPIO.input(38)#GPIO 7
    inputInt5 = GPIO.input(40)#GPIO 12
    

  fuss1_gruen(False)
  time.sleep(0.5)
  fuss1_gruen(True)
  time.sleep(0.5)
  fuss1_gruen(False)
  time.sleep(0.5)
  fuss1_gruen(True)
  time.sleep(0.5)
  fuss1_gruen(False)
  fuss1_rot(True)
  ampel1_gruen(False)
  time.sleep(0.5)
  ampel1_gruen(True)
  time.sleep(0.5)
  ampel1_gruen(False)
  time.sleep(0.5)
  ampel1_gruen(True)
  time.sleep(0.5)
  ampel1_gruen(False)
  time.sleep(0.5)
  ampel1_gruen(True)
  time.sleep(0.5)
  ampel1_gruen(False)
  time.sleep(0.5)
  ampel1_gruen(True)
  time.sleep(0.5)
  ampel1_gruen(False)
  ampel1_gelb(True)
  time.sleep(3) 
  ampel1_gelb(False)
  ampel1_rot(True)



