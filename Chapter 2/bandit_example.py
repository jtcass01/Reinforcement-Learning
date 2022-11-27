from numpy import array, where, amax, nan_to_num
from typing import List, Tuple

if __name__ == "__main__":
    k: int = 4
    initial_estimate: float = 0.
    action_value_estimates: array = nan_to_num(array([initial_estimate]*k, dtype=float))
    action_counts: array = array([0]*k, dtype=float)
    reward_sums: array = array([0]*k, dtype=float)
    action_reward_sequence: List[Tuple[int, int]] = \
        [(1, -1), (2, 1), (2, -2), (2, 2), (3, 0)]
    epsilon_timesteps: List[int] = []
    unknown_timesteps: List[int] = []

    # Iterate over actions taken and their reward
    for time_step, (action, reward) in enumerate(action_reward_sequence):
        action_index: int = action - 1

        # Display information for reference
        print(f"time_step: {time_step}")
        print(f"previous action_value_estimates: {action_value_estimates}")
        print(f"current Action({time_step}) = {action_index} -> Reward = {reward}")

        # Categorize action
        print(f"{list(where(action_value_estimates == amax(action_value_estimates)))}")
        if action_index in where(action_value_estimates == amax(action_value_estimates))[0]:
            unknown_timesteps.append(time_step)
        else:
            epsilon_timesteps.append(time_step)

        # Update
        reward_sums[action_index] += reward
        action_counts[action_index] += 1
        action_value_estimates[action_index] = reward_sums[action_index] / action_counts[action_index]

        print("")

    # Display result to Exercise 2.2:
    print(f"On which time steps did this definitely occur? Answer: {epsilon_timesteps}")
    print(f"On which time steps did this could this poissibly have occurred? Answer: {unknown_timesteps}")
