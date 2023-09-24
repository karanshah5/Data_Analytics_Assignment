import csv
import sys
import argparse


# numOfBus: the number of businesses in the city
def numOfBus(file, city):
    # Return an int with number of businesses in a city
    count = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                count = count + 1
    return count


# avgStars: the average number of stars of a business in the city
def avgStars(file, city):
    sum = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                sum = sum + float(row['stars'])
    return sum


# numOfRestaurants: the number of restaurants in the city
def numOfRestaurants(file, city):
    count = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    count += 1
    return count


# avgStarsRestaurants: the average number of stars of restaurants in the city
def avgStarsRestaurants(file, city):
    sum = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + float(row['stars'])
    return sum


# avgNumOfReviews: the average number of reviews for all businesses in the city
def avgNumOfReviews(file, city):
    sum = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                sum = sum + int(row['review_count'])
    return sum


# avgNumOfReviewsBus: the average number of reviews for restaurants in the city
def avgNumOfReviewsBus(file, city):
    sum = 0
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + int(row['review_count'])
    return sum


def main():
    # getting input from the terminal
    file = sys.argv[1]
    city = sys.argv[2]

    # each part calls the respectative method
    resCount = numOfRestaurants(file, city)
    busCount = numOfBus(file, city)
    avgBusStars = avgStars(file, city) / busCount
    avgResStars = avgStarsRestaurants(file, city) / resCount
    avgBusReviews = avgNumOfReviews(file, city) / busCount
    avgResReviews = avgNumOfReviewsBus(file, city) / resCount

    # printing each part in the required format
    print("numOfBus:", busCount, " in ", city)
    print("avgStars:", avgBusStars, " in ", city)
    print("numOfRestaurants: ", resCount, " in ", city)
    print("avgStarsRestaurants: ", avgResStars, " in ", city)
    print("avgNumOfReviews: ", avgBusReviews, " in ", city)
    print("avgNumOfReviewsBus: ", avgResReviews, " in ", city)


if __name__ == "__main__":
    main()