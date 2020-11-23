import numpy as np
import matplotlib.pyplot as plt


def formula(size = 100):
    n = np.random.standard_normal(size+1)
    result = lambda t: t*n[0] + np.sqrt(2)*np.sum([np.sin(i * np.pi * t)/(i * np.pi)*n[i] for i in range(1, size+1)], axis=0)
    return result

def graph_plot(x, y, name, color):
    plt.grid() == True
    plt.title(name)
    plt.plot(x, y, color=color)
    plt.show()

def graph_hist(k, delta, size = 1000):
    hist_arr = np.zeros(N)
    for i in range(N):
        result = formula()
        time = 0
        current = result(0)
        while -k < current < k:
            time += delta
            current = result(time)
        hist_arr[i] = time
    plt.grid() == True
    plt.xlabel("Математичне очікування: {}.\n Дисперсія: {}.".format(np.mean(hist_arr), np.var(hist_arr)))
    plt.title("Емпіричний закон розподілу")
    plt.hist(hist_arr, density=True, bins=20, color='orange', edgecolor="white", range = (0, np.quantile(hist_arr, 0.95)))
    plt.show()

N = 100

result = formula()
x_arr = np.linspace(0, 1, 200)
y_arr = np.array([result(i) for i in x_arr])
graph_plot(x_arr, y_arr, "Вінерівський процес", 'green')

y_mean = np.mean([formula()(x_arr) for i in range(200)], axis = 0)
graph_plot(x_arr, y_mean, "Середнє арифметичне", 'orange')

y_var = np.var([formula()(x_arr) for i in range(200)], axis = 0)
graph_plot(x_arr, y_var, "Дисперсія", 'red')

graph_hist(1, 0.01)