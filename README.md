# LunarLander DQN

## Project Goal

This project is a learning-focused replication and demonstration of the Deep Q-Network ideas from Mnih et al. (2015). The goal is to understand how a DQN learns a control policy for Gymnasium's LunarLander-v3 environment and compare it with a reproducible random-agent baseline.

## Current Progress

- Created the GitHub repository and Python environment
- Installed PyTorch, Gymnasium, and Box2D
- Explored the observation and action spaces
- Tested the environment physics
- Created a reproducible random-agent baseline
- DQN implementation and training are not complete yet

## MVP Scope

- Implement a PyTorch Q-network
- Implement experience replay
- Use epsilon-greedy action selection
- Use separate policy and target networks
- Build the DQN training loop
- Save training data and model checkpoints
- Evaluate the trained policy against the random baseline

## Future Plans

- Plot reward and loss during training
- Experiment with hyperparameters
- Compare standard DQN with Double DQN
- Create a polished video of the trained agent
- Explore exporting the trained policy for inference

## Tech Stack

- Python 3.13
- PyTorch
- Gymnasium
- Box2D
- NumPy
- Git and GitHub
- Local files for checkpoints and training logs

No external API or external dataset is required. Training data is produced through interaction with the LunarLander simulation.

## Build Plan

1. Set up the repository, Python environment, and dependencies
2. Test the observation space, action space, and environment physics
3. Create a reproducible random-agent baseline
4. Implement the PyTorch Q-network
5. Add replay memory and epsilon-greedy action selection
6. Add the target network and DQN update step
7. Build the training loop with checkpoints and logs
8. Evaluate the trained policy and update the documentation

## Project Documents

- [Project design document](docs/lunar-lander-project-design.pdf)
- [System diagram](docs/lunar-lander-system-diagram.png)

## Reference

Mnih, V., Kavukcuoglu, K., Silver, D., et al. (2015). Human-level control through deep reinforcement learning. *Nature, 518*, 529–533.
