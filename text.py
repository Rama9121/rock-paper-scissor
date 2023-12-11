from tkinter import *
from PIL import Image,ImageTk
from random import randint
root=Tk()
root.title('rock scissor paper')
root.configuration(background='#9b59b6')
#picture
rock_img=ImageTk.photoImage(Image.open('rock-user.png'))
paper_img=ImageTk.photoImage(Image.open('paper-user.png'))
scissor_img=ImageTk.photoImage(Image.open('scissor-user.png'))
rock_img_comp=ImageTk.photoImage(Image.open('rock.png'))
paper_img_comp=ImageTk.photoImage(Image.open('paper.png'))
scissor_img_comp=ImageTk.photoImage(Image.open('scissor.png'))
#insert picture
user_label=Label(root,Image=scissor_img,bg='#9b59b6')
comp_label=Label(root,Image=scissor_img,bf='#9b59b6')
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)
#score
playerscore=Label(root,text=0,font=100,bg='',fg='')
computerscore=Label(root,text=0,font=100,bg='',fg='')
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)
#buttons
rock=Button(root,width=20,height=2,text='rock',bg='',fg='white').grid(row=2,column=1)
paper=Button(root,width=20,height=2,text='paper',bg='',fg='white').grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text='scissor',bg='',fg='white').grid(row=2,column=3)
#indicator
user_indicator=Label(root,font=50,text='user',bg='',fg='white')
comp_indicator=Label(root,font=50,text='computer',bg='',fg='white')
user_indicator.grid(row=0,column=3)
comp_label.grid(row=0,column=1)
#messages
msg=Label(root,font=50,bg='',fg='white')
msg.grid(row=3,column=3)
#update choice
choices=['rock','paper','scissor']
def updatechoice(x):
    if x=='rock':
        user_label.configure(Image=rock_img)
    elif x=='paper':
        user_label.configure(Image=paper_img)
    else:
        user_label.configure(Image=scissor_img)
    checkwin(x,compchoice)
#for computer
compchoice=choices[randint(0,2)]
if compchoice=='rock':
    comp_label.configure(Image=rock_img_comp)
elif compchoice=='paper':
    comp_label.configure(Image=paper_img_comp)
else:
    comp_label.configure(Image=scissor_img_comp)

#button
COMMAND=lambda:updatechoice('rock')
#update message
def updatemessage(x):
    msg['text']=x
#update user score
def updateuserscore():
    score=int(playerscore['text'])
    score+=1
    playerscore['text']=str(score)
#update computer score
def updatecomputerscore():
    score=int(computerscore['text'])
    score+=1
    computerscore['text']=str(score)
#checkwinner
def checkwin(player,computer):
    if player==computer:
        updatemessage('it is tie')
    elif player=='rock':
        if computer=='paper':
            updatemessage('you loose')
            updatecomputerscore()
        else:
            updatemessage('you win')
            updateuserscore()
    elif player=='paper':
        if computer == 'scissor':
            updatemessage('you loose')
            updatecomputerscore()
        else:
            updatemessage('you win')
            updatecomputerscore()
    elif player =='scissor':
        if computer =='rock':
            updatemessage('you loose')
            updatecomputerscore()
        else:
            updatemessage('you win')
            updateuserscore()
    else:
        pass
root.mainloop()
