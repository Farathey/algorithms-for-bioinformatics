import fibonacci as fib
import matplotlib.pyplot as plt
import positions as pos
# we use numpy.log() to get natural logarithm value from our times
import numpy as np
import probability as prb
# this method returns processor time; by substracting time measured the begining of function
# from the time measured at the end of it we get precise time of calculation, without slowing down calculations
from time import clock


fibRecTimes = []  # the list of times from the recursion method of calculating values from Fibonacci series
fibIteTimes = []  # the list of times from the iteration method of calculating values from Fibonacci series
nRec = []  # the list of int numbers of expressions in Fibonacci series
nIte = []

print('Recursion method:')

# this loop prints out and appends to lists (so they can be shown in the diagram) values
# from Fibonacci series generated with recursion method

for i in range(10, 30):
    start = clock()  # measurement of processor time just before calculation
    value = fib.fibonacciRec(i)
    end = clock()  # measurement of processor time just after calculation
    time = end - start  # this is the time of our calculation
    fibRecTimes.append(time)
    nRec.append(i+1)
    print(i+1, 'value =', value, 'time = %5.8f seconds' % (time))

print('\nIteration method:')

# this loop prints out and appends to lists (so they can be shown in the diagram) values
# from Fibonacci series generated with iteration method

for i in range(10, 50):
    value, time = fib.fibonacciIte(i)
    fibIteTimes.append(time)
    nIte.append(i+1)
    print(i+1, 'value =', value, 'time = %5.8f seconds' % (time))

# plot of times of both methods *** time(F(k)) ***

# creates two subplots nex to each other
fig, (plot1, plot2) = plt.subplots(1, 2)
plot1.plot(nRec, fibRecTimes)   # the first plot with times of recursion method
# the second plot with times of iteration method
plot2.plot(nIte, fibIteTimes)
plot1.grid()    # creates grid lines on the plot
plot2.grid()
plot1.set_title('Recursion')        # sets the title of the plot
plot1.set_ylabel('Time [seconds]')  # sets the label of y axis
plot1.set_xlabel('n')   # sets the label of x axis
# sets the values on x axis to be exact as in nRec list (numbers of expression in Fibonacci series)
plot1.set_xticks(nRec)
plot2.set_title('Iteration')        # sets title of the second plot
plot2.set_xlabel('n')   # sets label of the x asxis in second plot
# sets the values on x axis to be exact as in nIte list (numbers of expression in Fibonacci series)
plot2.set_xticks(nIte)
plt.show()  # shows the plot

# plot of times of both methods in logarythmic scale *** log(time(F(k))) ***

# creates two subplots nex to each other
fig2, (plot3, plot4) = plt.subplots(1, 2)
# the first plot with log(times of recursion method)
plot3.plot(nRec, np.log(fibRecTimes))
# the second plot with log(times of iteration method)
plot4.plot(nIte, np.log(fibIteTimes))
plot3.grid()    # creates grid lines on the plot
plot4.grid()
plot3.set_title('Recursion')        # sets the title of the plot
plot3.set_ylabel('log(Time)')       # sets the label of y axis
plot3.set_xlabel('n')   # sets the label of x axis
# this set_xticks sets the values on x axis to be exact as in nRec list (numbers of expression in Fibonacci series)
plot3.set_xticks(nRec)
plot4.set_title('Iteration')        # sets title of the second plot
plot4.set_xlabel('n')   # sets label of the x asxis in second plot
# this set_xticks sets the values on x axis to be exact as in nIte list (numbers of expression in Fibonacci series)
plot4.set_xticks(nIte)
plt.show()  # shows the plot

'''
Results of the run from 10 to 50 are shown in the 'Fibonacci results' dierctory
It took almost 5 houres to ganerate values with recursion method (value for n = 50 took ~6944 seconds which is almost 2 hours)
and only ~1 second to generate them with iteration method
As we can see on the time(F(n)) diagrams time of the recursion method grows exponentialy and
time of the iteration method is relativly 'linear' - changes occure in the 5th position after the decimal point,
so it's very very minor
In logarythmic diagrams we can see that recursion method's time is more linear, due to logarythmisation of
exponential values, diagram of iteraion method looks fairly similar to previous one
(changes in y value are more extansive due to change of scale)

note: n values are moved by 1 in the diagrams, I noticed it later and changed the program a little bit
I leave the diagrams untouched because it would take another 5 hours to generate new ones
'''

number = 5000  # number of how many positions we want to generate with both methods

# we generate (number) of random positions in Cartesian system
x, y = pos.randomPositions(number)

# lists of positions which fulfill the condition of being in circle
circleX = []
circleY = []

center = 0.0  # both positions (x, y) of center are equal 0.0

# this loop checks if given point is in circle with radius = 1
for i in range(0, number):
    d = ((x[i] - center)**2)+((y[i] - center)**2)
    if d <= (1)**2:
        circleX.append(x[i])
        circleY.append(y[i])

# generates scatter plot with 2 layers: first conatins all points, second contains only those points which fulfill
# condition in the loop above
# creates two subplots nex to each other
fig3, (ax1, ax2) = plt.subplots(1, 2)

