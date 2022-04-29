import matplotlib.pyplot as plt
import pandas as pd

# get data from csv file
data = pd.read_csv('Database/tabela_danych.csv', header=0)
data_subjects = data.iloc[:, 1:].values
data_regions = data_subjects.transpose()


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

# generate for regions
generate_boxplot(regions, data_regions)

# generate for subjects
generate_boxplot(subjects, data_subjects)
