__author__ = 'Jacob Taylor Cassady'
__email__ = 'jacobtaylorcassady@outlook.com'

from numpy import array, where, amax
from typing import List, Tuple

if __name__ == '__main__':
    k: int = 4
    initial_estimate: float = 0.
    action_value_estimates: array = array([initial_estimate]*k, dtype=float)
    action_counts: array = array([0]*k, dtype=float)
    action_reward_sequence: List[Tuple[int, int]] = \
        [(1, -1), (2, 1), (2, -2), (2, 2), (3, 0)]
    epsilon_timesteps: List[int] = []
    unknown_timesteps: List[int] = []

    # Iterate over actions taken and their reward
    for time_step, (action, reward) in enumerate(action_reward_sequence):
        action_index: int = action - 1

        # Display information for reference
        print(f'previous action_value_estimates: {action_value_estimates}')
        print(f'current Action({time_step}) = {action_index} -> Reward = {reward}')

        # Categorize action
        max_indices: array = where(action_value_estimates == amax(action_value_estimates))[0]
        print(f'actions with best reward: {max_indices}')
        if action_index in max_indices:
            unknown_timesteps.append(time_step)
        else:
            epsilon_timesteps.append(time_step)

        # Update
        action_counts[action_index] += 1
        action_value_estimates[action_index] += (1/action_counts[action_index])\
                                                *(reward-action_value_estimates[action_index]) ## Added after reading Section 2.4

        ## Old update before incremental improvement:
        ##  reward_sums[action_index] += reward
        ##  action_value_estimates[action_index] = reward_sums[action_index] / action_counts[action_index]

        print('')

    # Display result to Exercise 2.2:
    print(f'On which time steps did this definitely occur? Answer: {epsilon_timesteps}')
    print(f'On which time steps did this could this poissibly have occurred? Answer: {unknown_timesteps}')
