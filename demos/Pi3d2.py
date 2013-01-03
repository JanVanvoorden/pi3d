from __future__ import absolute_import

import math,random,time

from pi3d import *

from pi3d import Display
from pi3d.Texture import Texture
from pi3d.Keyboard import Keyboard

from pi3d.context.Light import Light
from pi3d.Shader import Shader

from pi3d.shape.Sphere import Sphere
from pi3d.util.String import String
from pi3d.util.Font import Font

# Setup display and initialise pi3d
DISPLAY = Display.create(x=10, y=10, w=1000, h=800)
DISPLAY.set_background(0.4, 0.6, 0.8, 1.0)      # r,g,b,alpha

#setup textures, light position and initial model position
Light((5, 5, 1))
#create shaders
shader = Shader("shaders/uv_reflect")
flatsh = Shader("shaders/uv_flat")

#Create textures
shapeimg = Texture("textures/straw1.jpg")
shapebump = Texture("textures/floor_nm.jpg", True)
shapeshine = Texture("textures/pong3.png")

#Create shape
myshape = []
num = 7
for i in range(num):
  myshape.append(Sphere(sides=32))
  myshape[i].translate(0, -num +2*i, 10)
  myshape[i].set_draw_details(shader, [shapeimg, shapebump, shapeshine], 8.0, 0.2)
  light2 = Light((-5, -5, i - 3))
  myshape[i].set_light(light2)

cAngle = [0.0, 0.0, 0.0]
dx = 0.05

tick=0
next_time = time.time()+10.0

arialFont = Font("AR_CENA","#dd00aa")   #load AR_CENA font and set the font colour to 'raspberry'
mystring = String(font=arialFont, string="RaspberryPi_Rocks") #TODO needs to cope with spaces in strings
mystring.translate(0.0, 0.0, 1)
mystring.set_shader(flatsh)

# Fetch key presses. This line has to be commented out to see the FPS printout
#mykeys = Keyboard()

# Display scene and rotate shape
while DISPLAY.loop_running():

  #camera.reset()
  #cAngle[1] += 0.5
  #camera.rotateY(cAngle[1])

  for s in myshape:
    s.draw()
    #s.rotateIncY(1.247)
    #s.rotateIncZ(0.613)
    s.translateX(dx)
    if s.unif[0] > 5: dx = -0.05
    elif s.unif[0] < -5: dx = 0.05


  mystring.draw()
  mystring.rotateIncZ(0.05)

  #camera.was_moved = False

  if time.time() > next_time:
    print "FPS:",tick/10.0
    tick=0
    next_time = time.time()+10.0
  tick+=1

  """ # this block needs to be commented out to be able to see the FPS readout (actually the creation of the Keyboard instance above is what does it)
  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
  """

quit()
