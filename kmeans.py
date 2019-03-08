#coding:utf-8
import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

colorlist = ['r','g','b','y']
#change here to test ramdom init.
seedcount = 0
def gen_normal(m,sigma,num):
    global seedcount
    np.random.seed(seedcount)
    seedcount+=1
    s = np.random.normal(m, sigma, num )
    #print(s)
    #show_hori(s)
    return s

def show_hori(s):
    plt.hist(s, 30, normed=True)
    plt.show()

def D(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return(round((((x1-x2)**2+(y1-y2)**2)),2))

def kmeans(data,k):
    plt.clf() 
    print('#####K-MEANS BEGIN#####')
    # initialize groups
    num = len(data)
    init = np.random.randint(0,num,k).tolist()
    # init G(roups)
    G = [[]for row in range(k)]
    C = [[]for row in range(k)]
    print(G)
    for i in range(k):
        G[i].append(data[init[i]])
        C[i]=data[init[i]]
    #print(G)
    print(C)
    unstable_flag = 1
    roundcount = 0
    while (unstable_flag):
        roundcount += 1 
        plt.clf() 
        unstable_flag = 0
        # step 2
        for node in data:
            # find nearest centroid
            shortest = 0xFFFFFFF
            nearest_centroid = 0
            for centriod in C:
                dist = D(centriod,node)
                #print("[*]node{}{} nearer to {} D={} ".format(data.index(node),node,centriod,dist))
                
                if (dist<shortest):
                    #print("dist{}<sh{}".format(dist,shortest))
                    shortest = dist
                    nearest_centroid = centriod
            nearest_index = C.index(nearest_centroid)
            # moved
            if node not in G[nearest_index]:
                unstable_flag = 1
                for i in range(k):
                    if node in G[i]:
                        G[i].remove(node)
                        break
                G[nearest_index].append(node)
                print("[+]node{}{} nearer to {} D={} {}-->{}".format(data.index(node),node,centriod,dist,i,nearest_index))
        # step 3
        for i in range(k):
            sumx = 0
            sumy = 0
            showx = []
            showy = []
            for j in range(len(G[i])):
                sumx += G[i][j][0]
                sumy += G[i][j][1]
                showx.append(G[i][j][0])
                showy.append(G[i][j][1])
                
                xyshow(showx,showy,colorlist[i])
                plt.plot([C[i][0]],[C[i][1]],'bx')
            C[i][0] = round(sumx / len(G[i]),2)
            C[i][1] = round(sumy / len(G[i]),2)
            #print(C[i])
        plt.show()
        plt.pause(0.3)
        plt.savefig("round{}.png".format(roundcount))
        #print(G)
        print(C)
        #show
        






def xyshow(x,y,color):
    plt.figure(1,figsize=(10,6))
    plt.plot(x,y,color + 'o')

if __name__ == '__main__':
    
    x1 = gen_normal(120,10,100).tolist()
    y1 = gen_normal(50,15,100).tolist()
    x2 = gen_normal(67,10,80).tolist()
    y2 = gen_normal(120,20,80).tolist()
    x3 = gen_normal(60,15,90).tolist()
    y3 = gen_normal(15,10,90).tolist()
    x4 = gen_normal(30,13,180).tolist()
    y4 = gen_normal(60,24,180).tolist()
    f = open("data.txt","w")
    
    x1.extend(x2)
    y1.extend(y2)
    x1.extend(x3)
    x1.extend(x4)
    y1.extend(y3)
    y1.extend(y4)
    xyshow(x1,y1,'r')
    xyshow(x2,y2,'g')
    xyshow(x3,y3,'b')
    xyshow(x4,y4,'y')
    #plt.plot(x1,y1,'o','r')
    #plt.plot(x2,y2,'o','g')
    #plt.plot(x3,y3,'o','b')
    #plt.plot(x4,y4,'o','y')
    plt.ion()
    plt.show()
    plt.pause(0.3)
    plt.savefig("init.png")
    #print(x1)
    i=0
    data = []
    for _ in x1:
        #print("{:.4f},{:.4f} k={:.3f} i={}".format(x1[i],y1[i],(y1[i]/x1[i]),i))
        f.write("{:.4f},{:.4f}\n".format(x1[i],y1[i]))
        data.append([round(x1[i],2),round(y1[i],2)])
        i+=1
    print(data)
    plt.plot(x1,y1,'co',color = 'g')
    plt.show()
    plt.pause(0.3)
    plt.savefig("init_done.png")
    kmeans(data,4)
    plt.pause(1)

