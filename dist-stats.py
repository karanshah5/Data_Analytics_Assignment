import csv
import sys
import argparse
import matplotlib.pyplot as plt


# to check whether the key exists in the dictionary
def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False


def main():
    # reading arguments from the terminal
    file = sys.argv[1]
    city = sys.argv[2]
    dict = {}
    sum = 0.0
    avg = 0.0

    dictList = []
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            # checking the info of only the user given city
            if (row['city'] == city):

                # if "Restaurants" is a category in the row
                if "Restaurants" in row['categories']:

                    # splitting categories based on ;
                    for cat in row['categories'].split(';'):

                        # if category not in list then add in the list as a dict element
                        if (checkKey(dict, cat) == False):
                            dict[cat] = [float(row['review_count']), [float(row['stars'])], 1]

                        # if category in the list then increase the count of it
                        elif (checkKey(dict, cat) == True):
                            dict[cat][0] = float(dict[cat][0]) + float(row['review_count'])
                            dict[cat][1].append(float(row['stars']))
                            dict[cat][2] = float(dict[cat][2]) + 1


                # if restaurant is not a category in the row
                else:

                    # adding category to the list
                    for cat in row['categories'].split(';'):
                        if (not cat in dictList):
                            dictList.append(cat)

    # deleting the category that doesnt have "Restaurants" cat from the dictionary
    for cat in dictList:
        if cat in dict:
            del dict[cat]

    # deleting the category "Restaurants" itself from the dictionary
    del dict['Restaurants']

    sortedDict = {}

    # calculating the sum and the average and sorting the dictionary
    for item in sorted(dict, key=dict.get, reverse=True):
        sum = 0.0
        for element in dict[item][1]:
            sum = sum + element

        avg = sum / dict[item][2]
        sortedDict[item] = int(dict[item][0])

        # getting stats to plot the graph
    x = list(sortedDict)[:10]
    y = list(sortedDict.values())[:10]
    fig, ax = plt.subplots()
    plt.bar(x, y, align='center', alpha=0.5)
    plt.xlabel('Category')
    plt.xticks(rotation='vertical')
    plt.ylabel('Reviews')
    plt.title('Top 10 Restaurants Category by reviews')
    plt.show()


if __name__ == "__main__":
    main()