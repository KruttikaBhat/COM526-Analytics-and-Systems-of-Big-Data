import matplotlib.pyplot as plt

input=[22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 39, 20, 10, 26, 24, 27, 28, 26, 28, 18, 32, 29,
25, 31, 27]

stems=[]
for i in input:
    stems.append(int(i/10))

stems=sorted(stems)
print(stems)

plt.ylabel('Data')   # for label at y-axis
plt.xlabel('stems')   # for label at x-axis
#plt.xlim(0, 10)   # limit of the values at x axis
plt.stem(stems, input, use_line_collection="True")   # required plot
plt.show()

#bell-shaped
