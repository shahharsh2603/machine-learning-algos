import math
import sys

def maximum(alist):
      maximum = alist[0]
      for each in alist:
            if each > maximum:
                  maximum = each
      return maximum

def minimum(alist):
      minimum = alist[0]
      for each in alist:
            if each < maximum:
                  minimum = each
      return minimum

def mean(alist):
      total=0
      for each in alist:
            total += (each)
      mean = total/(len(alist))
      return mean

def stddev(alist):
      avg = mean(alist)
      variance = 0
      for each in alist:
            variance += (avg - each)**2
      variance /= len(alist)
      stddev = variance ** 0.5
      return stddev

def  readfile(filename):
      f = open(filename,'r')
      data = f.read()
      return data

def getdata(filename):
      afile = readfile(filename)
      words = afile.split();
      price = []
      sq_foot = []
      i = 0
      for x in range(0,len(words)):
            if i%2==0:
                  price.append(float(words[i]))
            else:
                  sq_foot.append(float(words[i]))
            i +=1
      d = {}
      j=0
      for each in sq_foot:
            d[each] = price[j]
            j+=1

      MeanP = mean(price)
      MeanS = mean(sq_foot)
      
      normalizedPrice = []
      normalizedSQ = []

      #to normalize

      for each in price:
            normalizedPrice.append(each/MeanP)
      for each in sq_foot:
            normalizedSQ.append(each/MeanS)
      
      dic = {}
      dic['price'] = price
      dic['squarefoot'] = sq_foot
      dic['price_keyvalues'] = [maximum(price),minimum(price),mean(price),stddev(price)]
      dic['squarefoot_keyvalues'] = [maximum(sq_foot),minimum(sq_foot),mean(sq_foot),stddev(sq_foot)]
      dic['nprice'] = normalizedPrice
      dic['nsq'] = normalizedSQ

      return dic

def linearRegressionAnalytical(pricelist,arealist):
      n = len(pricelist)
      sumPrice = sum(pricelist)
      sumArea = sum(arealist)
      termNum1 = n* sumOfProducts(pricelist,arealist)
      termNum2 = sumPrice * sumArea
      termDenom1 = n*sumOfSquares(arealist)
      termDenom2 = sumArea**2
      w1 = (termNum1 - termNum2)/(termDenom1 - termDenom2)
      w0 = (sumPrice - (w1*sumArea))/n
      
      return w0,w1

def sumOfProducts(list1,list2):
      answer =0
      for x in range(0,len(list1)):
            answer += (list1[x]*list2[x])
      return answer

def sumOfSquares(alist):
      answer = 0
      for each in alist:
            answer += each**2
      return answer

def batchGradientDescent(passedw0,passedw1,pricelist,arealist):
      alpha = 0.001
      oldw0 = passedw0
      oldw1 = passedw1
      count = 0
      e = 0.0000000001 #Epsilon Value
      
      while True:
            termforw0 = 0.0
            termforw1 = 0.0
            
            for x in range(0,len(arealist)):
                  function = (oldw1*arealist[x]) + oldw0
                  termforw0 += pricelist[x] - function
                  termforw1 += (pricelist[x] - function)*arealist[x]

            w0 = oldw0 + (alpha*termforw0)
            w1 = oldw1 + (alpha*termforw1)
            count+=1

            diffw0 = math.fabs(w0 - oldw0)
            diffw1 = math.fabs(w1-oldw1)
            
            print "w1 : %.4f, w0 : %.4f, diffw1 : %.6f, diffw0: %.6f, iteration : %d" % \
                  (w1,w0,diffw1,diffw0,count)       

            if (diffw0 <= e and diffw1 <=e):
                  return w0,w1,count
            
            oldw0 = w0
            oldw1 = w1

# Method for quadratic Gradient Descent


