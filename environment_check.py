import gymnasium as gym

env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset(seed=42)
print("Observation space:", env.observation_space)
print("Action space:", env.action_space)
input("Press Enter to close...")
action = 2
next_observation, reward, terminated, truncated, info = env.step(action)
print(next_observation, reward, terminated, truncated, info)
input("Press Enter to close...")
env.close()