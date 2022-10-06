from print_me_first import print_me_first
import matplotlib.pyplot as plt
import csv

"""
Function name: annotationLabel
Function description: To add labels to line plots (annotation)
                      zip joins x and y coordinates in pairs
@param xlist - x list of data (holds years)
       ylist - x list of data (holds rates)
@return none
"""
def annotationLabel(xlist, ylist):
    ax = plt.gca() # get current axes
    plt.xticks(rotation=0, fontsize=8) #Set an displayed xtick label to fontsize 8

    #For loop to only print out every 10th
    #xlabel so labels don't overlap (1971, 1981, etc)
    tNum = 10
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % tNum != 0:
            label.set_visible(False)
    
    count = 0 #used to only plot out annotation for every two numbers
    for x,y in zip(xlist,ylist):
        if (count == 3):  #print out label everytime count == 3
            label = "{:.2f}".format(y) + "%" #Set label, formatting it to a rate with a '%' character
            plt.annotate(label, # this is the text
                         (x,y), # this is the point to label
                         textcoords="offset points", # how to position the text
                         xytext=(0,10), # distance from text to points (x,y)
                         ha='center') # horizontal alignment can be left, right or center
            count = 0 #set count to 0 if a label was printed
        else:
            count += 1 #add 1 to count

"""
Function name: chart
Function description: To create a chart of historical mortgage rate in the past 30 years
@param none
@return none
"""
def chart():
    Axlist = [] #Stores years as x-axis in list
    Aylist = [] #Stores rates as y-axis in list

    #Opens mortgageRate.txt and reads it
    with open('mortgageRate.txt','r') as txtfile:
        #For loop that reads every line in mortgageRate.txt from bottom to top
        for row in reversed(list(csv.reader(txtfile, delimiter=','))):
            Axlist.append(row[0]) #Add read year
            Aylist.append(float(row[1])) #Add read rate
    
    plt.xlabel('Date in Years') #Set x label to 'Date in years'
    plt.ylabel('Rate %') #Set x label to 'Rate %'
    plt.title('Historical Mortgage Rate') #Set title of chart to 'Historical Mortgage Rate'

    #Plot graph based on xlist and ylist, labelling the line 'Mortgage rate'
    plt.plot(Axlist, Aylist, label = 'Mortgage Rate')
    annotationLabel(Axlist, Aylist) #Call annotationLabel to add labels
    plt.legend() #Place legend on axes
    plt.show() #Show the chart
