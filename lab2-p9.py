
m1 = float(input("Enter marks for test1: "))
m2 = float(input("Enter marks for test2: "))
m3 = float(input("Enter marks for test3: "))

avg1 = (m1 + m2) / 2
avg2 = (m1 + m3) / 2
avg3 = (m2 + m3) / 2

bestAvg = max(avg1, avg2, avg3)
print(f"Average of best two test marks out of three test’s marks is: {bestAvg}")
