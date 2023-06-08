# EDIT THIS FILE

# InvaderBot is a simple helper class which has methods to control the robot.
# It offers an interface over Webots' default motor controller.
# You can use it, modify it or you can also use Webots' own commands.
# Using the helper class is recommended because it will later help you to
# transfer your code into a physical robot, which is running on Raspberry Pi.

import math
from invader_bot import InvaderBot


def main():
    from pyry import MyBot

    bot = MyBot(-1)
    while bot.step():
        bot.update()


if __name__ == "__main__":
    main()
