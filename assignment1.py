import numpy as np
L=12#length of beam in meters
w=10#intensity of load in KN/m

#Question a
#Bending moment(M) and shear force(V) at the first end,x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
m='Bending moment at x=0 is'
n='shear force at x=0 is'
print()
print('(a.1)'+m+str(M)+ 'and', n+str(V))
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
a='bending moment at x=L is'
b='shear force at x=L is'
print()
print('(a.2)'+a+str(M)+ 'and', b+str(V))


#Question b
"""
when bending moment is zero, we obtain the expression x**2-Lx+L**2/6=0
"""
#from the expression
a=1
b=-L
c=L**2/6
#using almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print()
print('(b) the points of contra-flexure are (0) and (1)')


#Question c
"""
when shear force is zero,x=L/2
"""
x=L/2
print()
print('(c) bending moment is zero at' +str(root_1b)+ 'and' +str(root_2b))


#Question d
p=0
l=0.01
t=L+l
x=np.arange(p,t,l)
M=(w*(-6*x**2+6*L*x-L**2))/12
print()
print('(d) using initialized variable, bending moment at each step in the array is' + str(M))


#Question e
V=w*(L/2-x)
print()
print('(e) shear force for each step along the span is' + str(V))


#Question f
"""
let bending moment be m_am
"""
m_am=M
"""
when bending moment is m_am, we get an expression x**2-Lx+(L**2/6)+(2*m_AM)/w=0
"""
#from the expression above,
a=1
b=-L
c=(L**2/6)+(2*m_am)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1f=(-b+np.sqrt(discriminant))/2*a
root_2f=(-b-np.sqrt(discriminant))/2*a
print()
print('(f) the points along L at which the absolute values of the bending moment array is minimum are'+ str(root_1f)+ 'and' + str(root_2f))


#Question g
"""
let relative errors be r_e
"""
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2f-root_2b)/root_2f*100)
print()
print('(g) the relative errors between estimated points of contra-flexure are (0)% and (1)%')


#Question h
"""
let the maximum bending moment be max_M and the minimum bending moment be min_M
"""
#for the max,
max_M=max(M)
"""
when the bending moment is max_M, we get the expression,x**2-Lx+(L**2/6)+(2*max_M)/w=0
"""
a=1
b=-L
c=(L**2/6)+(2*max_M)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.1) the points at which the maximum bending moment occur are'+ str(root_1)+ 'and'+ str(root_2))
#for the min,
min_M=min(M)
"""
when bending moment is min_M, we get an expression,x**2-Lx+(L**2/6)+(2*min_M)/w=0
"""
a=1
b=-L
c=(L**2/6)+(2*min_M)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.2) the points at which the mimimum bending moment occur are'+ str(root_1)+  'and'+ str(root_2))


#https://github.com/laud-antwi/Data-Structures-