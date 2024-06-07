#import the Person class definition from the Person.py file
from Person import Person

def sortPersonList( personList ):
    """
    sort a list of Person objects
    """

    # you can set this True to turn on debug output
    debug = False
    
    # this many Person objects in the list
    nmax = len( personList )

    # count the number of passes through the loop required to complete the sort
    nPasses = 0

    # will keep looping until the sort is complete
    keep_looping = True
    while keep_looping:

        # update pass counter
        nPasses = nPasses + 1

        # initialize swap counter at the start of each pass through the list
        nSwaps = 0

        # each pass goes through the entire list
        for n in range( 0, nmax-1 ):
            
            if (debug):
                # comparing these personList entries
                print ( "personList[", n, "]", personList[n] )
                print ( "personList[", n+1, "]", personList[n+1] )
            
            # if the next person's name is < this person's name
            if (personList[n+1] < personList[n]): # swap them in the list

                if (debug):
                    print( "swapping", personList[n], "and", personList[n+1] )

                # swap list entries using a temporary Person object
                temp = personList [n+1]
                personList [n+1] = personList [n]
                personList [n] = temp

                # increment the swap counter
                nSwaps = nSwaps + 1

                if (debug):
                    print( nSwaps, "swaps so far on pass", nPasses )
                    # personList after this swap
                    for person in personList:
                        print ("  ", person)
                    print()

        if (debug):
            print( nSwaps, "total swaps on pass", nPasses )
            # personList after this pass
            for person in personList:
                print ("  ", person)
            print()

        # keep looping as long as we made at least one swap on this iteration
        if (nSwaps == 0):
            keep_looping = False
            
        # make sure there is not an infinite loop (this condition should not occur)
        if (nPasses > nmax):
            keep_looping = False

    # return when the sort is complete
    return

def main():
    """
    the main program
    """
    print("Person sort")
    print("")

    # create Person objects
    rick  = Person( "Rick",  "DiPersio" )
    micki = Person( "Micki", "DiPersio" )

    # compare Person objects with < operator
    if (rick < micki):
        print (rick, "precedes", micki, "alphabetically")
    else:
        print (rick, "does not precede", micki, "alphabetically")
    print("")

    # compare Person objects with == operator
    if (rick == micki):
        print (rick, "has the same name as", micki)
    else:
        print (rick, "does not have the same name as", micki)
    print("")

    # create list of Person objects
    personList = []
    personList.append( rick )
    personList.append( micki )
    personList.append( Person( "Donald",  "Trump" ) )
    personList.append( Person( "Hillary", "Clinton" ) )
    personList.append( Person( "Joe",     "Biden" ) )
    personList.append( Person( "James",   "Harden" ) )
    personList.append( Person( "J.J.",    "Watt" ) )
    personList.append( Person( "Jose",    "Altuve" ) )
    
    # print original personlist
    print ("original personList:")
    for person in personList:
        print ("  ", person)
    print()

    # sort personList
    sortPersonList( personList )
    
    # print sorted personlist
    print ("sorted personList:")
    for person in personList:
        print ("  ", person)

    # hold window open to allow user to view output
    print("")
    input("Press ENTER to continue ")
    
# call main()
if __name__ == "__main__":
    main()

