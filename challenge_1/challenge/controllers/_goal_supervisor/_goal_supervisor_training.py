from controller import Supervisor
import math

supervisor = Supervisor()

timestep = int(supervisor.getBasicTimeStep())

blue_score = 0
red_score = 0

blue_goal = supervisor.getFromDef("_blue_goal")
red_goal = supervisor.getFromDef("_red_goal")


def updateScore():
    supervisor.setLabel(0, "RED " + str(red_score), 0, 0, 0.1, 0xFF0000, 0, "Impact")
    supervisor.setLabel(
        1, "BLUE " + str(blue_score), 0, 0.05, 0.1, 0x0000FF, 0, "Impact"
    )


def check_goal(ball, goal):
    ball_pos = ball.getPosition()
    goal_pos = goal.getPosition()
    goal_angle = goal.getField("rotation").getSFRotation()[3]  # [0, -1, 0, angle]
    goal_width = 1  # meter
    goal_precision = 0.05  # meter

    # pole vector
    pole_x = math.cos(goal_angle) * goal_width / 2
    pole_z = math.sin(goal_angle) * goal_width / 2

    # distance between a point (a ball) to a line segment (a goal)
    dot_product = (ball_pos[0] - goal_pos[0]) * pole_x + (
        ball_pos[2] - goal_pos[2]
    ) * pole_z
    scale = max(-1, min(1, dot_product / (pole_z**2 + pole_x**2)))
    proj_x = goal_pos[0] + scale * pole_x
    proj_z = goal_pos[2] + scale * pole_z
    distance2 = (proj_x - ball_pos[0]) ** 2 + (proj_z - ball_pos[2]) ** 2

    is_goal = distance2 < goal_precision**2
    return is_goal


def reset_ball(ball):
    ball.getField("translation").setSFVec3f([0, 0, 0])


def loop_balls(group_name, blue_scoring_points, red_scoring_points):
    global red_score, blue_score
    root = supervisor.getFromDef(group_name)
    root = root.getField("children")
    ballCount = root.getCount()
    for i in range(ballCount - 1, -1, -1):
        ball = root.getMFNode(i)
        # Check if ball is in goal
        if check_goal(ball, blue_goal):
            blue_score += blue_scoring_points
            updateScore()
            reset_ball(ball)
        elif check_goal(ball, red_goal):
            red_score += red_scoring_points
            updateScore()
            reset_ball(ball)
        # Reset ball if it goes out of bounds
        elif max(map(abs, ball.getPosition())) > 2.1:
            reset_ball(ball)


updateScore()
while supervisor.step(timestep) != -1:
    loop_balls("_balls", 1, 1)
