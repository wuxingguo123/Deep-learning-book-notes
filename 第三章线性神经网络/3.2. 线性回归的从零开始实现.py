import numpy
import math
import random
import torch
n=10000
a=torch.ones([3,4])
b=torch.ones([n])

#normal为正态分布函数
def Normal(x,sigma,u):
    p=1/numpy.sqrt(2*math.pi*sigma**2)
    return p*math.exp(-0.5/sigma**2*(x-u)**2)

#Creat_data为创建相关数据集
def Creat_data(num_input,w,b):
    X = torch.normal(0 , 1 ,(num_input , len(w)))
    Y = torch.matmul(X , w) + b
    Y+=torch.normal(0 , 0.01 , Y.shape)
    return  X,Y.reshape(-1 , 1)

#data_iter为触发器用于批次返回小样本集
def Data_iter(bath_size ,X ,y ):
    num_input=len(X)
    indices=list(range(num_input))
    random.shuffle(indices)
    for i in range(0 ,num_input ,bath_size ):
        bath_indices=torch.tensor(indices[i :min(i+bath_size,num_input) ])
        yield X[bath_indices] ,y[bath_indices]
        
#Model_linreg为线性回归的模型
def Model_linreg(X ,w ,b ):
    y=torch.matmul(X,w)+b
    return y

#Loss_linreg为简单线性回归的损失函数
def Loss_linreg(y_true,y_forecast):
    Y=(y_true-y_forecast)**2/2
    return Y

#Improve_sgd为简单线性回归的优化算法
def Improve_sgd(params,lr,bath_size):
    with torch.no_grad():
        for param in params:
            param-=lr*param.grad/bath_size
            param.grad.zero_()
        
#Train_linreg用于喂数据
def Train_linreg(true_input,true_output,train_w,train_b):
    lr =0.3
    num_train=3
    for train in range(num_train):
        for X ,y in Data_iter(bath_size , true_input ,true_output ):
            l=Loss_linreg(Model_linreg(X ,train_w ,train_b ), y)
            l.sum().backward()
            Improve_sgd([train_w ,train_b], lr, bath_size)
        with torch.no_grad():
            train_1=Loss_linreg(true_output , Model_linreg(true_input, train_w, train_b))
            # 打印最终训练结果
            print(f'epoch {train + 1}, loss {float(train_1.mean()):f}')
            print(f'训练之前的w：{true_w.numpy()}  训练之后的w：{train_w.flatten().detach().numpy()}')
            print(f'训练之前的b：{true_b}  训练之后的b：{train_b.numpy()}')
            
                
true_w = torch.tensor([2 , -3.4])
true_b = 3
true_input , true_output= Creat_data(n, true_w, true_b)

bath_size=10
#for x ,y in Data_iter(bath_size ,true_input ,true_output):
    #print(x[ :5] ,'\n' ,y[ :5])
    #break
train_w=torch.normal(0,0.01,size=(2,1),requires_grad=True)
train_b=torch.zeros(1,requires_grad=True)
Train_linreg(true_input,true_output,train_w,train_b)
