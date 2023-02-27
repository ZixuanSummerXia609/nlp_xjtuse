from distance import Levenshtein_Distance

# 为简化起见，我在这里只举一个例子，来进行wordnet的模拟

words = ["xia", "xiazi", "xzx", "xiazx"]

def match_rate(word1, word2):
    return float(1 - Levenshtein_Distance(word1, word2) / max(len(word1), len(word2)))

if __name__=='__main__':
    t = 'izx'
    dic = {}
    for w in words:
        print("The candidate word is: " + w + ".The match rate is: ", match_rate(w, t))
        dic.update({w: match_rate(w, t)})
    
    most_likely = max(dic, key=lambda k: dic[k])
    print("Are you going to search for the keyword: "+ most_likely)
