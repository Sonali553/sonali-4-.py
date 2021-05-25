# python program to create a function that returns
the letters in decreasing oder of frequency


# creating a variable

W= input('Please enter a string ')


#creating the function

def most_frequent(string):

    d = dict()

# iterating over a string

    for key in string:

# incrementing the values based on how much times the letter repeated

        if key not in d:

            d[key] = 1

        else:
            d[key] += 1

# Converting it to list of tuples

    d=d.items()

    b=list(d)

#sorting on decreasing frequency of numbers

    return(sorted(b,key=lambda x:(-x[1],x[0])))


print (most_frequent(W))
