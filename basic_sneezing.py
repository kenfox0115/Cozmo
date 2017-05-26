import cozmo

def cozmo_program_sneeze(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(-50), speed_mmps(100))
    robot.say_text("aa").wait_for_completed()
    time.sleep(1)
    robot.say_text("aa").wait_for_completed()
    time.sleep(1)
    robot.drive_straight(distance_mm(50), speed_mmps(100))
    robot.say_text("aachoo").wait_for_completed()
    anim = robot.play_anim_trigger(cozmo.anim.Triggers.DizzyReactionMedium)
    anim.wait_for_completed()


cozmo.run_program(cozmo_program_sneeze)