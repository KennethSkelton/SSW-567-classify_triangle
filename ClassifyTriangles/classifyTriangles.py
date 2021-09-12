
#Kenneth Skelton 
#Professor Saremi
#SSW 567
#11 September 2021

#I pledge my honor that I have abided by the Stevens honor system

import unittest
import math

def classify_triangle(a, b, c):

    sides = [a,b,c]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    leg1 = sides[0]
    leg2 = sides[1]

    results = []

    if(leg1+leg2 <= hypotenuse or (leg1<=0 or leg2<=0 or hypotenuse<=0)):
        return str(results)
    if(leg1*leg1 + leg2*leg2 == hypotenuse*hypotenuse):
        results.append("right")

    if(leg1 != leg2 and leg2 != hypotenuse and hypotenuse != leg1):
        results.append("scalene")
    elif(leg1==leg2 and leg2==hypotenuse and hypotenuse==leg1):
        results.append("equilateral")
    else:
        results.append("isosceles")
    return str(results)

def runclassify_triangle(a,b,c):
    print("classify_triangle("+str(a)+", "+str(b)+", "+str(c)+") "+classify_triangle(a,b,c))

class TestTriangles(unittest.TestCase):
    def testSet1(self):    
        #testing all possible non-error responses
        self.assertEqual(classify_triangle(7,8,9), "['scalene']", "7,8,9 is a scalene triangle")
        self.assertEqual(classify_triangle(2,2,3), "['isosceles']", "2,2,3 is an isosceles triangle")
        self.assertEqual(classify_triangle(1,1,1), "['equilateral']", "1,1,1 is an equilateral triangle")
        self.assertEqual(classify_triangle(3,4,5), "['right', 'scalene']", "3,4,5 is a right scalene triangle")

        #testing against bias in parameter order
        self.assertEqual(classify_triangle(9,7,8), "['scalene']", "9,7,8 is a scalene triangle")
        self.assertEqual(classify_triangle(3,2,2), "['isosceles']", "3,2,2 is an isosceles triangle")
        self.assertEqual(classify_triangle(1,1,1), "['equilateral']", "1,1,1 is an equilateral triangle")
        self.assertEqual(classify_triangle(5,3,4), "['right', 'scalene']", "5,3,4 is a right scalene triangle")

        """
        Due to python rounding it is impossible to create 
        an isosceles right traingle because the hypotenuse of
        such a tringle is an irrational number.

        The commented out test case would be for an isosceles right triangle,
        if it were possible

        """

        #self.assertEqual(classify_triangle(1,1,math.sqrt((2))), "['right', 'isosceles']", "1,1,sqrt(2) is a right isosceles triangle")

    def testSet2(self):

        #testing not a triangle
        self.assertEqual(classify_triangle(1,1,10), "[]", "1,1,10 is not a traingle")
        self.assertEqual(classify_triangle(0,1,2), "[]", "0,1,2 is not a triangle")
        self.assertEqual(classify_triangle(-1, 1, 2), "[]", "-1,1,2 is not a triangle")

        #testing against bias in parameter order
        self.assertEqual(classify_triangle(10,1,1), "[]", "10,1,1 is not a traingle")
        self.assertEqual(classify_triangle(2,0,1), "[]", "2,0,1 is not a triangle")
        self.assertEqual(classify_triangle(2, -1, 1), "[]", "2,-1,1 is not a triangle")



if __name__ == '__main__':

    #examples of the running code
    runclassify_triangle(7,8,9)
    runclassify_triangle(2,2,3)
    runclassify_triangle(0,1,2)
    runclassify_triangle(1,1,1)
    runclassify_triangle(3,4,5)

    #tests
    unittest.main(exit=True)
