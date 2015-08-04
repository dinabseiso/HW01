# HW01_ex02_03
# NOTE: You do not run this script.
# #
# Practice using the Python interpreter as a calculator:

# 1. The volume of a sphere with radius r is 4/3 pi r^3. 
# What is the volume of a sphere with radius 5? (Hint: 392.7 is wrong!)
# volume: 523.3

r = 5
pi = 3.14
volume = (4 * pi * r**3) / 3
print(volume)


# 2. Suppose the cover price of a book is $24.95, but bookstores get a 
# 40% discount. Shipping costs $3 for the first copy and 75 cents for 
# each additional copy. What is the total wholesale cost for 60 copies?
# total wholesale cost: 945.45

discountedPrice = 24.95 * 0.60
firstShippingCost = 3
additionalShippingCost = 0.75
n = 60
firstCopyPrice = discountedPrice + firstShippingCost
additionalCopyPrice = (additionalShippingCost + discountedPrice) * (n-1)
wholesaleCost = firstCopyPrice + additionalCopyPrice
print(wholesaleCost)

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace 
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy 
# pace again, what time do I get home for breakfast?
# time: 

startHour = 6
startHourToSeconds = startHour * 3600.0
startMinutes = 52.0 
startMinutesToSeconds = startMinutes * 60
convertToOneHundred = 100.0 / 60
startTime = ( startHourToSeconds + startMinutesToSeconds ) * convertToOneHundred
print(startTime)
beginningRun = 1 * (8 + (15/60) ) * 60 
middleRun = 3 * (7+(12/60)) * 60 
endRun = 1 * (8 + (15/60)) * 60 
totalRunTime = (beginningRun + middleRun + endRun ) 
breakfast = (( startTime + totalRunTime ) / 3600.0) * (60/100.0)
round(breakfast, 2)
print(breakfast)