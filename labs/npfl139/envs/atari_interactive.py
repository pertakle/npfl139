# This file is part of NPFL139 <http://github.com/ufal/npfl139/>.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
if __name__ == "__main__":
    import argparse

    import ale_py
    import gymnasium as gym
    import gymnasium.utils.play
    import pygame

    parser = argparse.ArgumentParser()
    parser.add_argument("atari_game", type=str, help="The name of the Atari game to play.")
    parser.add_argument("--zoom", default=4, type=int, help="The default zoom level.")
    args = parser.parse_args()

    class ReturnReporter():
        def __init__(self):
            self.rewards = 0

        def __call__(self, obs_t, obs_tp1, action, rew, terminated, truncated, info):
            self.rewards += rew
            if terminated or truncated:
                print("Episode reward:", self.rewards)
                self.rewards = 0

    gym.utils.play.play(
        gym.make(f"ALE/{args.atari_game}-v5", render_mode="rgb_array", full_action_space=True),
        callback=ReturnReporter(), fps=15, zoom=args.zoom)
