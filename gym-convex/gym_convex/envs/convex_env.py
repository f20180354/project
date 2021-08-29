import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ConvexEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, array, step_size):
        super(Convex_env, self).__init__()
        self.array = array
        self.x = 0
        self.y = 0
        self.cost = 0
        self.step_size = step_size
        self.action_space = spaces.Discrete(2) # GO down the minima and STOP once limit is reached.
        self.observation_space = spaces.box(low=np.array([-100,-100]), high=np.array([+100,+100]), shape=(0,2), dtype=np.float16) # Observation space = (x,y)

    def _reset(self):
        # Resetting state to initial state
        self.x = 0 # Resetting x cordinate
        self.y = 0 # Resetting y cordinate
        return self._step()

    def _step(self, action):

        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self._take_action(action)
        self.current_step += 1
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.cost <= 0.0001
        return ob, reward, episode_over, {}

    def _take_action(action):
        action[0] = action_type

        self.cost = array[0]*x*x + array[1]*y*y + array[2]*x*y + array[3]*x + array[4]*y
        delta_x = (2*array[0]*x + array[2]*y + array[3])*step_size
        delta_y = (2*array[1]*y + array[2]*x + array[4])*step_size
        self.x = x - delta_x
        self.y = y - delta_y

    def _get_reward(self):
        optimal_x = (array[2]*array[4] - 2*array[1]*array[3])/(4*array[0]*array[1] - array[2]*array[2])
        optimal_y = (-array[3] - 2*array[0]*optimal_x)/(array[2])
        optimal_cost = array[0]*optimal_x*optimal_x + array[1]*optimal_y*optimal_y + array[2]*optimal_x*yoptimal_y + array[3]*optimal_x + array[4]*optimal_y
        diff = (optimal_cost - cost)*(optimal_cost - cost)
        return 1/diff

    def _render(self, mode='human', close=False):
        print(f'Step: {self.current_step}')
        print(f'Co-ordinates: ({self.x},{self.y})')
        print(f'Function value: {self.cost}')
        print(f'Reward for this step: {reward}')