# Implementation of Chain Matrix Multiplication using Dynamic Programming
# This program finds the minimum number of scalar multiplications needed
# to multiply a sequence of matrices and also prints the optimal order.


def matrix_chain_multiplication(dimensions):
    """
    dimensions: list of matrix dimensions, e.g. [30, 35, 15, 5, 10, 20, 25]
    Here, dimensions[i] x dimensions[i+1] gives the size of matrix i.
    Returns: minimum scalar multiplications and the optimal parenthesization.
    """
    n = len(dimensions) - 1

    if n <= 1:
        return 0, ["A1"]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    split = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    order = []

    def build_order(i, j):
        if i == j:
            order.append(f"A{i}")
            return
        order.append("(")
        build_order(i, split[i][j])
        order.append(" x ")
        build_order(split[i][j] + 1, j)
        order.append(")")

    build_order(1, n)

    return dp[1][n], ''.join(order)


# Example usage
if __name__ == "__main__":
    matrices = [30, 35, 15, 5, 10, 20, 25]
    min_cost, optimal_order = matrix_chain_multiplication(matrices)

    print("Matrix dimensions:", matrices)
    print("Minimum scalar multiplications needed:", min_cost)
    print("Optimal parenthesization:", optimal_order)
