import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.legend as legend
import matplotlib.animation as animation
import numpy as np

# set up duration of animation
t0 = 0 #hrs
t_end = 2 #hrs
dt = 0.005 #delta hrs

# array for time
t = np.arange(t0,t_end+dt,dt)

# array for x distance
x = 800*t # km

# array for y distance
altitute = 2 # km constant
y = np.ones(len(t))*altitute

##### Animation #####
frame_amount=len(t)

dot = np.zeros(frame_amount)
n=20
for i in range(0,len(dot)):
    if i==n:
        dot[i]=x[i]
        n=n+20
    else:
        dot[i]=x[n-20]

def update_plot(num):

    # subplot 1
    plane_trajectory.set_data(dot[0:num], y[0:num])
    plane_1.set_data([x[num]-40,x[num]+20], [y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]], [y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]], [y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30], [y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30], [y[num]-0.15,y[num]])
    
    stopwatch0.set_text(str(round(t[num],1))+' hrs')
    distance_counter0.set_text(str(int(x[num]))+' km')


    # subplot 2
    x_distance.set_data(t[0:num],x[0:num])
    horizontal_line.set_data([[t[0],t[num]],[x[num],x[num]]])
    vertical_line.set_data([[t[num],t[num]],[x[0],x[num-1]]])


    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,stopwatch0,\
    distance_counter0,x_distance,horizontal_line,vertical_line
    
fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))
plane_trajectory, = ax0.plot([],[],'r:o',linewidth=2)
plane_1, = ax0.plot([],[],'k',linewidth=10)
plane_2, = ax0.plot([],[],'k',linewidth=5)
plane_3, = ax0.plot([],[],'k',linewidth=5)
plane_4, = ax0.plot([],[],'k',linewidth=3)
plane_5, = ax0.plot([],[],'k',linewidth=3)

# Draw houses
house_1 = ax0.plot([100,100],[0,1.0],'k',linewidth=7)
house_2 = ax0.plot([300,300],[0,1.0],'k',linewidth=7)
house_3 = ax0.plot([700,700],[0,0.7],'k',linewidth=15)
house_4 = ax0.plot([900,900],[0,0.9],'k',linewidth=10)
house_5 = ax0.plot([1300,1300],[0,1.0],'k',linewidth=20)

box_obj = dict(boxstyle="square",fc=(0.9,0.9,0.9),ec="r",lw=1)
stopwatch0=ax0.text(1400,0.65,"",size=20,color="green",bbox=box_obj)

box_obj2 = dict(boxstyle="square",fc=(0.9,0.9,0.9),ec="g",lw=1)
distance_counter0 = ax0.text(1000,0.5,"",size=20,color="r",bbox=box_obj2)

plt.xlim(x[0], x[-1])
plt.ylim(0, y[0]+1)
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]),size=15)
plt.xlabel("x-distance",fontsize=15)
plt.ylabel("y-distance",fontsize=15)
plt.title("Airplane",fontsize=20)
plt.grid(True)



# Subplot 2
ax2 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
x_distance, = ax2.plot([],[],'-b',linewidth=3,label='x=800*t')
horizontal_line, = ax2.plot([],[],'r:o',label='horizontal line')
vertical_line, = ax2.plot([],[],'g:o',label='vertical line')
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4))
plt.xlabel('time [hrs]',fontsize=15)
plt.ylabel('x-distance [km]',fontsize=15)
plt.title('x-distance vs time',fontsize=15)
plt.grid(True)
plt.legend(loc='upper left', fontsize='x-large')


plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, interval=20, blit=True)
plt.show()