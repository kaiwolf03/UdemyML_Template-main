import matplotlib.pyplot as plt

grade_ben = [56, 64, 89, 45]
grade_tobi = [95, 34, -30, 56]

# Plot
plt.plot(range(len(grade_ben)), grade_ben, color="blue")
plt.plot(range(len(grade_tobi)), grade_tobi, color="green")
plt.legend(["Ben", "Tobi"])
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Bla Bla")
plt.show()

# Scatter
plt.scatter(range(len(grade_ben)), grade_ben, color="blue")
plt.scatter(range(len(grade_tobi)), grade_tobi, color="green")
plt.legend(["Ben", "Tobi"])
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Bla Bla")
plt.show()
