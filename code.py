import os

class DictAndBin:
    # time complexity: O(len(chr in dict))
    # varibles: int, float, str
    def __init__(self, i_dict):
        # intilize the dict and bin data, also check if input is a dict or not
        self.dict = None
        self.bin_data = None
        try:
            if isinstance(i_dict, dict):
                self.dict = i_dict
            else:
                raise Exception('Please enter valid input (Dictionary).')
        except:
            raise Exception('Please enter valid input (Dictionary).')
    
    def serialize(self):
        # convert dict into bin data using ord
        try:
            if self.dict != None:
                bin_data = ' '.join(format(ord(letter), 'b') for letter in str(self.dict))
                self.bin_data = bin_data
                return bin_data
            else:
                raise Exception('Your dictionary is not valid.')
        except:
            raise Exception('Can not serialize given input.')
    
    def saveBinFile(self):
        # save bin data into txt file, also create a dir to save file 
        try:
            path = os.path.join("c:/", "DictToBin")
            if not os.path.isdir(path):
                os.mkdir(path)
            
            if self.bin_data != None:
                with open(r'C:/DictToBin/data.txt', 'w') as f:
                    f.write(self.bin_data)
            else:
                raise Exception('Please serialize your dictionary.')

        except Exception:
            raise Exception('Can not write data into file.')

    def readBinFile(self):
        # read bin data txt file using with
        try:
            with open(r'C:/DictToBin/data.txt', 'r') as f:
                self.bin_data = f.readlines()[0]
        except Exception:
            raise Exception('Can not read data from file.')
    
    def getDataType(self, data):
        if data[0] == "\"" or data[0] == "'":
            return str(data[1:-1])
        elif "." in data:
            return float(data)
        else:
            return int(data)

    def deserialize(self):
        #get dict from string text
        if self.bin_data != None:
            try:
                ans = {}
                n_data = ''.join(chr(int(x, 2)) for x in self.bin_data.split())
                print("Time Complexity: O("+ str(len(n_data))+")\n")

                for i in n_data[1:-1].split(","):
                    key, value = i.split(":")
                    ans[self.getDataType(key.strip())] = self.getDataType(value.strip())
                self.dict = ans
            except:
                raise Exception('Can not find deserialize data.')
        else:
            raise Exception('Can not find serialize data.')


p = DictAndBin({1:2, 1.2: 4, "ram": "5", 5:5})
p.serialize()
p.saveBinFile()
p.readBinFile()
p.deserialize()
print(p.dict)

   