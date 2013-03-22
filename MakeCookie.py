from manipulations import *
from math import floor
import copy

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
clearance=10
speed=30

def odd(number):
    return ((number%2)!=0)

def quotient(number,devideBy):
    return int((number-number%devideBy)/devideBy)

def setPathsZ(paths,z):
    for pathel in paths:
        for pointel in pathel.iter("point"):
            for zEl in pointel.iter("z"):
                zEl.text = "%f"%z
 
 
    return paths
 
def pathZ(pathEl):
    return pathEl.find("point").find("z").text
    
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
    

    
    
    numLayers = num1+num2
    
    ratio = int(quotient(num1,num2))
    remainder = num1%num2
    layers = []
    h=0;
    for i in range(0,num2):  
        h+=1
        paths2=[]
        
        if odd(h):
            paths2 = copy.deepcopy(getPaths(oddTree2))
        else:
            paths2 = copy.deepcopy(getPaths(evenTree2))
            
        # translate path
        z = layerheight*h
        setPathsZ(paths2,z)
        cmds.extend(paths2)
        print h,z,len(list(cmds)), pathZ(cmds[-1])

        for j in range(0,ratio):
            h +=1
            paths1=[]
            if odd(h):
                paths1 = copy.deepcopy(getPaths(oddTree1))
            else:
                paths1 = copy.deepcopy(getPaths(evenTree1))
            z = layerheight*h
            setPathsZ(paths1,z)
            cmds.extend(paths1)
            print h,z,len(list(cmds)), pathZ(cmds[-1])
            
    for k in range(0,remainder):
        h+=1
        paths1=[]
        if odd(h):
            paths1 = copy.deepcopy(getPaths(oddTree1))
        else:
            paths1 = copy.deepcopy(getPaths(evenTree1))
        
        z = layerheight*h
        setPathsZ(paths1,z)
        cmds.extend(paths1)
        print h,z,len(list(cmds)), pathZ(cmds[-1])
        
    
    
    root.append(palette)
    root.append(cmds)

    #fabTree = setClearance(fabTree,clearance,speed)
    #fabTree = dropClearance(fabTree)
    writeTree("test.xdfl",fabTree)
    print calPerLayer_1, calPerLayer_2
    print remaining_cals;
    print num1, num2
    
    
    
    
    
    
if __name__ == '__main__':
    makeCookie(20.0)
    
    