# my implementation of b-spline curve formulation
import numpy as np
import matplotlib.pyplot as plt


class Bspline:
    def __init__(self):
        # example 0 degree in cal_pos is 2
        self.control_points = np.array([
            [0.0, 0.0, 0.0],
            [2.0, 3.0, 6.0],
            [-4.0, 5.0, -7.0],
            [3.0, 8.0, 12.0],
            [10.0, 6.0, 1.0],
            [1.0, 1.0, 1.0],
            [3.0, 4.0, -5.0],
            [-3.0, 6.0, -6.0],
            [4.0, 9.0, 13.0],
            [11.0, 7.0, 2.0],
        ])

        # # example 1 degree in cal_pos is 2
        # self.control_points = np.array([
        #     [0.0, 0.0, 0.0],
        #     [1.0, 0.0, 0.0],
        #     [2.0, 0.0, 0.0],
        #     [2.0, 0.5, 0.0],
        #     [3.0, 1.0, 0.0],
        #     [4.0, 1.0, 0.0],
        #     [5.0, 1.2, 0.0],
        #     [6.0, 1.5, 0.0],
        #     [10.0, 3.0, 0.0],
        #     [11.0, 4.0, 0.0],
        #     [12.0, 11.0, 0.0],
        #     [11.0, 4.0, 0.0],
        #     [10.0, 3.0, 0.0],
        #     [6.0, 1.5, 0.0],
        #     [5.0, 1.2, 0.0],
        #     [4.0, 1.0, 0.0],
        #     [3.0, 1.0, 0.0],
        #     [2.0, 0.5, 0.0],
        #     [2.0, 0.0, 0.0],
        #     [1.0, 0.0, 0.0],
        #     [0.0, 0.0, 0.0],
        # ])

        # example 2
        # the control points same as example 1 and the degree selected for cal_pos is 3 instead of 2

        self.degree = 3
        self.n = self.control_points.shape[0] - 1
        self.elem_num = self.degree + self.n + 1
        self.internal_nodes = self.n - self.degree + 1
        # the num of edge nodes = self.degree

        if self.elem_num == 1:
            self.knot_vector = np.array([0, 1])
        else:
            self.knot_vector = np.zeros((self.degree,))
            temp = np.arange(0, 1, 1 / (self.internal_nodes + 1))
            temp = temp[1:]
            self.knot_vector = np.append(self.knot_vector, temp)
            self.knot_vector = np.append(self.knot_vector, np.ones((self.degree,)))

    def print(self):
        print(self.control_points)
        print(self.control_points.shape[0])
        print(self.knot_vector)
        print(self.control_points.shape)

    def basis_func(self, partition_idx=0, degree=0, x=0.0):
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
        # just do it to avoid error (denominator be zero)
        if xipp - xi == 0:
            term1 = 0
        else:
            term1 = (x - xi) / (xipp - xi) * self.basis_func(partition_idx, degree - 1, x)
        if xipp1 - xip1 == 0:
            term2 = 0
        else:
            term2 = (xipp1 - x) / (xipp1 - xip1) * self.basis_func(partition_idx + 1, degree - 1, x)
        return term1 + term2

    def cal_pos(self, t):
        # needed to be implemented
        # let degree be 2
        degree = 3
        result = np.zeros_like(self.control_points[0])
        for i in range(self.n + 1 - degree):
            result += self.control_points[i] * self.basis_func(i, degree, t)
        return result

    def plot_curve(self):
        fig = plt.figure()
        if self.control_points.shape[1] == 2:
            ax = fig.add_subplot()
            for i in range(self.control_points.shape[0]):
                ax.scatter(self.control_points[i][0], self.control_points[i][1])

            for pt in np.linspace(0, 1, 100):
                ax.scatter(self.cal_pos(pt)[0], self.cal_pos(pt)[1], color='red')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
        elif self.control_points.shape[1] == 3:
            ax = fig.add_subplot(projection='3d')
            for i in range(self.control_points.shape[0]):
                ax.scatter(self.control_points[i][0], self.control_points[i][1], self.control_points[i][2])

            for pt in np.linspace(0, 1, 100):
                ax.scatter(self.cal_pos(pt)[0], self.cal_pos(pt)[1], self.cal_pos(pt)[2], color='red', s=10)

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        # ax.scatter(xs, ys, zs, marker=m)
        plt.savefig("example2.png")
        plt.show()


if __name__ == '__main__':
    a = Bspline()
    a.print()
    a.plot_curve()



