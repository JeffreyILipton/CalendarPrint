
calPerGram_1 = 120.0/30.0  #http://www.generalmills.com/Home/Brands/Baking_Products/Pillsbury/Brand%20Product%20List%20Page.aspx#{153A93A0-D524-4DD5-B114-037EA967CCDF}
calPerGram_2 = 120.0/80.0
densityOfCookie=1#????
calPerMM3_1 = densityOfCookie*calPerGram_1*0.001
calPerMM3_2 = densityOfCookie*calPerGram_2*0.001

volPerLayer = 740 #mm^3 = .74 ml

def quotient(number,devideBy):
    return (number-number%devideBy)/devideBy

def makeCookie(cals):
    calPerLayer_1 = calPerMM3_1*volPerLayer
    calPerLayer_2 = calPerMM3_2*volPerLayer
    
    num1 = quotient(cals,calPerLayer_1)
    remaining_cals = cals-num1*calPerLayer_1
    num2 = quotient(remaining_cals,calPerLayer_2)
    
    print calPerLayer_1, calPerLayer_2
    print remaining_cals;
    print num1, num2
    
if __name__ == '__main__':
    makeCookie(20.0)
    
    