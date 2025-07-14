import time
from hextech import CommandGroupParallel, CommandGroupSequential, HexTechMuscle


# Connect to the board
muscle = HexTechMuscle()

# Config speed, acceleration and current for stepper motor 0.
# Recommended not be executed in parallel because one setting command can be interrupt by another setting command.
# If these settings do not change, this sequence can be executed only one time.
muscle.stepper0.set_speed(20000).run()
muscle.stepper0.set_current(800).run()
muscle.stepper0.set_acceleration(20000).run()
from hextech import Microsteps
muscle.stepper0.set_microsteps(Microsteps.MS_4).run() 

muscle.stepper1.set_speed(10000).run(); muscle.stepper1.set_current(800).run(); muscle.stepper1.set_acceleration(7000).run()
#Move stepper motor 1 forward 1000 steps.
muscle.stepper1.move(0).run(); muscle.stepper1.move(0).run()


# Move stepper motor 0 and stepper motor 1 in parallel backward 6000 and 100 steps.
muscle.run(CommandGroupParallel(
    muscle.stepper0.move(-6000),
    muscle.stepper1.move(-150)
))

muscle.stepper1.move(-1640).run()

# Sleep for 1 sec
time.sleep(5)


# Move stepper motor 0 backward 1000 steps.
muscle.stepper0.move(6000).run()

#move stepper motor 1 forward 1000 steps.
muscle.stepper1.move (1790).run()





# Sleep for 1 sec
time.sleep(1)

#     )
# )

# Prevent board reset on Windows

while True:
    pass 

