import bisect


class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.cuisine_dict = defaultdict(list)
        self.food_dict = defaultdict(str)
        self.food_rating = defaultdict(int)
        for i in range(len(foods)):
            self.food_dict[foods[i]] = cuisines[i]
            self.food_rating[foods[i]] = ratings[i]
            bisect.insort(self.cuisine_dict[cuisines[i]], (-ratings[i], foods[i]))


    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.food_dict[food]
        self.cuisine_dict[cuisine].remove((-self.food_rating[food], food))
        bisect.insort(self.cuisine_dict[cuisine], (-newRating, food))
        self.food_rating[food] = newRating
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.cuisine_dict[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)