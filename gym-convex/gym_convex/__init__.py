from gym.envs.registration import register

register(
    id='convex-v0',
    entry_point='gym_convex.envs:ConvexEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_convex.envs:ConvexExtraHardEnv',
)