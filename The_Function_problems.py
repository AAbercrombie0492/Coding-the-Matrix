# version code 542eddf1f327+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
#def tuple_sum(A, B): return [(A[0][0] + B[0][0], A[0][1] + B[0][1]),(A[1][0] + B[1][0], A[1][1] + B[1][1])]

def tuple_sum(A, B): return[(A[i][j]+ B[i][j]) for i in range(len(A)) for j in range(len(A))]
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples

    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''




## 2: (Problem 2) Inverse Dictionary
def inv_dict(d): return {d.items()[i][1]: d.items()[i][0] for i in range(len(d))}
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
 



## 3: (Problem 3) Nested Comprehension
def row(p, n): return [p + i for i in range(n)]
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    pass

comprehension_with_row = [row(i, 20) for i in range(15)]

comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]

#A = [(1, 2), (10,20)]
#B = [(3,4), (4,20)]

#tuple_sum(A,B)


4: (Problem 4) Probability Exercise 1
domain = {1,2,3,4,5,6}
codomain = {2,3,4,5,6,7}
probabilities = {1 : 0.5, 2: 0.2, 3: 0.1, 4: 0, 5: 0.1, 6:0.1}

Pr_f_is_even = sum([probabilities.get(i) for i in range(2,7,2)])
Pr_f_is_odd  = sum([probabilities.get(i) for i in range(1,6,2)])


5: (Problem 5) Probability Exercise 2
domain = {1,2,3,4,5,6,7}
codomain = {0,1,2}
probabilities = {1 : 0.2, 2: 0.2, 3: 0.2, 4: 0.1, 5: 0.1, 6:0.1, 7:0.1}

Pr_g_is_1    = sum([probabilities.get(i) for i in [1,2,4,7]])
Pr_g_is_0or2 = sum([probabilities.get(i) for i in [3,5,6]])

