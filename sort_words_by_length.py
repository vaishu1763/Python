def sort_words_length():
    sentence=input("Enter a sentence: ")
    words=[]
    current_word=''
    for char in sentence:
        if char==' ':
            if current_word:
                words.append(current_word)
                current_word=''
        else:
            current_word+=char
    if current_word:
        words.append(current_word)
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if len(words[i])<len(words[j]):
                words[i],words[j]=words[j],words[i]
    for word in words:
        print(word+ ":" ,len(word))
sort_words_length()
