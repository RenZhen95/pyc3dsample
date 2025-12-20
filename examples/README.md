# Discussion regarding heel-strike detection
I have currently implemented three methods to detect heel-strikes, but firstly the **important assumption here is a normal gait**. All three methods detect a heel strike based on the kinematics of the heel marker on the respective foot, where **two** conditions must be fulfilled.

The first condition is:
> The respective heel marker must be in front (i.e. in walking direction) of the sternum marker.

The second condition is what differs among the different methods. To illustrate, say we would like to detect all right heel strikes, where it is given that the "forward"-walking direction is defined as the global $y$-axis. The second condition for the three different methods are defined as the following:

### Method: Zero-crossing of $z$-velocity of heel marker ('-' $\rightarrow$ '+')
```python
get_HeelStrike('R', _forwardaxis='Y', _method="zHeelVelocity")
```
> Returns heel strikes based on $z$-velocity of heel marker being zero, implemented by detecting sign switch from negative to positive.

> ### Method: Zero-crossing of $y$-acceleration of heel marker ('-' $\rightarrow$ '+')
```python
get_HeelStrike('R', _forwardaxis='Y', _method="yHeelAcceleration")
```
> Returns heel strikes based on $y$-acceleration of heel marker being zero, implemented by detecting sign switch from negative to positive.

> ### Method: Zero-crossing of $y$-snap (4-th derivative in time) of heel marker ('+' $\rightarrow$ '-')
```python
get_HeelStrike('R', _forwardaxis='Y', _method="yHeelSnap")
```
> Returns heel strikes based on $y$-snap of heel marker being zero, implemented by detecting sign switch from positive to negative.

The implemented methods were validated using the C3D file in `data/testsample.c3d`.

![Heel Detection Method Comparisons and Validation](examples/HeelStrikeDetectionMethods.png)
