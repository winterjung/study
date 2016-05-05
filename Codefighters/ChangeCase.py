'''
1000
Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it would consist either of lowercase letters or of uppercase ones.

At that as little as possible letters should be changed in the word. For example, the word "HoUse" should be replaced with "house", and the word "ViP" with "VIP". If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, "maTRIx" should be replaced by "matrix".

Your task is to implement this function and apply it to the given word.

Example

changeCase("HoUse") = "house";
changeCase("ViP") = "maTRIx";
changeCase("ViP") = "matrix".
[input] string word

A word that consists of lowercase and uppercase letters.
1 ≤ word.length ≤ 100.

[output] string

The given word in which all the letters are either uppercase or lowercase.
'''

def changeCase(word):
    w = word
    c = 0
    for i in w:
        if i.upper() == i:
            c += 1
    return w.upper() if c > len(w)/2 else w.lower()

'''
Solution of Alex_2oo8
'''
changeCase = lambda s: [s.lower, s.upper][sorted(s)[len(s) / 2] < 'a']()
