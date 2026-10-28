import gymnasium as gym

env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset(seed=42)
observation, reward, terminated, truncated, info = env.step(0)
print(f"Observation: {observation}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")
velocity1 = observation[3]
observation, info = env.reset(seed=42)
observation, reward, terminated, truncated, info = env.step(2)
print(f"Observation: {observation}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")
velocity2 = observation[3]

print(velocity2, velocity1)
print(velocity2-velocity1)
env.close()