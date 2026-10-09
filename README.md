![Robojam Logo](robojam_cover.jpg)

# Robojam Robot Code 
This repo contains the master copy of the robot code and all the necessary instruction packs and other files to run the day.

Copy these files to `/home/pi/robot`:

  `robot.py` 
  `robotlib.py`
  `init.sh`

then run

`chmod 555 /home/pi/robot/init.sh`

then create a tarball for refreshing back to this point in future, make read only.

`tar -cvf /home/pi/robot robot.tar; chmod 444 robot.tar`

This repo also contains 
* the instruction pack for the teams (ask the school to print 1-2 copies per team)
* the facilitator notes
* the scoreboard xls
