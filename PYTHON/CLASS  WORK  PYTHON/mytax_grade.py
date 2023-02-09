def yourtaxSlab(taxable_income):
    if(taxable_income>=10):
        tax=taxable_income*0.3
    else:
        if(taxable_income<10 and taxable_income>=5):
            tax=taxable_income*0.2
        else:
            if(taxable_income<5and txable_income>=2.5):
                tax=taxable_income*0.05
            else:
                tax=0
    return tax
        
def printgrade (score):
    if score <0  or score > 100:
        print("invalid score")
    if score >=90.0:
        print("A")
    elif score >=80.0:
        print("B")
    elif score >=70.0:
        print("C")
    elif score>=60.0:
        print("D")
    else:
        print('F')
        
# printgrade(90)
# printgrade(77)
# printgrade(80)
# printgrade(102)
printgrade(-100)
