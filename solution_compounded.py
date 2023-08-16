import time

def is_compounded(word, word_set):
    if word in word_set:
        return True
    
    n = len(word)
    for i in range(1, n):
        prefix = word[:i]
        suffix = word[i:]
        
        if prefix in word_set and is_compounded(suffix, word_set):
            return True
    
    return False

def find_longest_compounded_words(word_list):
    word_set = set(word_list)
    compounded_words = [word for word in word_list if is_compounded(word, word_set)]
    compounded_words.sort(key=lambda x: len(x), reverse=True)
    
    if len(compounded_words) >= 2:
        return compounded_words[0], compounded_words[1]
    elif len(compounded_words) == 1:
        return compounded_words[0], None
    else:
        return None, None

def read_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def main():
    word_list_01 = read_file("input_01.txt")
    word_list_02 = read_file( "input_02.txt")
    start_time = time.time()
    longest_compounded_01, second_longest_compounded_01 = find_longest_compounded_words(word_list_01)
    elapsed_time_01 = time.time() - start_time

    start_time = time.time()
    longest_compounded_02, second_longest_compounded_02 = find_longest_compounded_words(word_list_02)
    elapsed_time_02 = time.time() - start_time

    print(f"Longest compounded Word: {longest_compounded_01}")
    print(f"Second longest compounded Word: {second_longest_compounded_01}")
    print(f"Time taken to process file : {elapsed_time_01:.4f} seconds")	
    print(f"Longest compounded Word: {longest_compounded_02}")
    print(f"Second longest compounded Word: {second_longest_compounded_02}")
    print(f"Time taken to process file : {elapsed_time_02:.4f} seconds")	

if __name__ == "__main__":
    main()