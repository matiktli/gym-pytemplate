from gym.envs.registration import register

register(
    id='pytemplate-v0',
    entry_point='gym_pytemplate.envs:PytemplateEnv',
)
