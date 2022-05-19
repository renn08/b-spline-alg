# my implementation of b-spline curve formulation
import numpy as np
import matplotlib.pyplot as plt


class Bspline:
    def __init__(self):
        self.control_points = np.array([
            [0, 0, 0],
            [2, 3, -6],
            [-4, 5, -7],
            [3, 8, 12],
            [10, 6, 1],
        ])

        self.degree = 3
        self.control_points_num = self.control_points.shape[0]
        self.elem_num = self.degree + self.control_points_num + 1

        if self.elem_num == 1:
            self.knot_vector = np.array([0, 1])
        else:
            self.knot_vector = np.arange(0, 1, 1 / (self.elem_num - 1))
            self.knot_vector = np.append(self.knot_vector, 1)

    def print(self):
        print(self.control_points)
        print(self.control_points.shape[0])
        print(self.knot_vector)
        print(self.control_points.shape)

    def basis_func(self, partition_idx=0, degree=0, x=0):
        # degree should always between 0 and self.degree, inclusive
        # partition_idx should always between 0 and self.elem_num - 2, inclusive
        # base case:
        xi = self.knot_vector[partition_idx]
        xip1 = self.knot_vector[partition_idx + 1]
        xipp = self.knot_vector[partition_idx + degree]
        xipp1 = self.knot_vector[partition_idx + degree + 1]
        if degree == 0:
            if xi <= x < xip1:
                return 1
            return 0
        # else recursion relation:
        return (x - xi) / (xipp - xi) * self.basis_func(partition_idx, degree - 1, x) + \
               (xipp1 - x) / (xip1 - xip1) * self.basis_func(partition_idx + 1, degree - 1, x)

    def cal_pos(self):
        # needed to be implemented
        pass

    def plot_curve(self):
        fig = plt.figure()
        if self.control_points.shape[1] == 2:
            ax = fig.add_subplot()
            for i in range(self.control_points.shape[0]):
                ax.scatter(self.control_points[i][0], self.control_points[i][1])
                ax.set_xlabel('X Label')
                ax.set_ylabel('Y Label')
        elif self.control_points.shape[1] == 3:
            ax = fig.add_subplot(projection='3d')
            for i in range(self.control_points.shape[0]):
                ax.scatter(self.control_points[i][0], self.control_points[i][1], self.control_points[i][2])
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        # ax.scatter(xs, ys, zs, marker=m)
        plt.show()


if __name__ == '__main__':
    a = Bspline()
    a.print()
    a.plot_curve()
