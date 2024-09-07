import pygame, math, time, random, copy,numpy
from pygame.locals import *






from random import shuffle


ord = [i for i in range(10)]
shuffle(ord)




pygame.init()
screen = pygame.display.set_mode((1280, 720),FULLSCREEN)
clock = pygame.time.Clock()
running = True
red = 100
green = 100
blue = 100
color = (red,green,blue)

width = screen.get_width()
height = screen.get_height()


pos1 = [-8+width//6,height]
pos2 = [0,-8+height/2]
pos3 = [0,-8+height/6]
pos4 = [8+width/6,0]
pos5 = [8+width/2,0]
pos6 = [8+width*5//6,0]
pos7 = [width,8+height/2]
pos8 = [width,8+height*5/6]
pos9 = [-8+width*5/6,height]
pos10 = [-8+width/2,height]
position2 = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10]


pos1 = [8+width//6,height]
pos2 = [0,8+height/2]
pos3 = [0,8+height/6]
pos4 = [-8+width/6,0]
pos5 = [-8+width/2,0]
pos6 = [-8+width*5//6,0]
pos7 = [width,-8+height/2]
pos8 = [width,-8+height*5/6]
pos9 = [8+width*5/6,height]
pos10 = [8+width/2,height]
position1 = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10]





vars = {}
for i in range(10):
    string1 = str(i)
    for j in range(10):
        string2 = str(j)
        if string1 != string2:
            vars[string1 + string2] = [position1[i],position2[j]]





test_car = [True,False,False,False,False,False,False,False,False,False]


val = True 
    


 


start_line1 = (0,height/6)
end_line1 = (width/2,height/6)

start_line2 = (width/2,height*5/6)
end_line2 = (width,height*5/6)

start_line3 = (width/2,0)
end_line3 = (width/2,height)

start_line4 = (0,height/2)
end_line4 = (width,height/2)

start_line5 = (width/6,0)
end_line5 = (width/6,height)

start_line6 = (width*5/6,height)
end_line6 = (width*5/6,0)

start_line7 = (0,height*5/6)
end_line7 = (width/6,height*5/6)

start_line8 = (width*5/6,height/6)
end_line8 = (width,height/6)





def copy_vars(vars,length):
    list_vars = []
    for i in range(length):
        list_vars.append(copy.deepcopy(vars))
    return list_vars
    
vars_list = copy_vars(vars,10)


def copy_var(var,length):
    list_var = []
    for i in range(length):
        list_var.append(copy.copy(var))
    return list_var


test_car1 = copy.copy(test_car)
for i in range(10):
    for j in range(10):
        if ord[j] == i+1:
            test_car[i] = test_car1[j]
        



velocity = copy_var(1,50)
speedx = copy_var(50,10)
speedy = copy_var(0,10)
v_true = True
v_false = False
v_t = copy_var(v_true,10)
v_f1 = copy_var(v_false,10)
v_f2 = copy_var(v_false,10)
c = copy_var(1,50)
turn0 = copy_var(0,20)
turn1 = copy_var(0,20)
light1 = 'green'
light2 = 'red'
light_1 = copy_vars(light1,2)
light_2 = copy_vars(light2,2)



sum = 0


road = 'black'
light1 = 'green'
light2 = 'red'
light = {}
light['0'] = green
light['1'] = red





car = 8
sc = 5
th = 20
dt = 0

def randomness(length, num):
    randomness = []
    for i in range(length):
        randomness.append(random.randint(1,num))
    return randomness


random_int = randomness(50,50)



const_time = 1000
num_clock = 4


constant = copy_var(1,10)
print_val = True





while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



      
        
    
    screen.fill(color)


    
    
    pygame.draw.line(screen,road,start_line1,end_line1,th)
    pygame.draw.line(screen,road,start_line2,end_line2,th)
    pygame.draw.line(screen,road,start_line3,end_line3,th)
    pygame.draw.line(screen,road,start_line4,end_line4,th)
    pygame.draw.line(screen,road,start_line5,end_line5,th)
    pygame.draw.line(screen,road,start_line6,end_line6,th)

    pygame.draw.line(screen,color,start_line1,end_line1,th//2)
    pygame.draw.line(screen,color,start_line2,end_line2,th//2)
    pygame.draw.line(screen,color,start_line3,end_line3,th//2)
    pygame.draw.line(screen,color,start_line4,end_line4,th//2)
    pygame.draw.line(screen,color,start_line5,end_line5,th//2)
    pygame.draw.line(screen,color,start_line6,end_line6,th//2)




    

    sum_t =sum*const_time//1000


    w = sum % 5000 
    
    
    if w == 2500:
        random_int = randomness(50,50)





    

    pygame.draw.circle(screen,"white",vars_list[0]['16'][0],5)

    vars_list[0]['16'][0][0] += 50*dt*velocity[0]*c[0]

    if (light1 == 'green' and -30+width//6<vars_list[0]['16'][0][0]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[0]['16'][0][0]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[0]['16'][0][0]<-10+width*5//6):
        velocity[0] = 0
    else:
        velocity[0] = 1

    if vars_list[0]['16'][0][0] >= vars_list[0]['16'][1][0]:
        vars_list[0]['16'][0][0] = vars_list[4]['16'][0][0]

    if light1 == 'red':
        if 100>w>0:
            c[0] = 1.6
        if 1000>w>100:
            c[0] = 3.2
        if 2500>w>1000:
            c[0] = 1.6
    else:
        if 4000>w>2500:
            c[0] = 4/5
        if 4900>w>4000:
            c[0] = 3/5
        if 5000>w>4900:
            c[0] = 4/5


    if sum_t+random_int[0]*100>5000:
        pygame.draw.circle(screen,"white",vars_list[1]['16'][0],5)
        
        vars_list[1]['16'][0][0] += 50*dt*velocity[1]*c[1]
        
        if (light1 == 'green' and -30+width//6<vars_list[1]['16'][0][0]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[1]['16'][0][0]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[1]['16'][0][0]<-10+width*5//6):
            velocity[1] = 0
        else:
            velocity[1] = 1
        
        if vars_list[1]['16'][0][0] >= vars_list[1]['16'][1][0]:
            vars_list[1]['16'][0][0] = vars_list[4]['16'][0][0]
        
        if light1 == 'red':
            if 100>w>0:
                c[1] = 1.6
            if 1000>w>100:
                c[1] = 3.2
            if 2500>w>1000:
                c[1] = 1.6
        else:
            if 4000>w>2500:
                c[1] = 4/5
            if 4900>w>4000:
                c[1] = 3/5
            if 5000>w>4900:
                c[1] = 4/5

    if sum_t+random_int[1]*100>10000:
        pygame.draw.circle(screen,"white",vars_list[2]['16'][0],5)
        
        vars_list[2]['16'][0][0] += 50*dt*velocity[2]*c[2]
        
        if (light1 == 'green' and -30+width//6<vars_list[2]['16'][0][0]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[2]['16'][0][0]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[2]['16'][0][0]<-10+width*5//6):
            velocity[2] = 0
        else:
            velocity[2] = 1
        
        if vars_list[2]['16'][0][0] >= vars_list[2]['16'][1][0]:
            vars_list[2]['16'][0][0] = vars_list[4]['16'][0][0]
        
        if light1 == 'red':
            if 100>w>0:
                c[2] = 1.6
            if 1000>w>100:
                c[2] = 3.2
            if 2500>w>1000:
                c[2] = 1.6
        else:
            if 4000>w>2500:
                c[2] = 4/5
            if 4900>w>4000:
                c[2] = 3/5
            if 5000>w>4900:
                c[2] = 4/5



    if sum_t+random_int[2]*100>15000:
        pygame.draw.circle(screen,"white",vars_list[3]['16'][0],5)
        
        vars_list[3]['16'][0][0] += 50*dt*velocity[3]*c[3]
        
        if (light1 == 'green' and -30+width//6<vars_list[3]['16'][0][0]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[3]['16'][0][0]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[3]['16'][0][0]<-10+width*5//6):
            velocity[3] = 0
        else:
            velocity[3] = 1
        
        if vars_list[3]['16'][0][0] >= vars_list[3]['16'][1][0]:
            vars_list[3]['16'][0][0] = vars_list[4]['16'][0][0]
        
        if light1 == 'red':
            if 100>w>0:
                c[3] = 1.6
            if 1000>w>100:
                c[3] = 3.2
            if 2500>w>1000:
                c[3] = 1.6
        else:
            if 4000>w>2500:
                c[3] = 4/5
            if 4900>w>4000:
                c[3] = 3/5
            if 5000>w>4900:
                c[3] = 4/5







    




    
    pygame.draw.circle(screen,"white",vars_list[0]['61'][0],5)

    vars_list[0]['61'][0][0] += -50*dt*velocity[4]*c[4]

    if (light1 == 'green' and 30+width//6>vars_list[0]['61'][0][0]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[0]['61'][0][0]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[0]['61'][0][0]>10+width*5//6):
        velocity[4] = 0
    else:
        velocity[4] = 1

    if vars_list[0]['61'][0][0] <= vars_list[0]['61'][1][0]:
        vars_list[0]['61'][0][0] = vars_list[4]['61'][0][0]

    if light1 == 'red':
        if 100>w>0:
            c[4] = 1.6
        if 1000>w>100:
            c[4] = 3.2
        if 2500>w>1000:
            c[4] = 1.6
    else:
        if 4000>w>2500:
            c[4] = 4/5
        if 4900>w>4000:
            c[4] = 3/5
        if 5000>w>4900:
            c[4] = 4/5


    if sum_t+random_int[3]*100>5000:
        pygame.draw.circle(screen,"white",vars_list[1]['61'][0],5)
        
        vars_list[1]['61'][0][0] += -50*dt*velocity[5]*c[5]
        
        if (light1 == 'green' and 30+width//6>vars_list[1]['61'][0][0]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[1]['61'][0][0]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[1]['61'][0][0]>10+width*5//6):
            velocity[5] = 0
        else:
            velocity[5] = 1
        
        if vars_list[1]['61'][0][0] <= vars_list[1]['61'][1][0]:
            vars_list[1]['61'][0][0] = vars_list[4]['61'][0][0]
        
        if light1 == 'red':
            if 100>w>0:
                c[5] = 1.6
            if 1000>w>100:
                c[5] = 3.2
            if 2500>w>1000:
                c[5] = 1.6
        else:
            if 4000>w>2500:
                c[5] = 4/5
            if 4900>w>4000:
                c[5] = 3/5
            if 5000>w>4900:
                c[5] = 4/5

    if sum_t+random_int[4]*100>10000:
        pygame.draw.circle(screen,"white",vars_list[2]['61'][0],5)
        
        vars_list[2]['61'][0][0] += -50*dt*velocity[6]*c[6]
        
        if (light1 == 'green' and 30+width//6>vars_list[2]['61'][0][0]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[2]['61'][0][0]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[2]['61'][0][0]>10+width*5//6):
            velocity[6] = 0
        else:
            velocity[6] = 1
        
        if vars_list[2]['61'][0][0] <= vars_list[2]['61'][1][0]:
            vars_list[2]['61'][0][0] = vars_list[4]['61'][0][0]
        
        if light1 == 'red':
            if 100>w>0:
                c[6] = 1.6
            if 1000>w>100:
                c[6] = 3.2
            if 2500>w>1000:
                c[6] = 1.6
        else:
            if 4000>w>2500:
                c[6] = 4/5
            if 4900>w>4000:
                c[6] = 3/5
            if 5000>w>4900:
                c[6] = 4/5



    if sum_t+random_int[5]*100>15000:
        pygame.draw.circle(screen,"white",vars_list[3]['61'][0],5)
        
        vars_list[3]['61'][0][0] += -50*dt*velocity[7]*c[7]
        
        if (light1 == 'green' and 30+width//6>vars_list[3]['61'][0][0]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[3]['61'][0][0]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[3]['61'][0][0]>10+width*5//6):
            velocity[7] = 0
        else:
            velocity[7] = 1
        
        if vars_list[3]['61'][0][0] <= vars_list[3]['61'][1][0]:
            vars_list[3]['61'][0][0] = vars_list[4]['61'][0][0]
        
        
        if 100>w>0:
            c[7] = 1.6
        if 1000>w>100:
            c[7] = 3.2
        if 2500>w>1000:
            c[7] = 1.6
            
        if 4000>w>2500:
            c[7] = 4/5
        if 4900>w>4000:
            c[7] = 3/5
        if 5000>w>4900:
            c[7] = 4/5
    

    
 
    pygame.draw.circle(screen,"white",vars_list[0]['49'][0],5)

    vars_list[0]['49'][0][1] += 50*dt*velocity[8]*c[8]

    if (light1 != 'green' and -30+height//6<vars_list[0]['49'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[0]['49'][0][1]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[0]['49'][0][1]<-10+height*5//6):
        velocity[8] = 0
    else:
        velocity[8] = 1

    if vars_list[0]['49'][0][1] >= vars_list[0]['49'][1][1]:
        vars_list[0]['49'][0][1] = vars_list[4]['49'][0][1]

    
    if 100>w>0:
        c[8] = 4/5
    if 1000>w>100:
        c[8] = 3/5
    if 2500>w>1000:
        c[8] = 4/5

    if 4000>w>2500:
        c[8] = 1.6
    if 4900>w>4000:
        c[8] = 3.2
    if 5000>w>4900:
        c[8] = 1.6


    
    
    
    
    if sum_t + random_int[6]*100> 5000:
    
        pygame.draw.circle(screen,"white",vars_list[1]['49'][0],5)
    
        vars_list[1]['49'][0][1] += 50*dt*velocity[9]*c[9]
    
        if (light1 != 'green' and -30+height//6<vars_list[1]['49'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[1]['49'][0][1]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[1]['49'][0][1]<-10+height*5//6):
            velocity[9] = 0
        else:
            velocity[9] = 1
    
        if vars_list[1]['49'][0][1] >= vars_list[1]['49'][1][1]:
            vars_list[1]['49'][0][1] = vars_list[4]['49'][0][1]

    
    if 100>w>0:
        c[9] = 4/5
    if 1000>w>100:
        c[9] = 3/5
    if 2500>w>1000:
        c[9] = 4/5

    if 4000>w>2500:
        c[9] = 1.6
    if 4900>w>4000:
        c[9] = 3.2
    if 5000>w>4900:
        c[9] = 1.6



    if sum_t + random_int[7]*100> 10000:
    
        pygame.draw.circle(screen,"white",vars_list[2]['49'][0],5)
    
        vars_list[2]['49'][0][1] += 50*dt*velocity[10]*c[10]
    
        if (light1 != 'green' and -30+height//6<vars_list[2]['49'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[2]['49'][0][1]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[2]['49'][0][1]<-10+height*5//6):
            velocity[10] = 0
        else:
            velocity[10] = 1
    
        if vars_list[2]['49'][0][1] >= vars_list[1]['49'][1][1]:
            vars_list[2]['49'][0][1] = vars_list[4]['49'][0][1]

    
    if 100>w>0:
        c[10] = 4/5
    if 1000>w>100:
        c[10] = 3/5
    if 2500>w>1000:
        c[10] = 4/5

    if 4000>w>2500:
        c[10] = 1.6
    if 4900>w>4000:
        c[10] = 3.2
    if 5000>w>4900:
        c[10] = 1.6
    



    
            


    if sum_t + random_int[8]*100> 15000:
    
        pygame.draw.circle(screen,"white",vars_list[3]['49'][0],5)
    
        vars_list[3]['49'][0][1] += 50*dt*velocity[11]*c[11]
    
        if (light1 != 'green' and -30+height//6<vars_list[3]['49'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[3]['49'][0][1]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[3]['49'][0][1]<-10+height*5//6):
            velocity[11] = 0
        else:
            velocity[11] = 1
    
        if vars_list[3]['49'][0][1] >= vars_list[1]['49'][1][1]:
            vars_list[3]['49'][0][1] = vars_list[4]['49'][0][1]

    
    if 100>w>0:
        c[11] = 4/5
    if 1000>w>100:
        c[11] = 3/5
    if 2500>w>1000:
        c[11] = 4/5

    if 4000>w>2500:
        c[11] = 1.6
    if 4900>w>4000:
        c[11] = 3.2
    if 5000>w>4900:
        c[11] = 1.6
    



    
    if w >= 2500:
        light2 = 'red'
        light1 = 'green'
           
    else:
        light2 = 'green'
        light1 = 'red'
    





    pygame.draw.circle(screen,"white",vars_list[0]['94'][0],5)

    vars_list[0]['94'][0][1] += -50*dt*velocity[12]*c[12]

    if (light1 != 'green' and 30+height//6>vars_list[0]['94'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[0]['94'][0][1]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[0]['94'][0][1]>10+height*5//6):
        velocity[12] = 0
    else:
        velocity[12] = 1

    if vars_list[0]['94'][0][1] <= vars_list[0]['94'][1][1]:
        vars_list[0]['94'][0][1] = vars_list[4]['94'][0][1]

    
    if 100>w>0:
        c[12] = 4/5
    if 1000>w>100:
        c[12] = 3/5
    if 2500>w>1000:
        c[12] = 4/5

    if 4000>w>2500:
        c[12] = 1.6
    if 4900>w>4000:
        c[12] = 3.2
    if 5000>w>4900:
        c[12] = 1.6




    



    if sum_t+random_int[9]*100 > 5000:

        pygame.draw.circle(screen,"white",vars_list[1]['94'][0],5)
    
        vars_list[1]['94'][0][1] += -50*dt*velocity[13]*c[13]
    
        if (light1 != 'green' and 30+height//6>vars_list[1]['94'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[1]['94'][0][1]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[1]['94'][0][1]>10+height*5//6):
            velocity[13] = 0
        else:
            velocity[13] = 1
    
        if vars_list[1]['94'][0][1] <= vars_list[1]['94'][1][1]:
            vars_list[1]['94'][0][1] = vars_list[4]['94'][0][1]
    
        
        if 100>w>0:
            c[13] = 4/5
        if 1000>w>100:
            c[13] = 3/5
        if 2500>w>1000:
            c[13] = 4/5
    
        if 4000>w>2500:
            c[13] = 1.6
        if 4900>w>4000:
            c[13] = 3.2
        if 5000>w>4900:
            c[13] = 1.6



    


    if sum_t+random_int[10]*100 > 10000:

        pygame.draw.circle(screen,"white",vars_list[2]['94'][0],5)
    
        vars_list[2]['94'][0][1] += -50*dt*velocity[14]*c[14]
    
        if (light1 != 'green' and 30+height//6>vars_list[2]['94'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[2]['94'][0][1]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[2]['94'][0][1]>10+height*5//6):
            velocity[14] = 0
        else:
            velocity[14] = 1
    
        if vars_list[2]['94'][0][1] <= vars_list[1]['94'][1][1]:
            vars_list[2]['94'][0][1] = vars_list[4]['94'][0][1]
    
        
        if 100>w>0:
            c[14] = 4/5
        if 1000>w>100:
            c[14] = 3/5
        if 2500>w>1000:
            c[14] = 4/5
    
        if 4000>w>2500:
            c[14] = 1.6
        if 4900>w>4000:
            c[14] = 3.2
        if 5000>w>4900:
            c[14] = 1.6




    if sum_t+random_int[11]*100 > 15000:

        pygame.draw.circle(screen,"white",vars_list[3]['94'][0],5)
    
        vars_list[3]['94'][0][1] += -50*dt*velocity[15]*c[15]
    
        if (light1 != 'green' and 30+height//6>vars_list[3]['94'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[3]['94'][0][1]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[3]['94'][0][1]>10+height*5//6):
            velocity[15] = 0
        else:
            velocity[15] = 1
    
        if vars_list[3]['94'][0][1] <= vars_list[1]['94'][1][1]:
            vars_list[3]['94'][0][1] = vars_list[4]['94'][0][1]
    
        
        if 100>w>0:
            c[15] = 4/5
        if 1000>w>100:
            c[15] = 3/5
        if 2500>w>1000:
            c[15] = 4/5
    
        if 4000>w>2500:
            c[15] = 1.6
        if 4900>w>4000:
            c[15] = 3.2
        if 5000>w>4900:
            c[15] = 1.6

    



    pygame.draw.circle(screen,"white",vars_list[0]['03'][0],5)

    
    vars_list[0]['03'][0][1] += -50*dt*velocity[16]*c[16]

    if (light1 != 'green' and 30+height//6>vars_list[0]['03'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[0]['03'][0][1]>10+height//2):
        velocity[16] = 0
    else:
        velocity[16] = 1

    if vars_list[0]['03'][0][1] <= vars_list[0]['03'][1][1]:
        vars_list[0]['03'][0][1] = vars_list[4]['03'][0][1]

    
    if 100>w>0:
        c[16] = 4/5
    if 1000>w>100:
        c[16] = 3/5
    if 2500>w>1000:
        c[16] = 4/5

    if 4000>w>2500:
        c[16] = 1.6
    if 4900>w>4000:
        c[16] = 3.2
    if 5000>w>4900:
        c[16] = 1.6



    
    if sum_t+random_int[12]*100 > 5000:
    
        pygame.draw.circle(screen,"white",vars_list[1]['03'][0],5)
    
        
        vars_list[1]['03'][0][1] += -50*dt*velocity[17]*c[17]
    
        if (light1 != 'green' and 30+height//6>vars_list[1]['03'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[1]['03'][0][1]>10+height//2):
            velocity[17] = 0
        else:
            velocity[17] = 1
    
        if vars_list[1]['03'][0][1] <= vars_list[1]['03'][1][1]:
            vars_list[1]['03'][0][1] = vars_list[4]['03'][0][1]
    
        
        if 100>w>0:
            c[17] = 4/5
        if 1000>w>100:
            c[17] = 3/5
        if 2500>w>1000:
            c[17] = 4/5
    
        if 4000>w>2500:
            c[17] = 1.6
        if 4900>w>4000:
            c[17] = 3.2
        if 5000>w>4900:
            c[17] = 1.6




    
    if sum_t+random_int[13]*100 > 10000:
    
        pygame.draw.circle(screen,"white",vars_list[2]['03'][0],5)
    
        
        vars_list[2]['03'][0][1] += -50*dt*velocity[18]*c[18]
    
        if (light1 != 'green' and 30+height//6>vars_list[2]['03'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[2]['03'][0][1]>10+height//2):
            velocity[18] = 0
        else:
            velocity[18] = 1
    
        if vars_list[2]['03'][0][1] <= vars_list[1]['03'][1][1]:
            vars_list[2]['03'][0][1] = vars_list[4]['03'][0][1]
    
        
        if 100>w>0:
            c[18] = 4/5
        if 1000>w>100:
            c[18] = 3/5
        if 2500>w>1000:
            c[18] = 4/5
    
        if 4000>w>2500:
            c[18] = 1.6
        if 4900>w>4000:
            c[18] = 3.2
        if 5000>w>4900:
            c[18] = 1.6

    




    if sum_t+random_int[14]*100 > 15000:
    
        pygame.draw.circle(screen,"white",vars_list[3]['03'][0],5)
    
        
        vars_list[3]['03'][0][1] += -50*dt*velocity[19]*c[19]
    
        if (light1 != 'green' and 30+height//6>vars_list[3]['03'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[3]['03'][0][1]>10+height//2):
            velocity[19] = 0
        else:
            velocity[19] = 1
    
        if vars_list[3]['03'][0][1] <= vars_list[1]['03'][1][1]:
            vars_list[3]['03'][0][1] = vars_list[4]['03'][0][1]
    
        
        if 100>w>0:
            c[19] = 4/5
        if 1000>w>100:
            c[19] = 3/5
        if 2500>w>1000:
            c[19] = 4/5
    
        if 4000>w>2500:
            c[19] = 1.6
        if 4900>w>4000:
            c[19] = 3.2
        if 5000>w>4900:
            c[19] = 1.6






    
    
    pygame.draw.circle(screen,"white",vars_list[0]['30'][0],5)

    
    vars_list[0]['30'][0][1] += 50*dt*velocity[20]*c[20]

    if (light1 != 'green' and -30+height//6<vars_list[0]['30'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[0]['30'][0][1]<-10+height//2):
        velocity[20] = 0
    else:
        velocity[20] = 1

    if vars_list[0]['30'][0][1] >= vars_list[0]['30'][1][1]:
        vars_list[0]['30'][0][1] = vars_list[4]['30'][0][1]

    
    if 100>w>0:
        c[20] = 4/5
    if 1000>w>100:
        c[20] = 3/5
    if 2500>w>1000:
        c[20] = 4/5

    if 4000>w>2500:
        c[20] = 1.6
    if 4900>w>4000:
        c[20] = 3.2
    if 5000>w>4900:
        c[20] = 1.6




    if sum_t+random_int[15]*100 > 5000:
        
        pygame.draw.circle(screen,"white",vars_list[1]['30'][0],5)
    
        
        vars_list[1]['30'][0][1] += 50*dt*velocity[21]*c[21]
    
        if (light1 != 'green' and -30+height//6<vars_list[1]['30'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[1]['30'][0][1]<-10+height//2):
            velocity[21] = 0
        else:
            velocity[21] = 1
    
        if vars_list[1]['30'][0][1] >= vars_list[0]['30'][1][1]:
            vars_list[1]['30'][0][1] = vars_list[4]['30'][0][1]
    
        
        if 100>w>0:
            c[21] = 4/5
        if 1000>w>100:
            c[21] = 3/5
        if 2500>w>1000:
            c[21] = 4/5
    
        if 4000>w>2500:
            c[21] = 1.6
        if 4900>w>4000:
            c[21] = 3.2
        if 5000>w>4900:
            c[21] = 1.6



    if sum_t+random_int[16]*100 > 10000:
        
        pygame.draw.circle(screen,"white",vars_list[2]['30'][0],5)
    
        
        vars_list[2]['30'][0][1] += 50*dt*velocity[22]*c[22]
    
        if (light1 != 'green' and -30+height//6<vars_list[2]['30'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[2]['30'][0][1]<-10+height//2):
            velocity[22] = 0
        else:
            velocity[22] = 1
    
        if vars_list[2]['30'][0][1] >= vars_list[0]['30'][1][1]:
            vars_list[2]['30'][0][1] = vars_list[4]['30'][0][1]
    
        
        if 100>w>0:
            c[22] = 4/5
        if 1000>w>100:
            c[22] = 3/5
        if 2500>w>1000:
            c[22] = 4/5
    
        if 4000>w>2500:
            c[22] = 1.6
        if 4900>w>4000:
            c[22] = 3.2
        if 5000>w>4900:
            c[22] = 1.6





    if sum_t+random_int[17]*100 > 15000:
        
        pygame.draw.circle(screen,"white",vars_list[3]['30'][0],5)
    
        
        vars_list[3]['30'][0][1] += 50*dt*velocity[23]*c[23]
    
        if (light1 != 'green' and -30+height//6<vars_list[3]['30'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[3]['30'][0][1]<-10+height//2):
            velocity[23] = 0
        else:
            velocity[23] = 1
    
        if vars_list[3]['30'][0][1] >= vars_list[0]['30'][1][1]:
            vars_list[3]['30'][0][1] = vars_list[4]['30'][0][1]
    
        
        if 100>w>0:
            c[23] = 4/5
        if 1000>w>100:
            c[23] = 3/5
        if 2500>w>1000:
            c[23] = 4/5
    
        if 4000>w>2500:
            c[23] = 1.6
        if 4900>w>4000:
            c[23] = 3.2
        if 5000>w>4900:
            c[23] = 1.6






    pygame.draw.circle(screen,"white",vars_list[0]['85'][0],5)

    
    vars_list[0]['85'][0][1] += -50*dt*velocity[24]*c[24]

    if (light1 != 'green' and 30+height*5//6>vars_list[0]['85'][0][1]>10+height*5//6)or(light1 != 'green' and 30+height//2>vars_list[0]['85'][0][1]>10+height//2):
        velocity[24] = 0
    else:
        velocity[24] = 1

    if vars_list[0]['85'][0][1] <= vars_list[0]['85'][1][1]:
        vars_list[0]['85'][0][1] = vars_list[4]['85'][0][1]

    
    if 100>w>0:
        c[24] = 4/5
    if 1000>w>100:
        c[24] = 3/5
    if 2500>w>1000:
        c[24] = 4/5

    if 4000>w>2500:
        c[24] = 1.6
    if 4900>w>4000:
        c[24] = 3.2
    if 5000>w>4900:
        c[24] = 1.6




    if sum_t+random_int[25]*100 > 5000:

        pygame.draw.circle(screen,"white",vars_list[1]['85'][0],5)
    
        
        vars_list[1]['85'][0][1] += -50*dt*velocity[25]*c[25]
    
        if (light1 != 'green' and 30+height*5//6>vars_list[1]['85'][0][1]>10+height*5//6)or(light1 != 'green' and 30+height//2>vars_list[1]['85'][0][1]>10+height//2):
            velocity[25] = 0
        else:
            velocity[25] = 1
    
        if vars_list[1]['85'][0][1] <= vars_list[0]['85'][1][1]:
            vars_list[1]['85'][0][1] = vars_list[4]['85'][0][1]
    
        
        if 100>w>0:
            c[25] = 4/5
        if 1000>w>100:
            c[25] = 3/5
        if 2500>w>1000:
            c[25] = 4/5
    
        if 4000>w>2500:
            c[25] = 1.6
        if 4900>w>4000:
            c[25] = 3.2
        if 5000>w>4900:
            c[25] = 1.6





    if sum_t+random_int[26]*100 > 10000:

        pygame.draw.circle(screen,"white",vars_list[2]['85'][0],5)
    
        
        vars_list[2]['85'][0][1] += -50*dt*velocity[26]*c[26]
    
        if (light1 != 'green' and 30+height*5//6>vars_list[2]['85'][0][1]>10+height*5//6)or(light1 != 'green' and 30+height//2>vars_list[2]['85'][0][1]>10+height//2):
            velocity[26] = 0
        else:
            velocity[26] = 1
    
        if vars_list[2]['85'][0][1] <= vars_list[0]['85'][1][1]:
            vars_list[2]['85'][0][1] = vars_list[4]['85'][0][1]
    
        
        if 100>w>0:
            c[26] = 4/5
        if 1000>w>100:
            c[26] = 3/5
        if 2500>w>1000:
            c[26] = 4/5
    
        if 4000>w>2500:
            c[26] = 1.6
        if 4900>w>4000:
            c[26] = 3.2
        if 5000>w>4900:
            c[26] = 1.6





    if sum_t+random_int[27]*100 > 15000:

        pygame.draw.circle(screen,"white",vars_list[3]['85'][0],5)
    
        
        vars_list[3]['85'][0][1] += -50*dt*velocity[27]*c[27]
    
        if (light1 != 'green' and 30+height*5//6>vars_list[3]['85'][0][1]>10+height*5//6)or(light1 != 'green' and 30+height//2>vars_list[3]['85'][0][1]>10+height//2):
            velocity[27] = 0
        else:
            velocity[27] = 1
    
        if vars_list[3]['85'][0][1] <= vars_list[0]['85'][1][1]:
            vars_list[3]['85'][0][1] = vars_list[4]['85'][0][1]
    
        
        if 100>w>0:
            c[27] = 4/5
        if 1000>w>100:
            c[27] = 3/5
        if 2500>w>1000:
            c[27] = 4/5
    
        if 4000>w>2500:
            c[27] = 1.6
        if 4900>w>4000:
            c[27] = 3.2
        if 5000>w>4900:
            c[27] = 1.6






    pygame.draw.circle(screen,"white",vars_list[0]['58'][0],5)

    
    vars_list[0]['58'][0][1] += 50*dt*velocity[28]*c[28]

    if (light1 != 'green' and -30+height*5//6<vars_list[0]['58'][0][1]<-10+height*5//6)or(light1 != 'green' and -30+height//2<vars_list[0]['58'][0][1]<-10+height//2):
        velocity[28] = 0
    else:
        velocity[28] = 1

    if vars_list[0]['58'][0][1] >= vars_list[0]['58'][1][1]:
        vars_list[0]['58'][0][1] = vars_list[4]['58'][0][1]

    
    if 100>w>0:
        c[28] = 4/5
    if 1000>w>100:
        c[28] = 3/5
    if 2500>w>1000:
        c[28] = 4/5

    if 4000>w>2500:
        c[28] = 1.6
    if 4900>w>4000:
        c[28] = 3.2
    if 5000>w>4900:
        c[28] = 1.6







    if sum_t+random_int[29]*100 > 5000:

        pygame.draw.circle(screen,"white",vars_list[1]['58'][0],5)
    
        
        vars_list[1]['58'][0][1] += 50*dt*velocity[29]*c[29]
    
        if (light1 != 'green' and -30+height*5//6<vars_list[1]['58'][0][1]<-10+height*5//6)or(light1 != 'green' and -30+height//2<vars_list[1]['58'][0][1]<-10+height//2):
            velocity[29] = 0
        else:
            velocity[29] = 1
    
        if vars_list[1]['58'][0][1] >= vars_list[0]['58'][1][1]:
            vars_list[1]['58'][0][1] = vars_list[4]['58'][0][1]
    
        
        if 100>w>0:
            c[29] = 4/5
        if 1000>w>100:
            c[29] = 3/5
        if 2500>w>1000:
            c[29] = 4/5
    
        if 4000>w>2500:
            c[29] = 1.6
        if 4900>w>4000:
            c[29] = 3.2
        if 5000>w>4900:
            c[29] = 1.6







    if sum_t+random_int[30]*100 > 10000:

        pygame.draw.circle(screen,"white",vars_list[2]['58'][0],5)
    
        
        vars_list[2]['58'][0][1] += 50*dt*velocity[30]*c[30]
    
        if (light1 != 'green' and -30+height*5//6<vars_list[2]['58'][0][1]<-10+height*5//6)or(light1 != 'green' and -30+height//2<vars_list[2]['58'][0][1]<-10+height//2):
            velocity[30] = 0
        else:
            velocity[30] = 1
    
        if vars_list[2]['58'][0][1] >= vars_list[0]['58'][1][1]:
            vars_list[2]['58'][0][1] = vars_list[4]['58'][0][1]
    
        
        if 100>w>0:
            c[30] = 4/5
        if 1000>w>100:
            c[30] = 3/5
        if 2500>w>1000:
            c[30] = 4/5
    
        if 4000>w>2500:
            c[30] = 1.6
        if 4900>w>4000:
            c[30] = 3.2
        if 5000>w>4900:
            c[30] = 1.6



    if sum_t+random_int[31]*100 > 15000:

        pygame.draw.circle(screen,"white",vars_list[3]['58'][0],5)
    
        
        vars_list[3]['58'][0][1] += 50*dt*velocity[31]*c[31]
    
        if (light1 != 'green' and -30+height*5//6<vars_list[3]['58'][0][1]<-10+height*5//6)or(light1 != 'green' and -30+height//2<vars_list[3]['58'][0][1]<-10+height//2):
            velocity[31] = 0
        else:
            velocity[31] = 1
    
        if vars_list[3]['58'][0][1] >= vars_list[0]['58'][1][1]:
            vars_list[3]['58'][0][1] = vars_list[4]['58'][0][1]
    
        
        if 100>w>0:
            c[31] = 4/5
        if 1000>w>100:
            c[31] = 3/5
        if 2500>w>1000:
            c[31] = 4/5
    
        if 4000>w>2500:
            c[31] = 1.6
        if 4900>w>4000:
            c[31] = 3.2
        if 5000>w>4900:
            c[31] = 1.6


    



    pygame.draw.circle(screen,"white",vars_list[0]['27'][0],5)

    vars_list[0]['27'][0][turn0[0]] += 50*dt*velocity[32]*c[32]

    if turn0[0] == 0:
        
        
        
        if (light1 == 'green' and -30+width//6<vars_list[0]['27'][0][turn0[0]]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[0]['27'][0][turn0[0]]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[0]['27'][0][turn0[0]]<-10+width*5//6):
            velocity[32] = 0
        else:
            velocity[32] = 1

    

        if 100>w>0:
            c[32] = 1.6
        if 1000>w>100:
            c[32] = 3.2
        if 2500>w>1000:
            c[32] = 1.6
    
        if 4000>w>2500:
            c[32] = 4/5
        if 4900>w>4000:
            c[32] = 3/5
        if 5000>w>4900:
            c[32] = 4/5

    if turn0[0] == 1:

        if (light1 != 'green' and -30+height//2<vars_list[0]['27'][0][turn0[0]]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[0]['27'][0][turn0[0]]<-10+height*5//6):
            velocity[32] = 0
        else:
            velocity[32] = 1


        if 100>w>0:
            c[32] = 4/5
        if 1000>w>100:
            c[32] = 3/5
        if 2500>w>1000:
            c[32] = 4/5
    
        if 4000>w>2500:
            c[32] = 1.6
        if 4900>w>4000:
            c[32] = 3.2
        if 5000>w>4900:
            c[32] = 1.6
        
    
    
    if vars_list[0]['27'][0][0]>-10+width//2:
        turn0[0] = 1

    if vars_list[0]['27'][0][1]>10+height*5//6:
        turn0[0] = 0

    if vars_list[0]['27'][1][0] < vars_list[0]['27'][0][turn0[0]]:
        vars_list[0]['27'][0][0] = vars_list[4]['27'][0][0]
        vars_list[0]['27'][0][1] = vars_list[4]['27'][0][1]
        
        




    if sum_t+random_int[33]*100 > 6000:

        pygame.draw.circle(screen,"white",vars_list[1]['27'][0],5)
    
        vars_list[1]['27'][0][turn0[1]] += 50*dt*velocity[33]*c[33]
    
        if turn0[1] == 0:
            
            
            
            if (light1 == 'green' and -30+width//6<vars_list[1]['27'][0][turn0[1]]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[1]['27'][0][turn0[1]]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[1]['27'][0][turn0[1]]<-10+width*5//6):
                velocity[33] = 0
            else:
                velocity[33] = 1
    
        
    
            if 100>w>0:
                c[33] = 1.6
            if 1000>w>100:
                c[33] = 3.2
            if 2500>w>1000:
                c[33] = 1.6
        
            if 4000>w>2500:
                c[33] = 4/5
            if 4900>w>4000:
                c[33] = 3/5
            if 5000>w>4900:
                c[33] = 4/5
    
        if turn0[1] == 1:
    
            if (light1 != 'green' and -30+height//2<vars_list[1]['27'][0][turn0[1]]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[1]['27'][0][turn0[1]]<-10+height*5//6):
                velocity[33] = 0
            else:
                velocity[33] = 1
    
    
            if 100>w>0:
                c[33] = 4/5
            if 1000>w>100:
                c[33] = 3/5
            if 2500>w>1000:
                c[33] = 4/5
        
            if 4000>w>2500:
                c[33] = 1.6
            if 4900>w>4000:
                c[33] = 3.2
            if 5000>w>4900:
                c[33] = 1.6
            
        
        
        if vars_list[1]['27'][0][0]>-10+width//2:
            turn0[1] = 1
    
        if vars_list[1]['27'][0][1]>10+height*5//6:
            turn0[1] = 0
    
        if vars_list[1]['27'][1][0] < vars_list[1]['27'][0][turn0[1]]:
            vars_list[1]['27'][0][0] = vars_list[4]['27'][0][0]
            vars_list[1]['27'][0][1] = vars_list[4]['27'][0][1]
            
            



    if sum_t+random_int[34]*100 > 12000:

        pygame.draw.circle(screen,"white",vars_list[2]['27'][0],5)
    
        vars_list[2]['27'][0][turn0[2]] += 50*dt*velocity[34]*c[34]
    
        if turn0[2] == 0:
            
            
            
            if (light1 == 'green' and -30+width//6<vars_list[2]['27'][0][turn0[2]]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[2]['27'][0][turn0[2]]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[2]['27'][0][turn0[2]]<-10+width*5//6):
                velocity[34] = 0
            else:
                velocity[34] = 1
    
        
    
            if 100>w>0:
                c[34] = 1.6
            if 1000>w>100:
                c[34] = 3.2
            if 2500>w>1000:
                c[34] = 1.6
        
            if 4000>w>2500:
                c[34] = 4/5
            if 4900>w>4000:
                c[34] = 3/5
            if 5000>w>4900:
                c[34] = 4/5
    
        if turn0[2] == 1:
    
            if (light1 != 'green' and -30+height//2<vars_list[1]['27'][0][turn0[1]]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[1]['27'][0][turn0[1]]<-10+height*5//6):
                velocity[34] = 0
            else:
                velocity[34] = 1
    
    
            if 100>w>0:
                c[34] = 4/5
            if 1000>w>100:
                c[34] = 3/5
            if 2500>w>1000:
                c[34] = 4/5
        
            if 4000>w>2500:
                c[34] = 1.6
            if 4900>w>4000:
                c[34] = 3.2
            if 5000>w>4900:
                c[34] = 1.6
            
        
        
        if vars_list[2]['27'][0][0]>-10+width//2:
            turn0[2] = 1
    
        if vars_list[2]['27'][0][1]>10+height*5//6:
            turn0[2] = 0
    
        if vars_list[2]['27'][1][0] < vars_list[2]['27'][0][turn0[2]]:
            vars_list[2]['27'][0][0] = vars_list[4]['27'][0][0]
            vars_list[2]['27'][0][1] = vars_list[4]['27'][0][1]
            



    if sum_t+random_int[35]*100 > 18000:

        pygame.draw.circle(screen,"white",vars_list[3]['27'][0],5)
    
        vars_list[3]['27'][0][turn0[3]] += 50*dt*velocity[35]*c[35]
    
        if turn0[3] == 0:
            
            
            
            if (light1 == 'green' and -30+width//6<vars_list[3]['27'][0][turn0[3]]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[3]['27'][0][turn0[3]]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[3]['27'][0][turn0[3]]<-10+width*5//6):
                velocity[35] = 0
            else:
                velocity[35] = 1
    
        
    
            if 100>w>0:
                c[35] = 1.6
            if 1000>w>100:
                c[35] = 3.2
            if 2500>w>1000:
                c[35] = 1.6
        
            if 4000>w>2500:
                c[35] = 4/5
            if 4900>w>4000:
                c[35] = 3/5
            if 5000>w>4900:
                c[35] = 4/5
    
        if turn0[3] == 1:
    
            if (light1 != 'green' and -30+height//2<vars_list[3]['27'][0][turn0[3]]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[3]['27'][0][turn0[3]]<-10+height*5//6):
                velocity[35] = 0
            else:
                velocity[35] = 1
    
    
            if 100>w>0:
                c[35] = 4/5
            if 1000>w>100:
                c[35] = 3/5
            if 2500>w>1000:
                c[35] = 4/5
        
            if 4000>w>2500:
                c[35] = 1.6
            if 4900>w>4000:
                c[35] = 3.2
            if 5000>w>4900:
                c[35] = 1.6
            
        
        
        if vars_list[3]['27'][0][0]>-10+width//2:
            turn0[3] = 1
    
        if vars_list[3]['27'][0][1]>10+height*5//6:
            turn0[3] = 0
    
        if vars_list[3]['27'][1][0] < vars_list[3]['27'][0][turn0[3]]:
            vars_list[3]['27'][0][0] = vars_list[4]['27'][0][0]
            vars_list[3]['27'][0][1] = vars_list[4]['27'][0][1]
            




    pygame.draw.circle(screen,"white",vars_list[0]['72'][0],5)

    vars_list[0]['72'][0][turn0[4]] += -50*dt*velocity[36]*c[36]
    
    if turn0[4] == 0:
        
        
        
        if (light1 == 'green' and 30+width//6>vars_list[0]['72'][0][turn0[4]]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[0]['72'][0][turn0[4]]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[0]['72'][0][turn0[4]]>10+width*5//6):
            velocity[36] = 0
        else:
            velocity[36] = 1

    

        if 100>w>0:
            c[36] = 1.6
        if 1000>w>100:
            c[36] = 3.2
        if 2500>w>1000:
            c[36] = 1.6
    
        if 4000>w>2500:
            c[36] = 4/5
        if 4900>w>4000:
            c[36] = 3/5
        if 5000>w>4900:
            c[36] = 4/5

    if turn0[4] == 1:

        if (light1 != 'green' and 30+height//2>vars_list[0]['72'][0][turn0[4]]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[0]['72'][0][turn0[4]]>10+height*5//6):
            velocity[36] = 0
        else:
            velocity[36] = 1


        if 100>w>0:
            c[36] = 4/5
        if 1000>w>100:
            c[36] = 3/5
        if 2500>w>1000:
            c[36] = 4/5
    
        if 4000>w>2500:
            c[36] = 1.6
        if 4900>w>4000:
            c[36] = 3.2
        if 5000>w>4900:
            c[36] = 1.6
    
    
    
    if vars_list[0]['72'][0][0]<10+width//2 :
        turn0[4] = 1
    
    if vars_list[0]['72'][0][1]<-10+height//6 :
        turn0[4] = 0
    
    if vars_list[0]['72'][1][0] > vars_list[0]['72'][0][turn0[4]]:
        vars_list[0]['72'][0][0] = vars_list[4]['72'][0][0]
        vars_list[0]['72'][0][1] = vars_list[4]['72'][0][1]
        



    if sum_t+random_int[37]*100 > 6000:

    
        pygame.draw.circle(screen,"white",vars_list[1]['72'][0],5)
    
        vars_list[1]['72'][0][turn0[5]] += -50*dt*velocity[37]*c[37]
        
        if turn0[5] == 0:
            
            
            
            if (light1 == 'green' and 30+width//6>vars_list[1]['72'][0][turn0[5]]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[1]['72'][0][turn0[5]]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[1]['72'][0][turn0[5]]>10+width*5//6):
                velocity[37] = 0
            else:
                velocity[37] = 1
    
        
    
            if 100>w>0:
                c[37] = 1.6
            if 1000>w>100:
                c[37] = 3.2
            if 2500>w>1000:
                c[37] = 1.6
        
            if 4000>w>2500:
                c[37] = 4/5
            if 4900>w>4000:
                c[37] = 3/5
            if 5000>w>4900:
                c[37] = 4/5
    
        if turn0[5] == 1:
    
            if (light1 != 'green' and 30+height//2>vars_list[1]['72'][0][turn0[5]]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[1]['72'][0][turn0[5]]>10+height*5//6):
                velocity[37] = 0
            else:
                velocity[37] = 1
    
    
            if 100>w>0:
                c[37] = 4/5
            if 1000>w>100:
                c[37] = 3/5
            if 2500>w>1000:
                c[37] = 4/5
        
            if 4000>w>2500:
                c[37] = 1.6
            if 4900>w>4000:
                c[37] = 3.2
            if 5000>w>4900:
                c[37] = 1.6
        
        
        
        if vars_list[1]['72'][0][0]<10+width//2 :
            turn0[5] = 1
        
        if vars_list[1]['72'][0][1]<-10+height//6 :
            turn0[5] = 0
        
        if vars_list[1]['72'][1][0] > vars_list[1]['72'][0][turn0[5]]:
            vars_list[1]['72'][0][0] = vars_list[4]['72'][0][0]
            vars_list[1]['72'][0][1] = vars_list[4]['72'][0][1]
            





    if sum_t+random_int[38]*100 > 12000:

    
        pygame.draw.circle(screen,"white",vars_list[2]['72'][0],5)
    
        vars_list[2]['72'][0][turn0[6]] += -50*dt*velocity[38]*c[38]
        
        if turn0[6] == 0:
            
            
            
            if (light1 == 'green' and 30+width//6>vars_list[2]['72'][0][turn0[6]]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[2]['72'][0][turn0[6]]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[2]['72'][0][turn0[6]]>10+width*5//6):
                velocity[38] = 0
            else:
                velocity[38] = 1
    
        
    
            if 100>w>0:
                c[38] = 1.6
            if 1000>w>100:
                c[38] = 3.2
            if 2500>w>1000:
                c[38] = 1.6
        
            if 4000>w>2500:
                c[38] = 4/5
            if 4900>w>4000:
                c[38] = 3/5
            if 5000>w>4900:
                c[38] = 4/5
    
        if turn0[6] == 1:
    
            if (light1 != 'green' and 30+height//2>vars_list[2]['72'][0][turn0[6]]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[2]['72'][0][turn0[6]]>10+height*5//6):
                velocity[37] = 0
            else:
                velocity[37] = 1
    
    
            if 100>w>0:
                c[38] = 4/5
            if 1000>w>100:
                c[38] = 3/5
            if 2500>w>1000:
                c[38] = 4/5
        
            if 4000>w>2500:
                c[38] = 1.6
            if 4900>w>4000:
                c[38] = 3.2
            if 5000>w>4900:
                c[38] = 1.6
        
        
        
        if vars_list[2]['72'][0][0]<10+width//2 :
            turn0[6] = 1
        
        if vars_list[2]['72'][0][1]<-10+height//6 :
            turn0[6] = 0
        
        if vars_list[2]['72'][1][0] > vars_list[2]['72'][0][turn0[6]]:
            vars_list[2]['72'][0][0] = vars_list[4]['72'][0][0]
            vars_list[2]['72'][0][1] = vars_list[4]['72'][0][1]
            


    if sum > 300:
        

        for i in range(10):
            if ord[i] == 1 and test_car[i]:
        
                pygame.draw.circle(screen,"orange",vars_list[5]['16'][0],car)
            
                vars_list[5]['16'][0][0] += 50*dt*velocity[39]*c[39]
            
                if (light1 == 'green' and -30+width//6<vars_list[5]['16'][0][0]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[5]['16'][0][0]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[5]['16'][0][0]<-10+width*5//6):
                    velocity[39] = 0
                else:
                    velocity[39] = 1
            
                if vars_list[5]['16'][0][0] >= vars_list[0]['16'][1][0]:
                    vars_list[5]['16'][0][0] = vars_list[4]['16'][0][0]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                        
                    
            
                if light1 == 'red':
                    if 100>w>0:
                        c[39] = 1.6
                        val = True
                    if 1000>w>100:
                        c[39] = 3.2
                    if 2500>w>1000:
                        c[39] = 1.6
                else:
                    if 4000>w>2500:
                        val = False
                        c[39] = 4/5
                    if 4900>w>4000:
                        c[39] = 3/5
                    if 5000>w>4900:
                        c[39] = 4/5

                val1 = False
                val2 = True


        
        for i in range(10):
    
            if ord[i] == 2 and test_car[i]:

                pygame.draw.circle(screen,"orange",vars_list[5]['61'][0],car)
    
                vars_list[5]['61'][0][0] += -50*dt*velocity[40]*c[40]
            
                if (light1 == 'green' and 30+width//6>vars_list[5]['61'][0][0]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[5]['61'][0][0]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[5]['61'][0][0]>10+width*5//6):
                    velocity[40] = 0
                else:
                    velocity[40] = 1
            
                if vars_list[5]['61'][0][0] <= vars_list[0]['61'][1][0]:
                    vars_list[5]['61'][0][0] = vars_list[4]['61'][0][0]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                    
                if light1 == 'red':
                    if 100>w>0:
                        val = True
                        c[40] = 1.6
                    if 1000>w>100:
                        c[40] = 3.2
                    if 2500>w>1000:
                        c[40] = 1.6
                else:
                    if 4000>w>2500:
                        val = False
                        c[40] = 4/5
                    if 4900>w>4000:
                        c[40] = 3/5
                    if 5000>w>4900:
                        c[40] = 4/5


                
                

        
        for i in range(10):
            if ord[i] == 3 and test_car[i]:

                pygame.draw.circle(screen,"orange",vars_list[5]['49'][0],car)
    
                vars_list[5]['49'][0][1] += 50*dt*velocity[41]*c[41]
            
                if (light1 != 'green' and -30+height//6<vars_list[5]['49'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[5]['49'][0][1]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[5]['49'][0][1]<-10+height*5//6):
                    velocity[41] = 0
                else:
                    velocity[41] = 1
            
                if vars_list[5]['49'][0][1] >= vars_list[0]['49'][1][1]:
                    vars_list[5]['49'][0][1] = vars_list[4]['49'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
            
                
                if 100>w>0:
                    c[41] = 4/5
                    val = False
                if 1000>w>100:
                    c[41] = 3/5
                if 2500>w>1000:
                    c[41] = 4/5
            
                if 4000>w>2500:
                    val =  True
                    c[41] = 1.6
                if 4900>w>4000:
                    c[41] = 3.2
                if 5000>w>4900:
                    c[41] = 1.6


                
                

        
        for i in range(10):

            if ord[i] == 4 and test_car[i]:
             
                
            
                pygame.draw.circle(screen,"orange",vars_list[5]['94'][0],car)
            
                vars_list[5]['94'][0][1] += -50*dt*velocity[42]*c[42]
            
                if (light1 != 'green' and 30+height//6>vars_list[5]['94'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[5]['94'][0][1]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[5]['94'][0][1]>10+height*5//6):
                    velocity[42] = 0
                else:
                    velocity[42] = 1
            
                if vars_list[5]['94'][0][1] <= vars_list[0]['94'][1][1]:
                    vars_list[5]['94'][0][1] = vars_list[4]['94'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                
                if 100>w>0:
                    c[42] = 4/5
                    val = False
                if 1000>w>100:
                    c[42] = 3/5
                if 2500>w>1000:
                    c[42] = 4/5
            
                if 4000>w>2500:
                    val = True
                    c[42] = 1.6
                if 4900>w>4000:
                    c[42] = 3.2
                if 5000>w>4900:
                    c[42] = 1.6







        for i in range(10):
            if ord[i] == 5 and test_car[i]:


                
                            
                pygame.draw.circle(screen,"orange",vars_list[5]['03'][0],car)
            
                
                vars_list[5]['03'][0][1] += -50*dt*velocity[43]*c[43]
            
                if (light1 != 'green' and 30+height//6>vars_list[5]['03'][0][1]>10+height//6)or(light1 != 'green' and 30+height//2>vars_list[5]['03'][0][1]>10+height//2):
                    velocity[43] = 0
                else:
                    velocity[43] = 1
            
                if vars_list[5]['03'][0][1] <= vars_list[0]['03'][1][1]:
                    vars_list[5]['03'][0][1] = vars_list[4]['03'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                
                if 100>w>0:
                    c[43] = 4/5
                    val = False
                if 1000>w>100:
                    c[43] = 3/5
                if 2500>w>1000:
                    c[43] = 4/5
            
                if 4000>w>2500:
                    val = True
                    c[43] = 1.6
                if 4900>w>4000:
                    c[43] = 3.2
                if 5000>w>4900:
                    c[43] = 1.6

                
            
                        
            


        for i in range(10):
            if ord[i] == 6 and test_car[i]:

                            
                pygame.draw.circle(screen,"orange",vars_list[5]['30'][0],car)
            
                
                vars_list[5]['30'][0][1] += 50*dt*velocity[44]*c[44]
            
                if (light1 != 'green' and -30+height//6<vars_list[5]['30'][0][1]<-10+height//6)or(light1 != 'green' and -30+height//2<vars_list[5]['30'][0][1]<-10+height//2):
                    velocity[44] = 0
                else:
                    velocity[44] = 1
            
                if vars_list[5]['30'][0][1] >= vars_list[0]['30'][1][1]:
                    vars_list[5]['30'][0][1] = vars_list[4]['30'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
            
                
                if 100>w>0:
                    c[44] = 4/5
                    val = False
                if 1000>w>100:
                    c[44] = 3/5
                if 2500>w>1000:
                    c[44] = 4/5
            
                if 4000>w>2500:
                    c[44] = 1.6
                    val = True
                if 4900>w>4000:
                    c[44] = 3.2
                if 5000>w>4900:
                    c[44] = 1.6


               
            


        for i in range(10):
            if ord[i] == 7 and test_car[i]:


                pygame.draw.circle(screen,"orange",vars_list[5]['85'][0],car)
            
                
                vars_list[5]['85'][0][1] += -50*dt*velocity[45]*c[45]
            
                if (light1 != 'green' and 30+height*5//6>vars_list[5]['85'][0][1]>10+height*5//6)or(light1 != 'green' and 30+height//2>vars_list[5]['85'][0][1]>10+height//2):
                    velocity[45] = 0
                else:
                    velocity[45] = 1
            
                if vars_list[5]['85'][0][1] <= vars_list[0]['85'][1][1]:
                    vars_list[5]['85'][0][1] = vars_list[4]['85'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                
                if 100>w>0:
                    c[45] = 4/5
                    val = False
                if 1000>w>100:
                    c[45] = 3/5
                if 2500>w>1000:
                    c[45] = 4/5
            
                if 4000>w>2500:
                    val = True
                    c[45] = 1.6
                if 4900>w>4000:
                    c[45] = 3.2
                if 5000>w>4900:
                    c[45] = 1.6




        for i in range(10):
            if ord[i] == 8 and test_car[i]:


                            
            
                pygame.draw.circle(screen,"orange",vars_list[5]['58'][0],car)
            
                
                vars_list[5]['58'][0][1] += 50*dt*velocity[46]*c[46]
            
                if (light1 != 'green' and -30+height*5//6<vars_list[5]['58'][0][1]<-10+height*5//6)or(light1 != 'green' and -30+height//2<vars_list[5]['58'][0][1]<-10+height//2):
                    velocity[46] = 0
                else:
                    velocity[46] = 1
            
                if vars_list[5]['58'][0][1] >= vars_list[0]['58'][1][1]:
                    vars_list[5]['58'][0][1] = vars_list[4]['58'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
            
                
                if 100>w>0:
                    c[46] = 4/5
                    val = False
                if 1000>w>100:
                    c[46] = 3/5
                if 2500>w>1000:
                    c[46] = 4/5
            
                if 4000>w>2500:
                    c[46] = 1.6
                    val = True
                if 4900>w>4000:
                    c[46] = 3.2
                if 5000>w>4900:
                    c[46] = 1.6


       

                


        for i in range(10):
            if ord[i] == 9 and test_car[i]:


            
                pygame.draw.circle(screen,"orange",vars_list[5]['27'][0],car)
            
                vars_list[5]['27'][0][turn1[0]] += 50*dt*velocity[47]*c[47]
            
                if turn1[0] == 0:
                    
                    
                    
                    if (light1 == 'green' and -30+width//6<vars_list[5]['27'][0][turn1[0]]<-10+width//6)or(light1 == 'green' and -30+width//2<vars_list[5]['27'][0][turn1[0]]<-10+width//2)or(light1 == 'green' and -30+width*5//6<vars_list[5]['27'][0][turn1[0]]<-10+width*5//6):
                        velocity[47] = 0
                    else:
                        velocity[47] = 1
            
                
            
                    if 100>w>0:
                        c[47] = 1.6
                        val = True
                    if 1000>w>100:
                        c[47] = 3.2
                    if 2500>w>1000:
                        c[47] = 1.6
                
                    if 4000>w>2500:
                        c[47] = 4/5
                        val = False
                    if 4900>w>4000:
                        c[47] = 3/5
                    if 5000>w>4900:
                        c[47] = 4/5
                        

                    


                
            
                if turn1[0] == 1:
            
                    if (light1 != 'green' and -30+height//2<vars_list[5]['27'][0][turn1[0]]<-10+height//2)or(light1 != 'green' and -30+height*5//6<vars_list[5]['27'][0][turn1[0]]<-10+height*5//6):
                        velocity[47] = 0
                    else:
                        velocity[47] = 1
            
            
                    if 100>w>0:
                        c[47] = 4/5
                        val = False
                    if 1000>w>100:
                        c[47] = 3/5
                    if 2500>w>1000:
                        c[47] = 4/5
                
                    if 4000>w>2500:
                        c[47] = 1.6
                        val = True
                    if 4900>w>4000:
                        c[47] = 3.2
                    if 5000>w>4900:
                        c[47] = 1.6

                    
                    
                
                
                if vars_list[5]['27'][0][0]>-10+width//2:
                    turn1[0] = 1
            
                if vars_list[5]['27'][0][1]>10+height*5//6:
                    turn1[0] = 0
            
                if vars_list[5]['27'][1][0] < vars_list[5]['27'][0][turn0[0]]:
                    vars_list[5]['27'][0][0] = vars_list[4]['27'][0][0]
                    vars_list[5]['27'][0][1] = vars_list[4]['27'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True


        for i in range(10):
            if ord[i] == 10 and test_car[i]:

                

                
                pygame.draw.circle(screen,"orange",vars_list[5]['72'][0],car)
            
                vars_list[5]['72'][0][turn1[2]] += -50*dt*velocity[48]*c[48]
                
                if turn1[1] == 0:
                    
                    
                    
                    if (light1 == 'green' and 30+width//6>vars_list[5]['72'][0][turn1[1]]>10+width//6)or(light1 == 'green' and 30+width//2>vars_list[5]['72'][0][turn1[1]]>10+width//2)or(light1 == 'green' and 30+width*5//6>vars_list[5]['72'][0][turn1[1]]>10+width*5//6):
                        velocity[48] = 0
                    else:
                        velocity[48] = 1
            
                
            
                    if 100>w>0:
                        c[48] = 1.6
                        val = True
                    if 1000>w>100:
                        c[48] = 3.2
                    if 2500>w>1000:
                        c[48] = 1.6
                
                    if 4000>w>2500:
                        c[48] = 4/5
                        val = False
                    if 4900>w>4000:
                        c[48] = 3/5
                    if 5000>w>4900:
                        c[48] = 4/5


                    

                
            
                if turn1[1] == 1:
            
                    if (light1 != 'green' and 30+height//2>vars_list[5]['72'][0][turn1[1]]>10+height//2)or(light1 != 'green' and 30+height*5//6>vars_list[5]['72'][0][turn1[1]]>10+height*5//6):
                        velocity[48] = 0
                    else:
                        velocity[48] = 1
            
            
                    if 100>w>0:
                        c[48] = 4/5
                        val = False
                    if 1000>w>100:
                        c[48] = 3/5
                    if 2500>w>1000:
                        c[48] = 4/5
                
                    if 4000>w>2500:
                        c[48] = 1.6
                        val = True
                    if 4900>w>4000:
                        c[48] = 3.2
                    if 5000>w>4900:
                        c[48] = 1.6
                        

                    


                    
                
                
                
                if vars_list[5]['72'][0][0]<10+width//2 :
                    turn1[1] = 1
                
                if vars_list[5]['72'][0][1]<-10+height//6 :
                    turn1[1] = 0
                
                if vars_list[5]['72'][1][0] > vars_list[5]['72'][0][turn1[1]]:
                    vars_list[5]['72'][0][0] = vars_list[4]['72'][0][0]
                    vars_list[5]['72'][0][1] = vars_list[4]['72'][0][1]
                    test_car[i] = False
                    if i < 9:
                        test_car[ord[i+1]-1] = True
                    else:
                        test_car[ord[0]] = True
                    
                                


    
    
    if w >= 2500:

        
        
        light1 = 'green'
        
        if 5000>w>4500:
            light['0'] = 'yellow'
        if 4500>w>2500:
            light['0'] = 'green'
        
        
        light2 = 'red'
        light['1'] = 'red'
           
    if not w >= 2500:

        
        light2 = 'green'
        if 2500>w>2000:
            light['1'] = 'yellow'
        if not 2500>w>2000:
            light['1'] = 'green'

        
        
        light['0'] = 'red'
        light1 = 'red'

    if 3000 < w < 4000 or 1000 < w < 2000:
        print_val = True

    if 2510 > w > 2500 or 10 > w > 0:
        if print_val:
            
            print_val = False
        
        


        
        

    
    pygame.draw.circle(screen,light['0'],(width/6,10+height/2), sc)
    pygame.draw.circle(screen,light['0'],(width/6,-10+height/2), sc)
    pygame.draw.circle(screen,light['1'],(10+width/6,height/2), sc)
    pygame.draw.circle(screen,light['1'],(-10+width/6,height/2), sc)
    
    pygame.draw.circle(screen,light['0'],(width/2,10+height/2), sc)
    pygame.draw.circle(screen,light['0'],(width/2,-10+height/2), sc)
    pygame.draw.circle(screen,light['1'],(10+width/2,height/2), sc)
    pygame.draw.circle(screen,light['1'],(-10+width/2,height/2), sc)

    pygame.draw.circle(screen,light['0'],(width/6,10+height/6), sc)
    pygame.draw.circle(screen,light['0'],(width/6,-10+height/6), sc)
    pygame.draw.circle(screen,light['1'],(10+width/6,height/6), sc)
    pygame.draw.circle(screen,light['1'],(-10+width/6,height/6), sc)

    pygame.draw.circle(screen,light['0'],(width/2,10+height/6), sc)
    pygame.draw.circle(screen,light['0'],(width/2,-10+height/6), sc)
    pygame.draw.circle(screen,light['1'],(-10+width/2,height/6), sc)

    pygame.draw.circle(screen,light['0'],(width/2,10+height*5/6), sc)
    pygame.draw.circle(screen,light['0'],(width/2,-10+height*5/6), sc)
    pygame.draw.circle(screen,light['1'],(10+width/2,height*5/6), sc)
    
    pygame.draw.circle(screen,light['0'],(width*5/6,10+height/2), sc)
    pygame.draw.circle(screen,light['0'],(width*5/6,-10+height/2), sc)
    pygame.draw.circle(screen,light['1'],(10+width*5/6,height/2), sc)
    pygame.draw.circle(screen,light['1'],(-10+width*5/6,height/2), sc)

    pygame.draw.circle(screen,light['0'],(width*5/6,10+height*5/6), sc)
    pygame.draw.circle(screen,light['0'],(width*5/6,-10+height*5/6), sc)
    pygame.draw.circle(screen,light['1'],(10+width*5/6,height*5/6), sc)
    pygame.draw.circle(screen,light['1'],(-10+width*5/6,height*5/6), sc)
    
    



    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        const_time = 5000

    if keys[pygame.K_2]:
        const_time = 3500
        
    if keys[pygame.K_3]:
        const_time = 3000

    if keys[pygame.K_4]:
        const_time = 1500

    if keys[pygame.K_5]:
        const_time = 1000



    pygame.display.flip()

    num = clock.tick(60)//num_clock
    
    dt = num/const_time
        
    sum += int(num)


pygame.quit()
ser.close()
