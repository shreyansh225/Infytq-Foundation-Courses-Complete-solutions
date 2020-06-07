'''

Creating a set	-
flight_set={500,520,600,345,520,634,600,500,200,200}	        #Removes the duplicates from the given group of values to create the set.

Eliminating duplicates from a list-
passengers_list=["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
unique_passengers=set(passengers_list)	                  #set function - removes the duplicates from the list and returns a set

Common elements between setA and setB	 -
setA & setB	                                     #Creates a new set which has common elements from setA and setB
Elements that are only in setA-
setA - setB	                                  #Creates a new set which has only unique elements of setA
Merges elements of setA and setB-
setA | setB	                               #Creates a new set which has all the elements of setA and setB
'''
#list of passengers
passengers_list=["George","Annie", "Jack","Annie","Henry", "Helen","Maria","George","Jack","Remo"]

#set function - removes the duplicates from the list and returns a set
unique_passengers=set(passengers_list)
print(unique_passengers)

#creating a set
flight_set={500,520,600,345,520,634,600,500,200,200}
print(flight_set)

flights_at_src = ["AI230","BA944","EM395","AI704","BA944","AI704"]
flights_at_dest = ["SI107","AI034","EM395","AI704","BA802","SI236"]
print(flights_at_src)
print(flights_at_dest)

#Creating list of unique flights at source and destination
uniq_src_flights = set(flights_at_src)
uniq_dest_flights = set(flights_at_dest)
print(uniq_src_flights)
print(uniq_dest_flights)


#setA-setB -> Gives the elements that are only in setA
#List of flights only at source airport
flights_only_at_src = uniq_src_flights-uniq_dest_flights
print(flights_only_at_src)

#setA&setB -> Gives the common elements between setA and setB
#List of flights common to source and destination airports
common_flights=uniq_src_flights&uniq_dest_flights
print(common_flights)

#setA|setB -> merges setA and setB after removing duplicates
#List of all flights at source and destination airports
all_flights=uniq_src_flights|uniq_dest_flights
print(all_flights)

'''
{'George', 'Remo', 'Helen', 'Maria', 'Annie', 'Jack', 'Henry'}
{200, 520, 500, 600, 345, 634}
['AI230', 'BA944', 'EM395', 'AI704', 'BA944', 'AI704']
['SI107', 'AI034', 'EM395', 'AI704', 'BA802', 'SI236']
{'AI230', 'AI704', 'EM395', 'BA944'}
{'SI107', 'BA802', 'AI704', 'AI034', 'SI236', 'EM395'}
{'AI230', 'BA944'}
{'AI704', 'EM395'}
{'SI107', 'BA802', 'AI704', 'AI034', 'SI236', 'AI230', 'EM395', 'BA944'}

'''
