from game import Game
import random

def main():
    g = Game()
    epsilon = 0.9
    cool = 0.9
    episodes = 1000
    history = []
    short_history = []
    board_score = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    for _ in range(episodes):
        done = False
        while not done:
            available_steps = g.available_spaces()
            if epsilon > random.random():
                action = random.choice(available_steps)
                epsilon = epsilon * cool
            else:
                max = 0
                action = 0
                for step in available_steps:
                    if board_score[step] > max: 
                        max = board_score[step]
                        action = step

            done, reward = g.bot_step(action)


