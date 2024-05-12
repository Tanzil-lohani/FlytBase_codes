#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(10.0)

side_length = 10

print ' going along the setpoints'
drone.position_set(side_length, 0, 10, relative=False)
drone.position_set(side_length / 2, side_length * 0.866, 10, relative=False)
drone.position_set(0, 0, 10, relative=False)

print 'Landing'
drone.land(async=True)

# shutdown the instance
drone.disconnect()