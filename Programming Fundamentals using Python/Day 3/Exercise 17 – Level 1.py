#PF-Tryout
count=0
i=1
for baggage_weight in 29, 30, 31, 32, 28:
    if(baggage_weight>=1 and baggage_weight <=30):
        print("Passenger",i,": Proceed for baggage check.")
        count+=1
    else:
        print("Passenger",i,": Maximum baggage weight allowed is 30kg.")
    i+=1

print("No. of passengers who cleared baggage check:", count)
