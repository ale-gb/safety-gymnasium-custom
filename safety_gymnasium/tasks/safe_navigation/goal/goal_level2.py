# Copyright 2022-2023 OmniSafe Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Goal level 2."""

from safety_gymnasium.tasks.safe_navigation.goal.goal_level1 import GoalLevel1


class GoalLevel2(GoalLevel1):
    """An agent must navigate to a goal while avoiding more hazards and vases."""

    def __init__(self, config) -> None:
        super().__init__(config=config)
        # pylint: disable=no-member

        self.placements_conf.extents = [-2, -2, 2, 2]

        custom_hazards = [
            (-0.00981389, 0.3574721),
            (0.80151562, 0.1543777),
            (-1.36095092, 0.80045563),
            (-0.49269771, 1.75072803),
            (-0.08804318, -0.34069263),
            (0.73325852, -1.59022468),
            (1.20580279, 0.28784344),
            (1.46929582, 1.78680479),
            (-1.66409935, -0.74774131),
            (1.40551731, 0.98498632)
        ]

        custom_vases = [
            (-0.88915483, -0.70300423),
            (1.69020848, 0.4634428),
            (0.79774781, 1.00145465),
            (1.34324939, -1.31873714),
            (1.79159578, -0.2956067),
            (1.21384861, -0.10075854),
            (-1.07852827, 1.83322893),
            (-1.42567535, 1.71313728),
            (-1.67725284, -0.19730583),
            (0.19204782, -1.25879664)
        ]

        custom_hazards_hard = [
            (-1.79200794, 0.25423273),
            (-0.68643498, -0.56119746),
            (0.38040063, 0.50633205),
            (0.25816435, -0.602958),
            (-0.57438599, 1.61291354),
            (0.86581067, 0.7997055),
            (1.16637986, -1.63184676),
            (-1.33743626, -0.70041833),
            (-0.11206134, 0.80448687),
            (1.76927453, 0.85151169)
        ]

        custom_vases_hard = [
            (-1.08451784, -0.24345159),
            (0.82240281, -0.74593675),
            (1.6240554, 0.32155564),
            (1.27146136, -0.18503837),
            (-0.03360595, 0.42809615),
            (-1.14624302, -1.52946572),
            (-0.79883686, -1.43591594),
            (-1.34165404, 1.34771264),
            (1.31089762, 1.21717958),
            (1.12034874, 1.62880949)
        ]

        self.hazards.num = 10
        self.vases.num = 10
        if self.fixed_goals_and_obstacles:
            if self.hard_config:
                self.hazards.locations = custom_hazards_hard
                self.vases.locations = custom_vases_hard
            else:
                self.hazards.locations = custom_hazards
                self.vases.locations = custom_vases
        self.vases.is_constrained = True
