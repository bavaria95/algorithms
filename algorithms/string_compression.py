'''
    Compress string by replacing repeating characters with number of reperitions.
    Return the original string if the length of compressed string in this way is longer
'''

def compress(s):
    counter = []
    prev = None

    for letter in s:
        if letter != prev:
            counter.append({'letter': letter, 'count': 1})
            prev = letter
        else:
            counter[-1]['count'] += 1
    
    compressed_string = ''.join([x['letter']+str(x['count']) for x in counter])
    if len(compressed_string) < len(s):
        return compressed_string
    return s


if __name__ == '__main__':
    s = 'aabcccccaaa'
    assert compress(s) == 'a2b1c5a3'

    s = 'abcddde'
    assert compress(s) == s
