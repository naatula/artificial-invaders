# Artificial Invaders

[Artificial Invaders](https://robotuprising.fi/hackathon/artificial-invaders/) is a story-driven, strategic robotics game designed for hacker teams experienced in Artificial Intelligence and Robotics.

Artificial Invaders consists of two phases: ``pre-challenges`` and ``a physical robot battle tournament``. The pre-challenges are part of our qualification process of the tournament. The best 10 teams will be selected to fight for supremacy of the Robot Uprising universe. 

Schedule:

- Pre-challenges (1st phase) 19.06.-1.9.19
- Tournament (2nd phase) 11.-13.10.19

## Pre-Challenges

Pre-challenges test the skills of your team and also help you learn some of the technologies involved. The pre-challenge phase will culminate into a full battle against other competitors on the simulation platform.

The simulation platform is [``Webots``](https://cyberbotics.com/), which is an open source robotics simulation software. It is available for ``Windows``, ``Linux`` and ``macOS``.

In Webots, you can easily model custom robots and control them by using ``Python``. The code that is written for the simulation can be reused easily with the real physical robot running on for instance Arduino or Rasberry Pi.

For the pre-challenges, we will provide you a premade robot model and the game arena. So, you can focus on the crucial robotic skills, e.g. coding and AI. In other words, there is no need to spend time learning Webots thoroughly (unless you want to!).

## How to Start

Fork this repo to start working on the challenges! 

The challenge grading is done fully automatically, just push your code to the repo and the CI will do the rest.

## Setup

1. Fork
2. Go to "settings" -> "CI / CD" -> "Runners" and enable shared runners
3. Update your team info into the file `team_info.txt`

## Submitting Your Solution

When you feel you're ready to submit,
  1. Copy all files you want to submit into the folder `challenge_n/submission`
  2. Commit & Push: the CI will do the rest

Submissions will be evaluated, and scores will be published [here](http://robotuprising.fi/ai-scores)
    (this might take a couple days for some challenges)

## New Challenges
New Challenges are released [every X days / schedule here]. You'll be notified to the email address you used to [register/apply] to Artificial Invaders.
To automatically receive the new challenge files, you can setup [**Repository Mirroring**](https://about.gitlab.com/2016/12/01/how-to-keep-your-fork-up-to-date-with-its-origin/)
on your **Fork of this repository**.
Tip: set up development branches for each challenge, so you don't run into merge conflicts in the master branch.
