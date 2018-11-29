import csv
import matplotlib.pyplot as plt

categories = []
italy = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "ITA":
			italy.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

men = []
women = []

for gender in italy:
	if gender[1] == "Men":
		men.append(gender)

	if gender[1] == "Women":
		women.append(gender)

print('Number of men in ITALY', len(men))
print('Number of women in ITALY', len(women))
print('procesed', line_count, 'rows of data')

totalMedals = len(men) + len(women)

#percentage of all medals
men_percentage = int(len(men) / totalMedals * 100)
women_percentage = int(len(women) / totalMedals * 100)



labels = "Men", "Women"
sizes = [men_percentage, women_percentage]
colors = ['grey', 'skyblue',]
explode = (0.01, 0.01,)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Gender of ITALY in the Olympics")
plt.xlabel("Men vs Women")
plt.show()