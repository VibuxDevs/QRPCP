import math
import numpy as np

def existential_hunger_constant(H):
    return sum(
        (math.sin(i) + math.cos(i**2)) / math.sqrt(i + 1)
        for i in range(1, H + 1)
    )

def pizza_entropy_matrix(P, F, C):
    size = P + F

    if size <= 0:
        return np.array([[0]])

    matrix = np.zeros((size, size))

    for x in range(size):
        for y in range(size):
            matrix[x][y] = ((x + 1)**2 + (y + 1)**3 + C) % 17

    return matrix

def dominant_pizza_eigenvalue(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return max(abs(ev) for ev in eigenvalues)

def lunar_pizza_correction(lambda_pizza, M):
    return lambda_pizza * (1 + math.sin(2 * math.pi * M))

def bro_momentum(W):
    # Integral of x² + ln(x+1) from 0 to W
    return (
        (W**3) / 3
        + ((W + 1) * math.log(W + 1) - W)
    )

def cat_influence_field(C, T):
    total = 0

    for n in range(1, C + 2):
        total += ((-1) ** n * T) / math.factorial(n)

    return total

def friendship_debt(F):
    if F <= 0:
        return 1

    return friendship_debt(F - 1) + (F ** 2)

def calculate_pizza_slices(H, P, F, M, C, T, W):
    ehc = existential_hunger_constant(H)

    pem = pizza_entropy_matrix(P, F, C)
    lambda_pizza = dominant_pizza_eigenvalue(pem)

    lpc = lunar_pizza_correction(lambda_pizza, M)

    bm = bro_momentum(W)

    cif = cat_influence_field(C, T)

    fd = friendship_debt(F)

    pds = ((ehc * lpc) + bm) / fd + cif

    slices = abs(math.floor((pds % 8192) / math.pi))

    # Safety Adjustment
    max_slices = P * 8

    if slices > max_slices:
        slices = max_slices

    if slices < 0:
        slices = 0

    return {
        "EHC": ehc,
        "LambdaPizza": lambda_pizza,
        "LPC": lpc,
        "BM": bm,
        "CIF": cif,
        "FriendshipDebt": fd,
        "PDS": pds,
        "Slices": slices,
    }

if __name__ == "__main__":
    print("=== Quantum Recursive Pizza Consumption Predictor ===\n")

    H = int(input("Hunger Level (0-100): "))
    P = int(input("Pizzas Available: "))
    F = int(input("Nearby Friends: "))
    M = float(input("Moon Phase (0.0-1.0): "))
    C = int(input("Visible Cats: "))
    T = float(input("Room Temperature (Kelvin): "))
    W = int(input('Times you said "bro" today: '))

    result = calculate_pizza_slices(H, P, F, M, C, T, W)

    print("\n=== Results ===")
    for key, value in result.items():
        print(f"{key}: {value}")