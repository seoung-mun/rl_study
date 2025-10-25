import gymnasium as gym

def main():
    env = gym.make("LunarLanderContinuous-v3", render_mode="human")
    obs, info = env.reset()

    for _ in range(600):
        action = env.action_space.sample()  # 랜덤 행동
        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            obs, info = env.reset()

    env.close()

if __name__ == "__main__":
    main()
