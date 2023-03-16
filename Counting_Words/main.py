import csv
from collections import Counter


def create_filter():
    with open('filter_words.csv', newline='') as f:
        reader = csv.reader(f)
        return next(reader)

def read_text(file_name, top_N):
    filter_list = create_filter()
    file_data = []
    text_file = open(file_name,"r")

    for word in text_file.read().split():
        if word.lower() not in filter_list:
            file_data.append(word)
            
    file_data_lower = [i.lower() for i in file_data]
 
    counter_words = Counter(file_data_lower).most_common(top_N)
    
    text_file.close()
    
    return counter_words

if __name__ == "__main__":
    counts = read_text('file.txt',10)
    print(counts)
    
