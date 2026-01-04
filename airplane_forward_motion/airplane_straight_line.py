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

def update_plot(num):
    return
    
fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 1
ax0 = fig.add_subplot(gs[0:], facecolor=(0.9,0.9,0.9))

plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, interval=20, blit=True)
plt.show()