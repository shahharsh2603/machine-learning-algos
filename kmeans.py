import random
import sys
import math

def readfile(filename):
      datapoints = []
      
      with open(filename,'r') as f:
            for line in f.readlines():
                  temp = []
                  temp.append(float(line.strip()))
                  temp.append(0)
                  datapoints.append(temp)
      return datapoints

#returns datapoints in the form of [a,b] where a is value and b is which cluster it belongs to

def average(data):
      return sum(data)/len(data)

def initialize(dataset):
      kmeans =[]
            #If you want to initialize randomly
      """
      for i in [random.randint(0,900) for x in range(3)]:
            kmeans.append(dataset[i][0])
      return kmeans
      """
      tofindsum = []
      for each in dataset:
            tofindsum.append(each[0])
       
      avg = average(tofindsum)
      for i in range(3):
            kmeans.append(avg+i-1)
      return kmeans

      
def distance(x,mean):
      return math.fabs(x-mean)

def assigncluster(dataset,kmeans):
      for each in dataset:
            least_dist = distance(each[0],kmeans[0])
            incluster = kmeans[0]
            for m in kmeans:
                  dist = distance(each[0],m)
                  if dist < least_dist:
                        least_dist = dist
                        incluster = m
            each[1] = incluster
      return dataset
#-----------------------------------------------------------------------------
def run(filename):
      dataset = readfile(filename)
      kmeans = initialize(dataset)
      print "Initialization : "

      for i in range(len(kmeans)):
            print "Mean" + str(i) + "=" ,kmeans[i]
      # -------------------------- Assign initial cluster -------------------------

      assigncluster(dataset,kmeans)

      converge = False
      iteration = 0

      # --------------------- Loop for convergence -----------------------------

      while(not converge):
            temp = []
            for i in range(len(kmeans)):
                  temp.append(kmeans[i])
                           
            # ---------------------------------  recalculate means ----------------
            for i in range(len(kmeans)):
                  sum = 0
                  count = 0
                  for each in dataset:
                        if each[1] == kmeans[i]:
                              sum += each[0]
                              count +=1
                  kmeans[i] = sum/count
            print kmeans
            print " ----------- "

            # --------------------------------- check for convergence --------
            convcount = 3
            for i in range(3):
                  if temp[i] - kmeans[i] == 0:
                         convcount -=1
                  if convcount == 0:
                        converge = True
                  else:
                        converge = False

            # ------------------------------- Reassign clusters according to new means ----------
            dataset = assigncluster(dataset,kmeans)
            iteration +=1

      counts = {}
      for each in dataset:
            if each[1] in counts:
                  counts[each[1]] +=1
            else:
                  counts[each[1]] =1

      print "Final value of means and their counts: "
      for i in range(len(kmeans)):
            print "Mean" + str(i) + "=" ,kmeans[i], "count - ", counts[kmeans[i]]
      print "Number of iterations required for convergence: " + str(iteration)

if  __name__== '__main__':
      run(sys.argv[1])
      #run("1dgauss_au12.txt")
