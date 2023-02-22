# Name: Ariadna Gonzalez

class Card:
    #"""class representing a simple Neapolitan card. Holds a 
    #value and a suit"""

    def __init__(self,intvalue,suitgiven):
        self.intvalue = intvalue
        self.suitgiven = str(suitgiven)

    def __repr__(self):
        return f"Vector2d({self.intvalue},{self.suitgiven})"
    def __str__(self):
        return f"{self.intvalue} of {self.suitgiven}"
    def __eq__(self,other):
        if self.intvalue == other.intvalue:
            if self.suitgiven == other.suitgiven:
                return True
            else:
                return False
        else:
            return False
hi = Card(2,'hearts')
bye = Card(3,'diamonds')
totallyhi = Card(2,'hearts')