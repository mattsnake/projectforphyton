#MATT ANDREW SOLATAN
#CPE PETITION
#STRUCTURES

letters = ['M','A','T','T','A','T','T','M',
                'Y','M','A','T','A','Y','A','M',
                'T','A','M','Y','M','T','A',
                'T','M','A','Y','M','Y','A','T',
                'A','M','Y','A','M','A','T']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)
