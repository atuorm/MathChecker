import statistics

def cmath():
    # creating an empty list
    lst = []
    # Defining question number
    q = input("Homework Question #: ")
    # number of elements as input
    n = int(input("How many numbers : "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input()) 
        lst.append(ele) # adding the element
    lst.sort()
    print('Question Number# ' + str(q), file=open("homework.txt", "a"))
    print('Your numbers sorted: ' + str(lst), file=open("homework.txt", "a"))
    mean = statistics.mean(lst)
    mode = statistics.mode(lst)
    median = statistics.median(lst)
    low = int(lst[0])
    high = int(lst[-1])
    r1 = high - low
    print('\nShow Your Mean Work:\n' + str(lst) + ' / ' + str(n), file=open("homework.txt", "a"))
    for x in lst:
        meansum = sum(lst)
        ans = sum(lst) / n
    print("   " + str(meansum) + ' / ' + str(n) + ' = ' + str(ans), file=open("homework.txt", "a"))
    print('\n')
    print('\nShow Your Range Work:\n' + str(high) + ' - ' + str(low) + ' = ' + str(r1), file=open("homework.txt", "a"))
    print('\nMean: ' + str(mean), file=open("homework.txt", "a"))
    print('Median: ' + str(median), file=open("homework.txt", "a"))
    print('Mode: ' + str(mode), file=open("homework.txt", "a"))
    print('Range: ' + str(r1), file=open("homework.txt", "a"))
    print("\n--------------------------------------------", file=open("homework.txt", "a"))
