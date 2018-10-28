'''
    Compress string by replacing repeating characters with number of reperitions.
    Return the original string if the length of compressed string in this way is longer
'''
import re


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


def compress_re(s):
    '''
        Using regexp to match repeating letters
    '''

    rep_re = re.compile(r'((?P<letter>[a-z])((?P=letter)*))')
    re.findall(rep_re, s)
    compressed_string = ''.join(['{}{}'.format(letter[0][0], len(letter[0])) for letter in re.findall(rep_re, s)])
    if len(compressed_string) < len(s):
        return compressed_string
    return s


if __name__ == '__main__':
    s = 'aabcccccaaa'
    assert compress(s) == 'a2b1c5a3'

    s = 'abcddde'
    assert compress(s) == s