def quadraticGradientDescent(passedw0,passedw1,passedw2,pricelist,arealist):
      alpha = 0.0002
      oldw0 = passedw0
      oldw1 = passedw1
      oldw2 = passedw2
      count = 0
      e = 0.0001 #Epsilon Value
      
      while True:
            termforw0 = 0.0
            termforw1 = 0.0
            termforw2 = 0.0
            
            for x in range(0,len(arealist)):
                  function = (oldw1*arealist[x]) + oldw0
                  termforw0 += pricelist[x] - function
                  termforw1 += (pricelist[x] - function)*arealist[x]
                  termforw2 += (pricelist[x] - function)*(arealist[x]**2)

            w0 = oldw0 + (alpha*termforw0)
            w1 = oldw1 + (alpha*termforw1)
            w2 = oldw2 + (alpha*termforw2)
            count+=1

            diffw0 = math.fabs(w0 - oldw0)
            diffw1 = math.fabs(w1-oldw1)
            diffw2 = math.fabs(w2-oldw2)
            
            print "w1 : %.4f, w0 : %.4f, diffw2 : %.6f, diffw1 : %.6f, diffw0: %.6f, iteration : %d" % \
                  (w1,w0,diffw2,diffw1,diffw0,count)       

            if (diffw0 <= e and diffw1 <=e and diffw2 <= e):
                  return w0,w1,w2,count
            
            oldw0 = w0
            oldw1 = w1
            oldw2 = w2


# Method for stochastic gradient descent


"""
def stochaisticGradientDescent(passedw0,passedw1,pricelist,arealist):
      alpha = 0.1
      oldw0 = passedw0
      oldw1 = passedw1
      count =0
      m = len(arealist)
      e = 0.00000000001

      while True:
            for x in range(0,m):
                  func = (oldw1*arealist[x]) + oldw0
                  w0 = oldw0 + (alpha*(pricelist[x]-func))
                  w1 = oldw1 + (alpha*((pricelist[x]-func)*arealist[x]))
                  count+=1

            diffw0 = math.fabs(w0 - oldw0)
            diffw1 = math.fabs(w1-oldw1)
                  
            print "w1 : %.4f, w0 : %.4f, diffw1 : %.6f, diffw0: %.6f, iteration : %d" % \
                  (w1,w0,diffw1,diffw0,count)
                        
            if (diffw0 <= e and diffw1 <=e):
                  return w0,w1,count
                  
            oldw0 = w0
            oldw1 = w1
      
"""

def run(filename):
      dictionary = getdata(filename)
      
      coeffs = linearRegressionAnalytical(dictionary['nprice'],dictionary['nsq'])
      coeffsGD = batchGradientDescent(coeffs[0]+100,coeffs[1]+100,dictionary['nprice'],dictionary['nsq'])
      coeffsQGD = quadraticGradientDescent(1000,1000,1000,dictionary['nprice'],dictionary['nsq'])
      #coeffsSGD = stochaisticGradientDescent(coeffs[0]+10,coeffs[1]+10,dictionary['nprice'],dictionary['nsq'])
       

      rescalew0 = dictionary['price_keyvalues'][2]
      rescalew1 = dictionary['price_keyvalues'][2]/dictionary['squarefoot_keyvalues'][2]
      rescalew2 = dictionary['price_keyvalues'][2]/(dictionary['squarefoot_keyvalues'][2]**2)


      print "\n\n"
      print " Values of Max, Min,Mean and Standard Deviation are respectively: \n"
      print "Price : " + str(dictionary['price_keyvalues'])
      print "Square footage : " + str(dictionary['squarefoot_keyvalues'])
      print "\n"
      print "Values obtained by Analytical Linear Regression: w0 = %f , w1 = %f" % (coeffs[0]*rescalew0,coeffs[1]*rescalew1)
      print "Values obtained by Batch Gradient Descent in %d iterations: w0 = %f , w1 = %f" % (coeffsGD[2],coeffsGD[0]*rescalew0,coeffsGD[1]*rescalew1)
      #print "Values obtained by Stochaistic Gradient Descent in %d iterations: w0 = %f , w1 = %f" % (coeffsSGD[2],coeffsSGD[0]*rescalew0,coeffsSGD[1]*rescalew1)
      print "Values obtained by Quadratic Gradient Descent in %d iterations: w0 = %f , w1 = %f, w2 = %f" % (coeffsQGD[3],coeffsQGD[0]*rescalew0,coeffsQGD[1]*rescalew1,coeffsQGD[2]*rescalew2)

if __name__ =='__main__':
      run(sys.argv[1])
