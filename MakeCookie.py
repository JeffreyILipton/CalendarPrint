from manipulations import *

calPerGram_1 = 120.0/30.0  #http://www.generalmills.com/Home/Brands/Baking_Products/Pillsbury/Brand%20Product%20List%20Page.aspx#{153A93A0-D524-4DD5-B114-037EA967CCDF}
calPerGram_2 = 120.0/80.0
densityOfCookie=1#????
calPerMM3_1 = densityOfCookie*calPerGram_1*0.001
calPerMM3_2 = densityOfCookie*calPerGram_2*0.001
volPerLayer = 740 #mm^3 = .74 m
oddLayer1 = "odd-layer-1.xdfl"
oddLayer2 = "odd-layer-2.xdfl"
evenLayer1 = "even-layer-1.xdfl"
evenLayer2 = "even-layer-2.xdfl"
layerheight = .7


def quotient(number,devideBy):
    return (number-number%devideBy)/devideBy


    
def makeCookie(cals):
    calPerLayer_1 = calPerMM3_1*volPerLayer
    calPerLayer_2 = calPerMM3_2*volPerLayer
    
    num1 = quotient(cals,calPerLayer_1)
    remaining_cals = cals-num1*calPerLayer_1
    num2 = quotient(remaining_cals,calPerLayer_2)
    
    root = Element("xdfl")
    fabTree = ElementTree(element = root)
    
    
    oddTree1 = ElementTree(file =oddLayer1)
    oddTree2 = ElementTree(file =oddLayer2)
    evenTree1 = ElementTree(file =evenLayer1);
    evenTree2 = ElementTree(file = evenLayer2)

    matEl1 = getMaterial(oddTree1)
    matEl2 = getMaterial(oddTree2)
    
    cmds = Element("commands")
    palette = Element("palette")
    palette.append(matEl1)
    palette.append(matEl2)
    
    root.append(palette)
    root.append(cmds)

    
    
    numLayers = num1+num2
    
    ratio = floor(quotient(num1,num2))
    remainder = num1%num2
    layers = []
    h=0;
    for i in range(0,num2):  
        h+=1
        z = layerheight*h
        # select odd Even
        # translate path
        
        layers.append(getPaths(oddTree2)
        for j in range(0,ratio):
            h +=1
            z = layerheight*h
            # odd even test
            # translate paths
            layers.append(getPaths(oddTree1))
    for k in range(0,remainder):
        h+=1
        z = layerheight*h
        # odd Even test
        layers.appendpath(getPaths(oddTree1))
        
    
    for layer in layers
        for path in layer
            cmds.append(path)
    
    
    writeTree("test.xdfl",fabTree)
    print calPerLayer_1, calPerLayer_2
    print remaining_cals;
    print num1, num2
    
    
    
    
    
    
if __name__ == '__main__':
    makeCookie(20.0)
    
    