#!/usr/bin/python3
'''
Minimum Operations coding interview
'''

def minOperations(n):
    '''
    function that computes the fewest number of ops
    to result in exactly n H characters.
    
    Args:
    n (int): The desired number of H characters.
    Returns:
    int: The fewest number of ops needed
    '''
    if not isinstance(n, int):
        return 0
    #set op_count => `operations_count` to 0
    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        #if clipboard is empty, copy all and paste
        if clipboard == 0:
            clipboard = done
            done += clipboard #Increment done by clipboard size
            ops_count += 2 #Increment operations count by 2 (copy and paste)
        #If (n - done) is divisible by done, copy all and paste
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard # Increment done by clipboard size
            ops_count += 2 # Increment operations count by 2 (copy and paste)
        #If clipboard has content, paste
        elif clipboard > 0:
            done += clipboard #Increment done by clipboard size
            ops_count += 1 # Increment operations count by 1(paste)
    return ops_count

