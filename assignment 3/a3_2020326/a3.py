import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.a=A.transpose()
        self.old=None
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        
        self.old=np.copy(self.a)
        Shape.translate(self,dx,dy)
        self.a=np.dot(self.T_t,self.a)
        return (np.round(self.a[0],2),np.round(self.a[1],2))

    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        self.old=np.copy(self.a)
        a=np.sum(self.a[0])/len(self.a[0])
        b=np.sum(self.a[1])/len(self.a[1])
        Shape.translate(self,-a,-b)
        self.a=np.dot(self.T_t,self.a)
        Shape.scale(self,sx,sy)
        self.a=np.dot(self.T_s,self.a)
        Shape.translate(self,a,b)
        self.a=np.dot(self.T_t,self.a)
        return (np.round(self.a[0],2),np.round(self.a[1],2))
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        
        self.old=np.copy(self.a)
        if rx==0 and ry==0:
            Shape.rotate(self,deg)
            self.a=np.dot(self.T_r,self.a)
            
        else:
            Shape.translate(self,-rx,-ry)
            self.a=np.dot(self.T_t,self.a)
            Shape.rotate(self,deg)
            self.a=np.dot(self.T_r,self.a)
            Shape.translate(self,rx,ry)
            self.a=np.dot(self.T_t,self.a)
            
        return (np.round(self.a[0],2),np.round(self.a[1],2))
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        
        xp=self.old[0]
        yp=self.old[1]
        plt.plot(xp,yp,linestyle='dashed',marker='o')
        x=self.a[0]
        y=self.a[1]
        plt.plot(x,y,marker='o')
        c1=xp[0]
        c2=yp[0]
        for i in range(len(xp)):
            if abs(xp[i])>c1:
                c1=abs(xp[i])
        for i in range(len(x)):
            if abs(x[i])>c1:
                c1=abs(x[i])
        for j in range(len(yp)):
            if abs(yp[j])>c2:
                c2=abs(yp[j])
        for j in range(len(y)):
            if abs(y[j])>c2:
                c2=abs(y[j])
        Shape.plot(self,c1,c2)


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.a=np.array([x,y,1])
        self.r=radius
        self.old=None
        self.ort=None

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        
        self.old=np.copy(self.a)
        self.ort=float(self.r)
        Shape.translate(self,dx,dy)
        self.a=np.dot(self.T_t,self.a)
        c=(np.round(self.a[0],2),np.round(self.a[1],2),np.round(self.r,2))
        return c
        
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.old=np.copy(self.a)
        self.ort=float(self.r)
        self.r=self.r*sx
        return (np.round(self.a[0],2),np.round(self.a[1],2),np.round(self.r,2))
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.old=np.copy(self.a)
        self.ort=float(self.r)
        if rx==0 and ry==0:
            Shape.rotate(self,deg)
            self.a=np.dot(self.T_r,self.a)
            d=(np.round(self.a[0],2),np.round(self.a[1],2),np.round(self.r,2))
            return d
        else:
            Shape.translate(self,-rx,-ry)
            self.a=np.dot(self.T_t,self.a)
            Shape.rotate(self,deg)
            self.a=np.dot(self.T_r,self.a)
            Shape.translate(self,rx,ry)
            self.a=np.dot(self.T_t,self.a)
            d=(np.round(self.a[0],2),np.round(self.a[1],2),np.round(self.r,2))
            return d
            
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
      
        
        fig,ax=plt.subplots()
        ci=plt.Circle((self.old[0],self.old[1]),self.ort,linestyle='dashed',fill=False)
        cir=plt.Circle((self.a[0],self.a[1]),self.r,fill=False)
        ax.set_aspect(1)
        ax.add_patch(ci)
        ax.add_patch(cir)
        ax.add_artist(ci)
        ax.add_artist(cir)
        d=max(abs(self.a[0])+self.r,abs(self.old[0])+self.ort)
        e=max(abs(self.a[1])+self.r,abs(self.old[1])+self.ort)
        Shape.plot(self,d,e)
        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    v=int(input("verbose? 1 to plot, 0 otherwise:"))
    if v==0:
        t=int(input("enter no of test cases"))
        for i in range(t):
            fi=int(input("enter type of shape(0 for polygon or 1 for circle)"))
            if fi==0:
                s=int(input("enter the number of sides"))
                l=[]
                for j in range(s):
                    p=input("enter space separated x and y coordinates")
                    p=list(p.split())
                    c=[float(p[0]),float(p[1]),float(1)]
                    l.append(c)
                a=np.array(l)
                p=Polygon(a)
                n=int(input("enter number of queries"))
                print('''
                Enter Query:
                a) R theta (rx) (ry)               
                b) S sx (sy) 
                c) T dx (dy)
                d) P
                ''')
                for j in range(n):
                    q=input()
                    q=list(q.split())
                    if q[0]=='T' or q[0]=='t':
                        if len(q)==2:
                            q.append(float(q[1]))
                            q[1]=float(q[1])
                        out=p.translate(float(q[1]),float(q[2]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                    elif q[0]=='S' or q[0]=='s':
                        if len(q)==2:
                            q.append(float(q[1]))
                            q[1]=float(q[1])
                        out=p.scale(float(q[1]),float(q[2]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                    elif q[0]=='R' or q[0]=='r':
                        q[1]=float(q[1])
                        if len(q)==2:
                            out=p.rotate(float(q[1]))
                        elif len(q)==3:
                            q[2]=float(q[2])
                            out=p.rotate(float(q[1]),float(q[2]))
                        else:
                            q[2]=float(q[2])
                            q[3]=float(q[3])
                            out=p.rotate(float(q[1]),float(q[2]),float(q[3]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                    elif q[0]=='P' or q[0]=='p':
                        p.plot()
                    else:
                        print("incorrect query code: Please try again")
            elif fi==1:
                c=input("enter space separated x,y coordinates and radius r of circle")
                c=list(c.split())
                if len(c)==0:
                    ci=Circle()
                elif len(c)==1:
                    ci=Circle(float(c[0]))
                elif len(c)==2:
                    ci=Circle(float(c[0]),float(c[1]))
                else:
                    ci=Circle(float(c[0]),float(c[1]),float(c[2]))
                n=int(input("enter number of queries"))
                print('''
                Enter Query:
                a) R theta (rx) (ry) 
                b) S sr 
                c) T dx (dy) 
                d) P 
                ''')
                for j in range(n):
                    q=input()
                    q=list(q.split())
                    if q[0]=='T' or q[0]=='t':
                        if len(q)==2:
                            q[1]=float(q[1])
                            q.append(float(q[1]))
                        out=ci.translate(float(q[1]),float(q[2]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                    elif q[0]=='S' or q[0]=='s':
                        out=ci.scale(float(q[1]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                    elif q[0]=='R' or q[0]=='r':
                        if len(q)==2:
                            out=ci.rotate(float(q[1]))
                        elif len(q)==3:
                            out=ci.rotate(float(q[1]),float(q[2]))
                        else:
                            out=ci.rotate(float(q[1]),float(q[2]),float(q[3]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                    elif q[0]=='P' or q[0]=='p':
                        ci.plot()
                    else:
                        print("incorrect query code: please try again")
                            
    elif v==1:
        t=int(input("enter no of test cases"))
        for i in range(t):
            fi=int(input("enter type of shape(0 for polygon or 1 for circle)"))
            if fi==0:
                s=int(input("enter the number of sides"))
                l=[]
                for j in range(s):
                    p=input("enter space separated x and y coordinates")
                    p=list(p.split())
                    c=[float(p[0]),float(p[1]),float(1)]
                    l.append(c)
                a=np.array(l)
                p=Polygon(a)
                n=int(input("enter number of queries"))
                print('''
                Enter Query:
                a) R theta (rx) (ry)               
                b) S sx (sy) 
                c) T dx (dy)
                ''')
                for j in range(n):
                    q=input()
                    q=list(q.split())
                    if q[0]=='T' or q[0]=='t':
                        if len(q)==2:
                            q.append(float(q[1]))
                            q[1]=float(q[1])
                        out=p.translate(float(q[1]),float(q[2]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                        p.plot()
                    elif q[0]=='S' or q[0]=='s':
                        if len(q)==2:
                            q.append(float(q[1]))
                            q[1]=float(q[1])
                        out=p.scale(float(q[1]),float(q[2]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                        p.plot()
                    elif q[0]=='R' or q[0]=='r':
                        q[1]=float(q[1])
                        if len(q)==2:
                            out=p.rotate(float(q[1]))
                        elif len(q)==3:
                            q[2]=float(q[2])
                            out=p.rotate(float(q[1]),float(q[2]))
                        else:
                            q[2]=float(q[2])
                            q[3]=float(q[3])
                            out=p.rotate(float(q[1]),float(q[2]),float(q[3]))
                        for k in p.old[0]:
                            print(np.round(k,2),end=" ")
                        for k in p.old[1]:
                            print(np.round(k,2),end=" ")
                        print("")
                        for k in out[0]:
                            print(np.round(k,2),end=" ")
                        for k in out[1]:
                            print(np.round(k,2),end=" ")
                        p.plot()
                    else:
                        print("incorrect query code: Please try again")
            elif fi==1:
                c=input("enter space separated x,y coordinates and radius r of circle")
                c=list(c.split())
                if len(c)==0:
                    ci=Circle()
                elif len(c)==1:
                    ci=Circle(float(c[0]))
                elif len(c)==2:
                    ci=Circle(float(c[0]),float(c[1]))
                else:
                    ci=Circle(float(c[0]),float(c[1]),float(c[2]))
                n=int(input("enter number of queries"))
                print('''
                Enter Query:
                a) R theta (rx) (ry) 
                b) S sr 
                c) T dx (dy) 
                ''')
                for j in range(n):
                    q=input()
                    q=list(q.split())
                    if q[0]=='T' or q[0]=='t':
                        if len(q)==2:
                            q[1]=float(q[1])
                            q.append(q[1])
                        out=ci.translate(float(q[1]),float(q[2]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                        ci.plot()
                    elif q[0]=='S' or q[0]=='s':
                        out=ci.scale(float(q[1]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                        ci.plot()
                    elif q[0]=='R' or q[0]=='r':
                        if len(q)==2:
                            out=ci.rotate(float(q[1]))
                        elif len(q)==3:
                            out=ci.rotate(float(q[1]),float(q[2]))
                        else:
                            out=ci.rotate(float(q[1]),float(q[2]),float(q[3]))
                        print(np.round(ci.old[0],2),np.round(ci.old[1],2),np.round(ci.ort,2))
                        print(np.round(out[0],2),np.round(out[1],2),np.round(out[2],2))
                        ci.plot()
                    else:
                        print("incorrect query code: please try again")
    