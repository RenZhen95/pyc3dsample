# PyC3DSample
Interface to easily deal with a C3D file, including some helpful methods for dealing with gait analysis (e.g. detecting heel strike)

## Installation
```
pip install pyc3dsample
```

## Basic usage
Initialize PyC3DSample object and get general information about C3D file
```python
from pyc3dsample import PyC3D

Test = PyC3DSample(c3dfile)
print(Test)
```

To get the progression of the left hip angles with respect to the X-axis
```python
print(Test.get_TimeProgress("LHipAngles_X"))
```

To get events (e.g. left or right foot strike)
```python
# Get events -> List of (<label>, <time [s]>)
print(Test.Events)
```

Get progression of the left knee angles with respect to the X-axis from 100 ms before an event, until the event itself
```python
EventEvent = round(
    [e for e in Test.Events if e[0] == 'Event'][0][1], 2
)
print(
    Test.get_TimeProgressRange("LKneeAngles_X", EventEvent-0.1, EventEvent)
)
```

Get and plot position and velocity of the RHEE marker along the global z-axis
```python
RHEE_Z  = Test.get_TimeProgress("RHEE_Z")
RHEE_Zd = Test.get_TimeProgress1D("RHEE_Z")

# Plot
fig, axs = plt.subplots(2, 1, sharex=True)

# Position
axs[0].plot(RHEE_Z[:,0], RHEE_Z[:,1])
axs[0].set_ylabel("Position [mm]")
axs[0].set_title("RHEE Marker Position (z)", loc="left", fontsize="large")
# Velocity
axs[1].plot(RHEE_Zd[:,0], RHEE_Zd[:,1])
axs[1].set_ylabel("Velocity [mm/s]")
axs[1].set_xlabel("Time [s]")
axs[1].set_title("RHEE Marker Velocity (z)", loc="left", fontsize="large")
axs[0].grid()
axs[1].grid()
fig.tight_layout()
plt.show()
```

To identify heel strikes
```python
rHeelStrike_Time = Test.get_HeelStrike('R')
print(f"Right heel strike at : {rHeelStrike_Time}")

lHeelStrike_Time = Test.get_HeelStrike('L')
print(f"Left heel strike at  : {lHeelStrike_Time}")
```