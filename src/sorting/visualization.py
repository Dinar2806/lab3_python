import matplotlib.pyplot as plt

filename = "image.png"


x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.scatter(x, y)


plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Пример линейного графика")

plt.savefig(filename, dpi=300, bbox_inches='tight')