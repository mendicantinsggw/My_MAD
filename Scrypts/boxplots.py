import matplotlib.pyplot as plt
import numpy as np

# subject percent ranges for each region
data = [
	[31.20, 31.37, 30.83, 30.57, 33.92, 39.49, 65.60, 49.96, 28.07],
	[30.29, 30.97, 36.45, 30.84, 35.65, 41.05, 65.03, 44.49, 27.77],
	[33.05, 36.91, 38.04, 31.21, 35.11, 33.74, 61.29, 46.15, 31.20],
	[31.98, 33.78, 31.14, 31.63, 31.97, 33.37, 64.60, 54.33, 25.27],
	[33.46, 32.78, 37.91, 34.82, 36.41, 33.13, 62.89, 41.91, 32.37],
	[35.00, 38.67, 42.64, 34.68, 42.69, 44.50, 64.33, 49.29, 35.13],
	[35.25, 37.49, 44.74, 38.57, 40.27, 40.65, 68.80, 51.77, 36.80],
	[32.25, 27.82, 27.72, 31.54, 32.44, 33.82, 64.50, 48.21, 27.41],
	[32.82, 35.50, 34.35, 30.91, 35.21, 31.64, 60.81, 44.63, 30.84],
	[35.13, 42.04, 35.83, 33.59, 36.81, 43.42, 64.37, 52.55, 32.33],
	[32.87, 36.41, 38.15, 34.14, 33.13, 38.31, 67.02, 43.11, 31.67],
	[32.67, 34.38, 35.55, 34.28, 35.16, 37.45, 65.16, 51.96, 29.05],
	[37.17, 36.39, 34.23, 31.18, 36.84, 33.47, 61.69, 49.73, 29.43],
	[30.39, 30.40, 36.55, 29.96, 31.50, 30.51, 63.78, 46.82, 26.22],
	[32.22, 32.81, 35.28, 32.15, 36.45, 39.17, 64.25, 52.65, 28.58],
	[32.85, 33.54, 39.14, 30.48, 34.55, 35.51, 65.76, 54.57, 27.86]
]

# the same data but each subject is in the row instead of the column
data_t = np.transpose(data)

regions = [ # short regions names
	"Dol",
	"Kuj",
	"Lube",
	"Lubu",
	"Łdz",
	"Mał",
	"Maz",
	"Opol",
	"Podk",
	"Podl",
	"Pom",
	"Ślą",
	"Świ",
	"Warm",
	"Wlkp",
	"Zach"
]

subjects = [ # short subjects names
	"biol",
	"chem",
	"fiz",
	"geo",
	"hist",
	"inf",
	"j. ang",
	"j. pol",
	"mat",
]

colors = [
	"black",
	"grey",
	"silver",
	"black",
	"grey",
	"silver",
	"black",
	"grey",
	"silver",
	"black",
	"grey",
	"silver",
	"black",
	"grey",
	"silver",
	"black"
]

bplots = []

def generate_boxplot(labels, plotdata):
	fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8,6))
	bplot = axes.boxplot(
		x=plotdata,
		labels=labels,
		vert=False,
		patch_artist=True)
	for patch, color in zip(bplot['boxes'], colors):
		patch.set_facecolor(color)
	plt.show()

# for regions
generate_boxplot(regions, data)

# for subjects
generate_boxplot(subjects, np.transpose(data_t)) # for some weird reason data has to be transposed twice
