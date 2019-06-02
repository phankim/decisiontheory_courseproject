#-*-coding: utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

iteration = 0
start_k = 174
# Призводительность цеха 1
def f1(x):
    return 5 + np.power((x + 40),2/3) 

# Призводительность цеха 2
def f2(x):
    return 7 + np.power((x + 30),1/2)

# Общая производительность за месяц
def w(k, x):
    return (f1(x)+f2(k-x))

# Остаток производства за месяц
def phi(k,x):
    return (0.7 *x + 0.94*(k-x))

# Вычисление условного оптимального выигрыша при заданном остатке k
def  W(k,ks,Ws):
    xs =  np.arange(k+1)
    next_k = phi(k,xs)
    vals = w(k,xs) + Ws[np.searchsorted(ks,next_k)]
    besti = np.argmax(vals)
    return (vals[besti],xs[besti])

# Вычисление условного оптимального выигрыша при заданном остатке k и заданных
# управлениях xs.
def Wx(k, xs, ks, Ws):
    next_k = phi(k, xs)
    return w(k,xs) + Ws[np.searchsorted(ks, next_k)]

#Для  3-го месяца
k_4 = np.linspace(0.7**3*174,0.94**3*174,10)
W_4 = np.zeros(len(k_4)+1)
k3_min = 0.7**2*174
k3_max = 0.94**2*174
k_3 = np.linspace(k3_min,k3_max,10)
W_3 = np.zeros(len(k_4)+1)
x_3 = W_3
for i in range(len(k_3)):
    (W_3[i],x_3[i]) = W(k_3[i],k_4,W_4)
    
x3_min = np.arange(0,k3_min,5)
x3_max = np.arange(0,k3_max,5)
W_3 = np.linspace(np.max(w(k3_min,x3_min)),np.max(w(k3_max,x3_max)),10)
plt.plot(x3_max,w(k3_max,x3_max),x3_min,w(k3_min,x3_min))
plt.xlabel('x')
plt.ylabel('W_3')
plt.grid(True)
plt.title('График функции W_3 (k_3,x_3 )')
plt.show()

#Для  2-го месяца
k2_min = 0.7**1*174
k2_max = 0.94**1*174
k_2 = np.linspace(k2_min,k2_max,10)
W_2 = np.zeros(len(k_2)+1)
x_2 = W_2
for i in range(len(k_2)):
    (W_2[i],x_2[i]) = W(k_2[i],k_3,W_3)
    
x2_min = np.arange(k2_min)
x2_max = np.arange(k2_max)
w2_max = Wx(k2_max, x2_max, k_3, W_3);
w2_min = Wx(k2_min, x2_min, k_3, W_3);
W_2 = np.linspace(np.max(w2_min),np.max(w2_max),10)
plt.plot (x2_max,w2_max,x2_min,w2_min);
plt.xlabel('x')
plt.ylabel('W_2')
plt.grid(True)
plt.title('График функции W_2 (k_2,x_2 )')
plt.show()

#Для  1-го месяца
k1_max = 174
x1_max = np.arange(k1_max)
k_1 = np.linspace(0.7**0*174,0.94**0*174,10)
W_1 = np.zeros(len(k_1)+1)
x_1 = W_1
for i in range(len(k_1)):
     (W_1[i],x_1[i]) = W(k_1[i],k_2,W_2)
w1_max = Wx(k1_max,x1_max,k_2,W_2)
W_1 = np.max(w1_max)
print("Total Win W1= ",W_1)
plt.show()
x_1
