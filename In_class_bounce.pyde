

def setup():
    size(600,600)
    global ball_y
    ball_y = random(550)
    global ball_x
    ball_x = random(550)
    global y_speed
    y_speed = random(2,6)
    global x_speed
    x_speed = random(2,6)
    
    global brick1
    global brick2
    global brick3
    global brick4
    
    brick1 = True
    brick2 = True
    brick3 = True
    brick4 = True
    
    
   
    
def draw():
    background(200)
    #noStroke()
    global ball_y
    global ball_x
    global y_speed
    global x_speed
    
    global brick1
    global brick2
    global brick3
    global brick4
  
    #fill(200,56,98)
    ellipse(ball_x,ball_y,20,20)
    #line(0,400,600,400)]
    
     #paddle
    rect(mouseX - 50,500,100,10)
           
    ball_y = ball_y + y_speed
    ball_x = ball_x + x_speed
    
       
    #ball hit the bottom of the floor
    if(ball_y > 600):
         print("Hit the floor")
         y_speed = -4
         
    #ball hit the ceiling
    elif(ball_y < 10):
        
        print("Hit the Top")
        y_speed = 4
         #range(start, end)
         
       #ball hit the right wall
    if(ball_x > 600):
         print("Hit the Line")
         x_speed = -4
         #ball hit the left wall
    elif(ball_x < 0):
        
        print("Hit the Top")
        x_speed = 4
         #range(start, end)
         
    
    if brick1 == True:
        noStroke()
        fill(0)
        rect(0,0,150,30)
        
    if brick2 == True:
        rect(150,0,150,30)
        
    if brick3 == True:
        rect(300,0,150,30)
        
    if brick4 == True:
        rect(450,0,150,30)
        
    #when ball hit bricks
    if(ball_x > 0 and ball_x < 150):
        if ball_y < 30:
            print("false1")
            
            
            brick1 = False
            
    if(ball_x > 150 and ball_x < 300):
        if ball_y < 30:
            print("false2")
            brick2 = False
            
            
    if(ball_x > 300 and ball_x < 450):
        if ball_y < 30:
            print("false3")
            brick3 = False
            
            
    if(ball_x >450 and ball_x < 600):
        if ball_y < 30:
            print("false4")
            brick4 = False
           
        

 
   
  
    
    
    #ball hitting the paddle
    if (ball_x > mouseX and ball_x < mouseX + 60 and ball_x > mouseX and ball_x > mouseX - 60 ):
        if ball_y > 500:
            y_speed = -y_speed
            x_speed = -x_speed
            
  
        
 
    
    
    
    
