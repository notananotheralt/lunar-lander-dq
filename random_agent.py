import gymnasium as gym

env = gym.make("LunarLander-v3", render_mode="human")
#run 5 times
episode_returns = []
for i in range(20):
    #reset using the current seed
    #seed the action space with the same seed
    observation, info = env.reset(seed=i)
    env.action_space.seed(i)
    total_reward = 0
    step_count = 0
    terminated, truncated = False, False
    while not (terminated or truncated):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        step_count += 1
    print(f"Total Reward: {total_reward}, Step Count: {step_count}")
    episode_returns.append(total_reward)
    print("Final step reward:", reward)
mean_return = sum(episode_returns) / len(episode_returns)
print("Mean return:", mean_return)
print("Episode returns:", episode_returns)
env.close()