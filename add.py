import matplotlib.pyplot as plt
x=complex(input('Enter a complex number:'))
angle=int(input('Enter an angle of rotation (90/180/270);'))
if angle==90:
    s1={x*1j}
elif angle==180:
    s1={x*-1}
elif angle==270:
    s1={x*1j*-1}
X=[x.real for x in s1]
Y=[x.imag for x in s1]
plt.plot(X,Y,'ro')
plt.show()
