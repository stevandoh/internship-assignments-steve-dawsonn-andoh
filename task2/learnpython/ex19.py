#function count number of cheese and crackers 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boces of crackers!"% boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
# cheese_and_crackers function is calld
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_crackers = 10 

cheese_and_crackers(10 + 20, 5 +6)

print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese +100, amount_crackers + 1000)


#Study drill
def practice(data1, data2):
    print data1 , data2

practice (1,2)
practice("one","two")
practice (True, False)
practice(2<5,6<10)
practice(50 %2 , 100% 6)
practice ("Trump", "50 missiles")
practice(10.0/50, 10**2)
practice(12-2-3-4, 23/3)
practice ("asds\nsfs\n",1)
practice("Hello","Goodbye")

#