import math
import sys

def readfile(filename):
      data = []
      with open(filename) as f:
            for line in f:
                  data.append(line.strip().split(','))           
      return data

def cleandata(data):
      d = []
      for each in data:
            single = []
            for every in each:
                  single.append(float(every))
            d.append(single)
      return d

def initialize(dataset):
      length = len(dataset[0])
      weights = [0.1]*length
      #weights = [0.1,0.2,0.3,0.4,0.5]

      for i in range(len(dataset)):
            dataset[i].insert(0,-1) 

      return dataset,weights

def train(dataset,weights):
      iterationcount =0
      epsilon = 0.001
      alpha = 0.001
      avgerror = 1
      
      while(avgerror>epsilon and iterationcount < 10000):
            sumerror = 0.0
            for eachinput in dataset:
                  total = 0.0
                  output = 0.0
                  error = 0.0
                  
                  for i in range(len(eachinput)-1):
                        total += weights[i] * eachinput[i]
                  
                  if total < 0:
                        output = 0
                  else:
                        output = 1
                              
                  error = eachinput[-1] - output
                  sumerror += error
                  
                  if error != 0 :
                        for i in range(len(eachinput)-1):
                              weights[i] += alpha * error * eachinput[i]
                        

            avgerror = math.fabs(sumerror / len(dataset))
            iterationcount +=1
      print "Number of iterations : " + str(iterationcount)
      return weights

def test(dataset,weights):
      count = 0
      for eachinput in dataset:
            total = 0.0
            for i in range(len(eachinput) - 1):
                  total += weights[i]*eachinput[i]

            if total  < 0:
                  output = 0
            else:
                  output = 1

            print "Prediction : Actual = " + str(output) + " : " + str(eachinput[-1]) ,

            if output == eachinput[-1]:
                  print "Correct Prediction"
                  count +=1
            else:
                  print "Incorrect Prediction"

      print  str(count) + " correctly predicted out of " + str(len(dataset))

def run(trainingfile,testfile):
      training_dataset, initialweights = initialize(cleandata(readfile(trainingfile)))

      weights = train(training_dataset,initialweights)
      print "Learned Weights : " + str(weights)

      test_dataset = initialize(cleandata(readfile(testfile)))[0]
      test(test_dataset,weights)

if __name__ =='__main__':
      run(sys.argv[1],sys.argv[2])
