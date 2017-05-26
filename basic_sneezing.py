import cozmo
from cozmo.util import distance_mm, speed_mmps
import time

def cozmo_program_sneeze(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(-50), speed_mmps(100)).wait_for_completed()
    robot.move_head(5)
    robot.say_text("ah").wait_for_completed()
    robot.drive_straight(distance_mm(-50), speed_mmps(100)).wait_for_completed()
    robot.move_head(5)
    robot.say_text("ah").wait_for_completed()
    robot.drive_straight(distance_mm(50), speed_mmps(100)).wait_for_completed()
    robot.move_head(-10)
    robot.say_text("aachoo").wait_for_completed()
    anim = robot.play_anim_trigger(cozmo.anim.Triggers.DizzyReactionMedium)
    anim.wait_for_completed()


cozmo.run_program(cozmo_program_sneeze)
