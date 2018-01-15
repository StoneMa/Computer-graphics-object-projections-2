# Hoang, Vincent
# 1000-949-600
# 2016-11-06
# Assignment_05

import sys
import OpenGL

from numpy import *
from math import *

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *

Angle = 0
Incr = 1

filename = None
vectors = []
faces = []
facesize = 0

c = 0
i = []
t = []
e = []
l = []
u = []
w = []
s = []

def get_globals():
      global vectors
      global faces
      global facesize      
      
      global c 
      global i 
      global t 
      global e
      global l
      global u 
      global w
      global s          

def readfile(myfile):
      global vectors
      global faces
      global facesize
      global filename
      
      #makes data empty
      vectors = []
      faces = []
      facesize = 0     
      
      filename = myfile
      
      fn = open(filename,"r")
      for line in fn:

            if "v" in line:
                  letter,x,y,z = line.strip().split()
                  x = float(x)
                  y = float(y)
                  z = float(z)
                  vectors.append([x,y,z,1])
                  continue
            if "f" in line:
                  tokens = line.strip().split()
                  if len(tokens) == 4: #triangle faces
                        facesize = 3
                  if len(tokens) == 5: #square faces
                        facesize = 4
                  tokens.remove("f")
                  faces.append(tokens)
                  continue
      '''
      print(vectors)
      print(faces)
      print(facesize)
      '''
      
def loadcamera():
      global c 
      global i 
      global t 
      global e
      global l
      global u 
      global w
      global s  
      global filename
      '''
      vectors = []
      faces = []
      facesize = 0
      '''
      c = 0
      i = []
      t = []
      e = []
      l = []
      u = []
      w = []
      s = []   
      
      if (filename == None):
            readfile("pyramid_05.txt")
      
      fn = open("cameras_05.txt","r")
      for line in fn:
            if "c" in line.strip().split():
                  c = c + 1
                  continue
            if "i " in line:
                  x = line.strip("i ").strip("\n")
                  #camera_names.append(i)
                  if (x == ""):
                        i.append([""])
                  else:
                        i.append([x])
            if "t " in line:
                  x = line.strip("t ").strip("\n")
                  if (x == ""):
                        t.append(["parallel"])
                  else:
                        t.append([x])
            if "e " in line:
                  x = line.strip("e ").split()
                  if (x == ""):
                        e.append([0,0,0,1])
                  else:
                        e.append([float(x[0]),float(x[1]),float(x[2])])
            if "l " in line:
                  x = line.strip("l ").split()
                  if (x == ""):
                        l.append([0,0,1,1])
                  else:
                        l.append([float(x[0]),float(x[1]),float(x[2])])
            if "u " in line:
                  x = line.strip("u ").split()
                  if (x == ""):
                        u.append([0,1,0,1])
                  else:
                        u.append([float(x[0]),float(x[1]),float(x[2])])
                  
            if "w " in line:
                  x = line.strip("w ").split()
                  if (x == ""):
                        w.append([-1,1,-1,1,-1,1])
                  
                  else:
                        w.append([float(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[4]),float(x[5])])
 
            if "s " in line:
                  x = line.strip("s ").split()
                  if (x == ""):
                        s.append([0.1,0.1,0.9,0.9])
          
                  else:
                        s.append([float(x[0]),float(x[1]),float(x[2]),float(x[3])])     
               
      '''         
      print(c)
      print(i)
      print(t)
      print(e)
      print(l)
      print(u)
      print(w)
      print(s)            
      '''
def create_pyramid():
      get_globals()
      
      glNewList(1,GL_COMPILE)
      if (facesize == 3):
            glBegin(GL_TRIANGLES)
      else:
            glBegin(GL_QUADS)
      
      for f in faces:
            v1 = vectors[int(f[0])-1]
            v2 = vectors[int(f[1])-1]
            v3 = vectors[int(f[2])-1]
            if (facesize == 4):
                  v4 = vectors[int(f[3])-1]
            '''
            print(v1)
            print(v2)
            print(v3)
            '''
            glColor3f(0,0,1)
            glVertex3f(v1[0],v1[1],v1[2])
            glVertex3f(v2[0],v2[1],v2[2])
            glVertex3f(v3[0],v3[1],v3[2])
            if(facesize == 4):
                  glVertex3f(v4[0],v4[1],v4[2])
            
            
      glEnd() 
      glEndList()

def display():
      get_globals()
      
      width=glutGet(GLUT_WINDOW_WIDTH)
      height=glutGet(GLUT_WINDOW_HEIGHT)
      
      for x in range(0,c):
            glEnable(GL_SCISSOR_TEST)
            glScissor(int(s[x][0]*width),int((1-s[x][3])*height),int((s[x][2] - s[x][0])*width),int((s[x][3] - s[x][1])*height))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            if (t[x][0] == "parallel"):
                  glOrtho(w[x][0],w[x][1],w[x][2],w[x][3],w[x][4],w[x][5])
            elif (t[x][0] == "perspective"):
                  glFrustum(w[x][0],w[x][1],w[x][2],w[x][3],w[x][4],w[x][5])
            gluLookAt(e[x][0],e[x][1],e[x][2],l[x][0],l[x][1],l[x][2],u[x][0],u[x][1],u[x][2])
            glMatrixMode(GL_MODELVIEW)    
            glViewport(int(s[x][0]*width),int((1-s[x][3])*height),int((s[x][2] - s[x][0])*width),int((s[x][3] - s[x][1])*height))
            glCallList(1) 
            glPushMatrix()
            glLoadIdentity() 
            glPopMatrix()    
            
      glFlush()
      glutSwapBuffers()                 

