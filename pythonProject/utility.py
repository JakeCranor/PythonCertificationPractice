class Shortner:
    def __init__(self, items):
        self.orignal_items = items
    def print_original_items(self):
        print(self.orignal_items)

class ListAndCharShortner(Shortner):
    def prints_shortened_items(self):
        print(self.orignal_items[0:3])

class DictionaryShortner(Shortner):
    def prints_shortened_items(self):
        dict = self.orignal_items
        counter = 0
        result_dict = {}
        for (k, v) in dict.items():
            if (counter < 3):
                result_dict.update({k: v})
                counter += 1
        print(result_dict)

if __name__ == '__main__':
    print("Utility file ran")