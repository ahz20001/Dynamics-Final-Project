#!/usr/bin/env python
# coding: utf-8

# # This is a python model that allows you to model the dynamics concept of deceleration: (Final velocity - intial velocity)/time  

# # ![image.png](attachment:image.png)
# 

# # Here we define the intial conditions of and properties of the bowling ball
#     Playing around with the property values allow you to see how they each variable effects deceleration, if at all.

# In[2]:


# Define the physical properties of the bowling ball
air_resistance = 0.1  # constant for air resistance
friction_coefficient = 0.2  # coefficient of friction
rolling_friction_coefficient = 0.05  # coefficient of rolling friction
gravity = 9.81  # acceleration due to gravity
mass = 7  # mass of the bowling ball

# Set the initial conditions
initial_velocity = 10  # initial velocity in m/s
initial_time = 0  # initial time in seconds
time_interval = 0.01  # time interval in seconds


# # Calculation
# Here is where the setup and computation for the equation is completed

# In[3]:


# Create empty lists to store the data
time_list = [initial_time]
velocity_list = [initial_velocity]
acceleration_list = [-air_resistance*initial_velocity**2/mass - friction_coefficient*rolling_friction_coefficient*gravity]

# Loop through the calculations until the ball comes to rest
while velocity_list[-1] > 0:
    # Calculate the time, velocity and acceleration at each time interval
    time_list.append(time_list[-1] + time_interval)
    velocity_list.append(velocity_list[-1] + acceleration_list[-1]*time_interval)
    acceleration_list.append(-air_resistance*velocity_list[-1]**2/mass - friction_coefficient*rolling_friction_coefficient*gravity)


# # Plotting
# here we import pythons math plot function and we plot deceleration over time 

# In[4]:


# Import the required library for plotting
import matplotlib.pyplot as plt

# Plot the data on a graph
plt.plot(time_list, acceleration_list)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Deceleration of a Bowling Ball due to Air Resistance and Friction')
plt.show()

