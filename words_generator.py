

# Generate all the possible permutation of the list of letters considering the number of letter specified in the number parameter
def generate(letters, number, selected, result):
    for index, _ in enumerate(letters):
        if index not in selected:

            l = letters.copy()
            s = selected.copy()
            n = number - 1

            s.append(index)

            if(n == 0):
                t = []
                for i in s:
                    t.append(letters[i])
                
                result.append("".join(t))
            else:
                generate(l, n, s, result)
           
    return result

def is_valid_portuguese_word(word):
    url = f'https://api.datamuse.com/words?sp={word}&max=1'
    response = requests.get(url)
    data = response.json()
    return len(data) > 0


def load_word_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = set(line.strip().lower() for line in file)
    return words

#il = list(input("Characters: "))
#numb = int(input("Word size: "))
il = list("ratied")
numb = 4
#letters = ['a', 'r', 'c', 'i', 'o']
letters = il
request_list = []
words = load_word_list("portuguese.txt")

l = generate(letters, numb, [], [])
for it in l: 
    if it not in request_list:
        test_word = it
        if test_word in words and test_word[0] == 't':
            print(test_word)
        
        request_list.append(it)