# first subplot with two layers
# first layer with all points drawed in random in cartesian system, colour = blue
ax1.scatter(x, y, color=(0, 0, 1,), s=1)
# second layer points fulfilling condition 𝑥^2 + 𝑦^2 <= 1, colour = red
ax1.scatter(circleX, circleY, color=(1, 0, 0), s=1)
ax1.grid()  # adds grid lines to the plot
ax1.set_title('Cartesian')  # sets the title of the first subplot
# equalizes axises so the equal values on both of them are evenly spaced
ax1.axis('equal')

# we generate (number) of random positions in polar system
x2, y2 = pos.randomPositionsPolar(number)

# second subplot with points drawed in random in polar system and projected onto cartesian one, colour = blue
ax2.scatter(x2, y2, s=1, color=(0, 0, 1))
ax2.grid()  # adds grid lines to the plot
ax2.set_title('Polar')  # sets the title of the first subplot
# equalizes axises so the equal values on both of them are evenly spaced
ax2.axis('equal')
plt.show()

'''
Points generated in cartesian coordinates are distributed evenly
Those generated in polar coordinates are mostly concentrated near the center of the circle
It's caused by distribution of similar number of points on different radiuses - if we take equal number of points on r = 1, and r2 = 2
those on r will be 2 times closer to each other - the smaller radius is the closer points are to each other
'''

# generates 3 sets of motifs matrixes, for 10000, 1000 and 100 samples
motifs, deviation = prb.generateMotifs(10000)
motifs2, deviation2 = prb.generateMotifs(1000)
motifs3, deviation3 = prb.generateMotifs(100)

# generates matrixes of probability for each matrix generated above
probability = prb.probabilityInPositions(motifs, 10000)
probability2 = prb.probabilityInPositions(motifs2, 1000)
probability3 = prb.probabilityInPositions(motifs3, 100)

print('\n \n \n')

# this loop prints out probabilities with which given base occures
print('   [100]  [1000]  [10000]        <- number of samples')
for i in range(8):
    print('In position', i+1, 'probability of occuring of given base equals')
    print('A: %1.3f  %1.3f   %1.3f' %
          (probability3[0][i], probability2[0][i], probability[0][i]))
    print('C: %1.3f  %1.3f   %1.3f' %
          (probability3[1][i], probability2[1][i], probability[1][i]))
    print('G: %1.3f  %1.3f   %1.3f' %
          (probability3[2][i], probability2[2][i], probability[2][i]))
    print('T: %1.3f  %1.3f   %1.3f' %
          (probability3[3][i], probability2[3][i], probability[3][i]))

# here we print tables of standard deviations for each nuber of samples
# print('{:^5}'.format('|')) prints 5 whitespaces and places '|' char in the central position
# here we print 4th position after the decimal point, becasue loop with 10000 samples changes occure in this place at max
print('\nTable of standard deviations in each position 100 samples\n')
for i in range(4):
    print('%1.4f' % (deviation3[i][0]), '{:^5}'.format('|'), '%1.4f' % (deviation3[i][1]),
          '{:^5}'.format('|'), '%1.4f' % (deviation3[i][2]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation3[i][3]),
          '{:^5}'.format('|'), '%1.4f' % (deviation3[i][4]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation3[i][5]),
          '{:^5}'.format('|'), '%1.4f' % (deviation3[i][6]), '{:^5}'.format('|'), '%1.4f' % (deviation3[i][7]))
    print()

print('\nTable of standard deviations in each position 1000 samples\n')
for i in range(4):
    print('%1.4f' % (deviation2[i][0]), '{:^5}'.format('|'), '%1.4f' % (deviation2[i][1]),
          '{:^5}'.format('|'), '%1.4f' % (deviation2[i][2]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation2[i][3]),
          '{:^5}'.format('|'), '%1.4f' % (deviation2[i][4]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation2[i][5]),
          '{:^5}'.format('|'), '%1.4f' % (deviation2[i][6]), '{:^5}'.format('|'), '%1.4f' % (deviation2[i][7]))
    print()

print('\nTable of standard deviations in each position 10000 samples\n')
for i in range(4):
    print('%1.4f' % (deviation[i][0]), '{:^5}'.format('|'), '%1.4f' % (deviation[i][1]),
          '{:^5}'.format('|'), '%1.4f' % (deviation[i][2]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation[i][3]),
          '{:^5}'.format('|'), '%1.4f' % (deviation[i][4]), '{:^5}'.format(
              '|'), '%1.4f' % (deviation[i][5]),
          '{:^5}'.format('|'), '%1.4f' % (deviation[i][6]), '{:^5}'.format('|'), '%1.4f' % (deviation[i][7]))
    print()

'''
If we were to approximate values from the probability matrixes we would get profil_in matrix - the more samples we use the closer
to the values from profil_in matrix we will probably get

The more samples we will generate the smaller values in standard deviation matrix we will achive
It indicates that greater number of samples leads to values closer to average
'''