def keyHandler(Key, MouseX, MouseY):

      if (Key == b'n'):
            myfile = input("ENTER NAME OF FILE: ")
            readfile(myfile)
            
      elif (Key == b'd'):
            loadcamera()
            create_pyramid()
            display()
            
      elif (Key == b'x'):
            glRotatef(5,1,0,0)
            display()
            
      elif (Key == b'X'):
            glRotatef(-5,1,0,0)
            display()            
            
      elif (Key == b'y'):
            glRotatef(5,0,1,0)
            display()              
            
      elif (Key == b'Y'):
            glRotatef(-5,0,1,0)
            display()               
            
      elif (Key == b'z'):
            glRotatef(5,0,0,1)
            display()              
            
      elif (Key == b'Z'):
            glRotatef(-5,0,0,1)
            display()              
            
      elif (Key == b's'):
            glScalef(1.05,1.05,1.05)
            display()        
      
      elif (Key == b'S'):
            glScalef(1/1.05,1/1.05,1/1.05)
            display()            
                
      elif (Key == b'f'):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  value = (.05/1.05)*distance
                  Ap = e[x] + (value * N)
                  e[x] = Ap
                                  
            
            display()
                        
      elif (Key == b'b'):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  value = (.05)*distance
                  Ap = e[x] - (value * N)
                  e[x] = Ap                  
            
            display()                           
      
      elif (Key == b'p'):
            for x in range(0,c):
                  if(t[x][0] == "parallel"):
                        t[x][0] = "perspective"
                  elif(t[x][0] == "perspective"):
                        t[x][0] = "parallel"
                        
            display()
            
      elif Key == b'q' or Key == b'Q':
            print ("Bye")
            sys.exit()      
            
      else:
            print ("Invalid Key ",Key)      
      
def SpecialInput(Key, MouseX, MouseY):
      get_globals()
      
      if (Key == GLUT_KEY_LEFT):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  
                  U = [N[1]*u[x][2]-u[x][1]*N[2],-(N[0]*u[x][2]-u[x][0]*N[2]),N[0]*u[x][1]-u[x][0]*N[1] ]
                  distance = sqrt(U[0]**2 + U[1]**2 + U[2]**2)
                  U = array(U).dot(1/distance)
                  value = .05*distance
                  Ap = e[x] + (value * U)
                  e[x] = Ap
            
            display()
            
      if (Key == GLUT_KEY_RIGHT):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  
                  U = [N[1]*u[x][2]-u[x][1]*N[2],-(N[0]*u[x][2]-u[x][0]*N[2]),N[0]*u[x][1]-u[x][0]*N[1] ]
                  distance = sqrt(U[0]**2 + U[1]**2 + U[2]**2)
                  U = array(U).dot(1/distance)
                  value = .05*distance
                  Ap = e[x] - (value * U)
                  e[x] = Ap
                  
            display()            
            
      if (Key == GLUT_KEY_UP):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  
                  U = [N[1]*u[x][2]-u[x][1]*N[2],-(N[0]*u[x][2]-u[x][0]*N[2]),N[0]*u[x][1]-u[x][0]*N[1] ]
                  distance = sqrt(U[0]**2 + U[1]**2 + U[2]**2)
                  U = array(U).dot(1/distance)

                  V = [U[1]*N[2]-N[1]*U[2],-(U[0]*N[2]-N[0]*U[2]),U[0]*N[1]-N[0]*U[1]] #aleady normalized
                  distance = sqrt(V[0]**2 + V[1]**2 + V[2]**2)
                  value = .05*distance
                  Ap = e[x] + (value * array(V))
                  e[x] = Ap
                  
            display()            
            
      if (Key == GLUT_KEY_DOWN):
            for x in range(0,c):
                  
                  N = array(l[x])-array(e[x])
                  distance = sqrt(N[0]**2 + N[1]**2 + N[2]**2)
                  N = N.dot(1/distance)
                  
                  U = [N[1]*u[x][2]-u[x][1]*N[2],-(N[0]*u[x][2]-u[x][0]*N[2]),N[0]*u[x][1]-u[x][0]*N[1] ]
                  distance = sqrt(U[0]**2 + U[1]**2 + U[2]**2)
                  U = array(U).dot(1/distance)

                  V = [U[1]*N[2]-N[1]*U[2],-(U[0]*N[2]-N[0]*U[2]),U[0]*N[1]-N[0]*U[1]] #aleady normalized
                  distance = sqrt(V[0]**2 + V[1]**2 + V[2]**2)
                  value = .05*distance
                  Ap = e[x] - (value * array(V))
                  e[x] = Ap                  
            
            display()            

def timer(dummy):
      display()
      glutTimerFunc(30,timer,0)
def reshape(w, h):
      print ("Width=",w,"Height=",h)
          
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Hoang_assignment_05")
glClearColor(1,1,0,0)
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS);

glutDisplayFunc(display)
glutSpecialFunc(SpecialInput)
glutKeyboardFunc(keyHandler)
glutReshapeFunc(reshape)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
create_pyramid()
loadcamera()
glutMainLoop()

