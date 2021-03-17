from datetime import*     #date n time
class bank:
    b_name="SIB"                                                   #static(common for all obj)
    def create_acc(self,acno,cname,phno,bal): #local variable
        self.acno=acno
        self.cname=cname
        self.phno=phno
        self.bal=bal      #instance variable
    def deposite(self,amount):
        self.bal+=amount
        print(bank.b_name,self.acno,"credited with",amount,"on",datetime.today(),"your available bal",self.bal)
    def withdrow(self,amount):
        if amount>self.bal:
            print("transaction failed")
        else:
            self.bal-=amount
            print(self.acno,"debited with",amount,"your available bal",self.bal)

    def balance_enq(self):
        print("available bal",self.bal)
obj=bank()
obj.create_acc(100015,"rohit",7656889754,30000)
obj.deposite(20000)

#class
#object

