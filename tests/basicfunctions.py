import pytest
from pyc3dsample import PyC3DSample

def test_initializeobject():
    Test = PyC3DSample("testsample.c3d")

    # Get general information about C3D file
    print(Test)

# # Get Left Hip Angles, with respect to time
# print(Test.get_TimeProgress("LHipAngles_Z"))

# # Get events -> List of (<label>, <time [s]>)
# print(Test.Events)
# # Note: This will return the "original" time that the event is placed in,
# #       not the time, relative to clipping in postprocessing

# # Example 1::
# # Get time-progression of LKneeAngles_X from 100 ms before the event
# # 'Event', until the event itself
# EventEvent = round(
#     [e for e in Test.Events if e[0] == 'Event'][0][1], 2
# )
# print(
#     Test.get_TimeProgressRange("LKneeAngles_X", EventEvent-0.1, EventEvent)
# )

# # Example 2::
# # Get first-derivative of a time-progress
# print(Test.get_TimeProgress1D("LKneeAngles_X"))

# # Example 3::
# # Get and plot position and velocity of the RHEE marker in z-axis
# RHEE_Z  = Test.get_TimeProgress("RHEE_Z")
# RHEE_Zd = Test.get_TimeProgress1D("RHEE_Z")

# fig, axs = plt.subplots(2, 1, sharex=True)
# # Position
# axs[0].plot(RHEE_Z[:,0], RHEE_Z[:,1])
# axs[0].set_ylabel("Position [mm]")
# axs[0].set_title("RHEE Marker Position (z)", loc="left", fontsize="large")
# # Velocity
# axs[1].plot(RHEE_Zd[:,0], RHEE_Zd[:,1])
# axs[1].set_ylabel("Velocity [mm/s]")
# axs[1].set_xlabel("Time [s]")
# axs[1].set_title("RHEE Marker Velocity (z)", loc="left", fontsize="large")
# axs[0].grid()
# axs[1].grid()
# fig.tight_layout()
# plt.show()

# # Example 4::
# # Identify heel strikes
# rHeelStrike_Time = Test.get_HeelStrike('R')
# print(f"Right heel strike at : {rHeelStrike_Time}")

# lHeelStrike_Time = Test.get_HeelStrike('L')
# print(f"Left heel strike at  : {lHeelStrike_Time}")
