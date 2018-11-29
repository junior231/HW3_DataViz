import csv
import matplotlib.pyplot as plt 
import numpy as np


categories = []
usa =[]
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "USA":
			usa.append([int(row[0]), row[5], row[6], row[7]])
		else:
			world.append([int(row[0]), row[5], row[6], row[7]]) 		
		line_count += 1
men_usa = []
women_usa = []

for medal in usa:
		if medal[1] == "Men":
			men_usa.append(medal)

		if medal[1] == "Women":
			women_usa.append(medal)



m = len(men_usa)
f = len(women_usa)


print('Number of men in USA' , len(men_usa))
print('Number of women in USA', len(women_usa))



print('processed', line_count, 'rows of data')

x = np.arange(2)
medals = [m,f]

fig, ax = plt.subplots()
plt.bar(x, medals)
plt.xticks(x, ('USA Men', 'USA Women'))
plt.title("Number of man and woman in USA and another countries in Olympic Winter since 1924 ")

plt.show()


