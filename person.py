class Person:
    def __init__(self, name,age,weight,height,gender):
        self.weight = weight #KG
        self.age = age
        self.name = name
        self.height = height #in cm
        self.calConsumed = 0
        self.calExercised = 0
        if "female"==gender.lower():
            self.male= False
        else:
            self.male = True

        self.bmr = self._calcBMR();
        
    def _calcBMR(self):
        s = 0
        if self.male :
            s = 5
        else:
            s=-161
        return 10*self.weight+6.25*self.height-5.0*self.age+s
        
    def printSelf(self):
        print "Name:",self.name, " Age:",self.age, " Weight (kg)",self.weight, " Height (cm)",self.height, " Male?",self.male
        print "BMR:",self.bmr," Eaten:",self.calConsumed," Exercised:",self.calExercised, " Remaining:",self.calRemaining()
    
    def ate(self,cal):
        self.calConsumed+=cal
        
    def exercised(self,cal):
        self.calExercised+=cal
        
    def calRemaining(self):
        return self.calExercised+self.bmr-self.calConsumed
    
     

if __name__ == '__main__':
    jeff = Person("jeff",25,240/2.2,(5*12+10)*2.54,'male')
    
    jeff.ate(2000.0)
    
    jeff.exercised(100.0)
    
    print jeff.calRemaining()
    
    jeff.printSelf()
    