import taichi as ti


class Grid:
    def __init__(self, dim, grid_res,x_len,y_len,z_len):
        self.x_len=x_len
        self.y_len=y_len
        self.z_len = z_len
        self.dx= x_len / grid_res
        self.dy = x_len / grid_res
        self.dz = x_len / grid_res
        self.grid_res = grid_res
        self.grid_v = ti.Vector.field(dim, float, (grid_res,) * dim)
        self.grid_m = ti.field(float, (grid_res,) * dim)

    def get_grid_res(self):
        return self.grid_res

    pass
