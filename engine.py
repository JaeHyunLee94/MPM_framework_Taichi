import taichi as ti


class Engine:

    def __init__(self, dt, grid_res, dim=3):
        self.dim = dim
        self.dt = dt
        self.substep_dt = dt
        self.grid_res = grid_res
        self._is_grid_initialized = False
        self.particle_system_list = dict()
        ti.init(arch=ti.gpu)

        pass

    def init_grid(self):
        self._is_grid_initialized = True
        pass

    def set_param(self):
        pass

    def add_particle_group(self):
        pass

    def substep(self):
        pass

    def add_obstacle(self):
        pass

    def __p2g(self):
        pass

    def __g2p(self):
        pass

    def __update_grid(self):
        pass

    def __update_particle(self):
        pass

    pass
