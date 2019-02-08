# CHOMP: Covariant Hamiltonian optimization for motion planning

### Abstract

------

> In this paper, we present CHOMP (covariant Hamiltonian optimization for motion planning), a method for trajectory optimization, invariant to reparametrization.

- CHOMP 一种 trajectory optimization 的方法, 对reparametrization保持不变/不受reparametrization影响 

> CHOMP uses functional gradient techniques to iteratively improve the quality of an initial trajectory, optimizing a functional that trades off between a smoothness and an obstacle avoidance component.

- CHOMP 用 functional gradient 技术迭代地改进 初始traj的质量, 优化一个功能、这个功能在smoothness和oac之间有个trade-off

> CHOMP can be used to locally optimize feasible trajectories, as well as to solve motion planning queries, converging to
low-cost trajectories even when initialized with infeasible ones.
- CHOMP 可以用于局部优化可靠traj，同时也可以解决motion planning问题，使得即使初始化不稳定的traj也收敛到稳定
> It uses Hamiltonian Monte Carlo to alleviate the problem of
> convergence to high-cost local minima (and for probabilistic completeness), and is capable of respecting hard constraints along the trajectory.

- 使用Hamiltonian Monte Carlo来解决(缓和)老是收敛到high-cost的localminima(为了概率完整？？？), 也可以解决 需要respecting hard constraints的traj问题,(比如要求robot arm只能在z=0的平面运动????)

>   We present extensive experiments with CHOMP on manipulation and locomotion tasks, using sevendegree-of-freedom manipulators and a rough-terrain quadruped robot.

- 我们展示了广泛的extensive的使用CHOMP的expe，在manipulation、locomotion的任务上，我们用了7DOF的manipulator和粗糙地形四足机器人。

  

## 1. Introduction

 我们提出了一个traj opti tech 为了mo planning 在high-dim. key motion for it 是 focus on producing optimal motion:incorporating dynamics, smoothness, and obstacle avoidance in a mathematically precise objective. 

> Despite a rich theoretical history and successful applications, most notably in the control of spacecraft and rockets, trajectory optimization techniques have had limited success in motion planning

- 尽管traj optimizaiton理论丰富、应用成果，特别是在spacecraft、rockets方面，但是traj opti tech 在$\color{red}{motion\quad planning}$上面成功很有限

> Much of this may be attributed to two causes: the large computational cost for evaluating objective functions and their higher-order derivatives in highdimensional spaces, and the presence of local minima when considering motion planning as a (generally non-convex) continuous optimization problem.

- 原因be attributed to 两个：1.computational cost for evaluating 高维ObjFun&its derivatives, 以及2. 当把motion planning考虑成连续optimizaiton问题时，non-convex带来的local minima

> Our algorithm CHOMP, short for covariant Hamiltonian optimization for motion planning, is a simple variational strategy for achieving good trajectories. This approach to motion planning builds on two central tenets:

- CHOMP是一个简易的alternative strategy for 达到一个好的traj, 这个appr to motion planning 建立在两个中心tenets信条:

#### 1. Gradient information is often available and can be computed inexpensively

. Robot motion planning problems share a common objective of producing smooth
motion while avoiding obstacles.  

1. Smoothness term: $\mathfrak{u}_{smooth}[\xi]$  capturing dynamics of traj
2. Obstacle term: $\mathfrak{u}_{obs}[\xi]$ capturing requirement of avoid obs and margin from tm

>  We define the smoothness functional naturally in terms of a metric in the space of trajectories.

- 自然就in terms of 某种在traj space里面的metic 来定义smooth fun

> By doing so, we generalize many prior notions of trajectory smoothness, including springs and dampers models of trajectories (Quinlan and Khatib, 1993). Each of these prior notions are just one type of valid metric in the space of trajectories

- 通过这样做，我们概括了许多先前的轨迹平滑度概念，包括弹道和阻尼器轨迹模型，这些notions都是一种valid metric in traj space

> With this generalization, we are able to include higher-order derivatives or
> configuration-dependent metrics to define smoothness.

- 推广之后，我们可以把高阶derivatives ???或者config-depend??? 的metrics包含进来来定义smoothness

> The obstacle functional is developed as a line integral of a scalar cost field c, defined so that it is invariant to retiming. Consider a robot arm sweeping through a cost field, accumulating cost as is moves. Regardless of how fast or slow the arm moves through the field, it must accumulate the exact same cost.

- $\mathfrak{u}_{obs}[\xi]​$ 被开发成一个线积分， 在scalar cost field c 上面， 被定义得和retiming时间无关，和快慢无关、robot arm 扫过(scope,范围)cost field，这个accumulated cost 积分必须是快慢都一样

> The physical intuition of an arm sweeping through a cost field, hints at a further simplification. Instead of computing the cost field in the robot’s high-dimensional configuration space, we compute it in its workspace (typically two or three dimensional) and use body points on the robot to accumulate workspace cost to compute $\mathfrak{u}_{obs}[\xi]​$.

- what's the difference between computing cost in c-space and w-space(using body points on robot)???

#### 2. Trajectory optimization should be invariant to parametrization.



