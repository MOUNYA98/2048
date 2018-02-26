import random
a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
a[random.randint(-1,3)][random.randint(-1,3)]=2;
score=0;
def g2048(c,a,score):
    if c=="1":
        i=0;
        for j in range(0,4):
            if a[i][j]==0 and (a[i+1][j]!=0 or a[i+2][j]!=0 or a[i+3][j]!=0):
                while a[i][j]==0:
                    a[i][j]=a[i+1][j];
                    a[i+1][j]=a[i+2][j];
                    a[i+2][j]=a[i+3][j];
                    a[i+3][j]=0;
            if a[i+1][j]==0 and (a[i+2][j]!=0 or a[i+3][j]!=0):
                while a[i+1][j]==0:
                    a[i+1][j]=a[i+2][j];
                    a[i+2][j]=a[i+3][j];
                    a[i+3][j]=0;
            if a[i+2][j]==0 and a[i+3][j]!=0:
                while a[i+2][j]==0:
                    a[i+2][j]=a[i+3][j];
                    a[i+3][j]=0;


        i=0;
        for j in range(0,4):
            if a[i][j]==a[i+1][j]:
                a[i][j]=a[i][j]+a[i+1][j];
                a[i+1][j]=a[i+2][j];
                a[i+2][j]=a[i+3][j];
                a[i+3][j]=0;
                score=score+a[i][j];
            if a[i+1][j]==a[i+2][j]:
                a[i+1][j]=a[i+2][j]+a[i+1][j];
                a[i+2][j]=a[i+3][j];
                a[i+3][j]=0;
                score=score+a[i+1][j];
            if a[i+2][j]==a[i+3][j]:
                a[i+2][j]=a[i+2][j]+a[i+3][j];
                a[i+3][j]=0;
                score=score+a[i+2][j];
    elif c=="2":
        i=0;
        for j in range(0,4):
            if a[i+3][j]==0 and (a[i+2][j]!=0 or a[i+1][j]!=0 or a[i][j]!=0):
                while a[i+3][j]==0:
                    a[i+3][j]=a[i+2][j];
                    a[i+2][j]=a[i+1][j];
                    a[i+1][j]=a[i][j];
                    a[i][j]=0;
            if a[i+2][j]==0 and (a[i+1][j]!=0 or a[i][j]!=0):
                while a[i+2][j]==0:
                    a[i+2][j]=a[i+1][j];
                    a[i+1][j]=a[i][j];
                    a[i][j]=0;
            if a[i+1][j]==0 and a[i][j]!=0:
                while a[i+1][j]==0:
                    a[i+1][j]=a[i][j];
                    a[i][j]=0;


        i=0;
        for j in range(0,4):
            if a[i+3][j]==a[i+2][j]:
                a[i+3][j]=a[i+3][j]+a[i+2][j];
                a[i+2][j]=a[i+1][j];
                a[i+1][j]=a[i][j];
                a[i][j]=0;
                score=score+a[i+3][j];
            if a[i+2][j]==a[i+1][j]:
                a[i+2][j]=a[i+2][j]+a[i+1][j];
                a[i+1][j]=a[i][j];
                a[i][j]=0;
                score=score+a[i+2][j];
            if a[i+1][j]==a[i][j]:
                a[i+1][j]=a[i+1][j]+a[i][j];
                a[i][j]=0;
                score=score+a[i+2][j];
    elif c=="3":
        j=0;
        for i in range(0,4):
            if a[i][j+3]==0 and (a[i][j+2]!=0 or a[i][j+1]!=0 or a[i][j]!=0):
                while a[i][j+3]==0:
                    a[i][j+3]=a[i][j+2];
                    a[i][j+2]=a[i][j+1];
                    a[i][j+1]=a[i][j];
                    a[i][j]=0;
            if a[i][j+2]==0 and (a[i][j+1]!=0 or a[i][j]!=0):
                while a[i][j+2]==0:
                    a[i][j+2]=a[i][j+1];
                    a[i][j+1]=a[i][j];
                    a[i][j]=0;
            if a[i][j+1]==0 and a[i][j]!=0:
                while a[i][j+1]==0:
                    a[i][j+1]=a[i][j];
                    a[i][j]=0;
        j=0;
        for i in range(0,4):
            if a[i][j+3]==a[i][j+2]:
                a[i][j+3]=a[i][j+3]+a[i][j+2];
                a[i][j+2]=a[i][j+1];
                a[i][j+1]=a[i][j];
                a[i][j]=0;
                score=score+a[i][j+3];
            if a[i][j+2]==a[i][j+1]:
                a[i][j+2]=a[i][j+2]+a[i][j+1];
                a[i][j+1]=a[i][j];
                a[i][j]=0;
                score=score+a[i][j+2];
            if a[i][j+1]==a[i][j]:
                a[i][j+1]=a[i][j+1]+a[i][j];
                a[i][j]=0;
                score=score+a[i][j+1];

    elif c=="4":
        j=0;
        for i in range(0,4):
            if a[i][j]==0 and (a[i][j+2]!=0 or a[i][j+1]!=0 or a[i][j+3]!=0):
                while a[i][j]==0:
                    a[i][j]=a[i][j+1];
                    a[i][j+1]=a[i][j+2];
                    a[i][j+2]=a[i][j+3];
                    a[i][j+3]=0;
            if a[i][j+1]==0 and (a[i][j+2]!=0 or a[i][j+3]!=0):
                while a[i][j+1]==0:
                    a[i][j+1]=a[i][j+2];
                    a[i][j+2]=a[i][j+3];
                    a[i][j+3]=0;
            if a[i][j+2]==0 and a[i][j+3]!=0:
                while a[i][j+2]==0:
                    a[i][j+2]=a[i][j+3];
                    a[i][j+3]=0;
        j=0;
        for i in range(0,4):
            if a[i][j]==a[i][j+1]:
                a[i][j]=a[i][j]+a[i][j+1];
                a[i][j+1]=a[i][j+2];
                a[i][j+2]=a[i][j+3];
                a[i][j+3]=0;
                score=score+a[i][j];
            if a[i][j+1]==a[i][j+2]:
                a[i][j+1]=a[i][j+2]+a[i][j+1];
                a[i][j+2]=a[i][j+3];
                a[i][j+3]=0;
                score=score+a[i][j+1];
            if a[i][j+2]==a[i][j+3]:
                a[i][j+2]=a[i][j+2]+a[i][j+3];
                a[i][j+3]=0;
                score=score+a[i][j+2];
    


       

while True:
    print (a[0][0],"\t",a[0][1],"\t",a[0][2],"\t",a[0][3],"\n");
    print (a[1][0],"\t",a[1][1],"\t",a[1][2],"\t",a[1][3],"\n");
    print (a[2][0],"\t",a[2][1],"\t",a[2][2],"\t",a[2][3],"\n");
    print (a[3][0],"\t",a[3][1],"\t",a[3][2],"\t",a[3][3],"\n");
    user_input = input("1.upward direction\n2.downwards\n3.Right\n4.left");
    g2048(user_input,a,score);
    listfori = [];
    listforj = [];
    count = 0;
    for i in range(0,4):
        for j in range(0,4):
            if a[i][j]==0:
                count+=1;
                listfori.append(i);
                listforj.append(j);
    if count > 0:
        if count > 1:
            randomindex = listfori.index(random.choice(listfori));
            a[listfori[randomindex]][listforj[randomindex]]=2;
        else:
            a[listfori[0]][listforj[0]]=2;
    else:
        break
print ("Game over");


        


            
                    
        
