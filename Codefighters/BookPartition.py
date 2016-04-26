'''
Author
chienthan
2000
In addition to learning magic, Harry Potter also has to learn Math, Physics and Chemistry, the subjects that will surely help his to become a legendary magician.

One day, Harry obtained a huge number of books, each book about one of these subjects. Harry wants to divide them into groups of 3, so that each groups contains either books of the same subject, or of three different subjects.

Let's help Harry find the maximum number of groups he can create. Note that Harry doesn't have to use all of the books since there're so many of them.

Example

For m = 7, p = 8 and c = 9, the output should be
BookPartition(m, p, c) = 7.
One of the possible partition is 6 groups of books of different subjects and 1 group of books on Chemistry.
For m = 1, p = 3 and c = 3, the output should be
BookPartition(m, p, c) = 2.
It's possible to create two groups of books on Physics and Chemistry.
[input] integer m

The number of Mathematics books, 0 ≤ m ≤ 10^9.

[input] integer p

The number of Physics books, 0 ≤ p ≤ 10^9.

[input] integer c

The number of Chemistry books, 0 ≤ c ≤ 10^9.

[output] integer

The maximum number of groups. It is guaranteed that the answer won't have more than 9 digits in it.
'''

def BookPartition(m, p, c):
    sum1 = m//3 + p//3 + c//3
    array = [m, p, c]
    array.sort()
    array2 = array[::]

    sum2 = array[0]
    array[1] -= array[0]
    array[2] -= array[0]
    sum2 += array[1]//3
    sum2 += array[2]//3

    sum3 = array2[0]-1
    array2[1] -= sum3
    array2[2] -= sum3
    sum3 += array2[1]//3
    sum3 += array2[2]//3

    return max(sum1, sum2, sum3)
