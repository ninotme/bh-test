#stable baseline test 
import gym

from stable_baselines3 import A2C, PPO

env = gym.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)

vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    #vec_env.render("human")
    # VecEnv resets automatically
    # if done:
    #   obs = vec_env.reset()
