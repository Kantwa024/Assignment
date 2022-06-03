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
    
    def getType(self, data):
        if isinstance(data, int):
            return 0
        elif isinstance(data, float):
            return 1
        elif isinstance(data, str):
            return 2
        else:
            return None

    def serialize(self):
        # convert dict into bin data using ord
        # how i am saving data
        # key -> Type Value -> 0 100111 here 0 is int type and 100111 is variable bin data
        # Same for value
        try:
            if self.dict != None:
                bin_data = ""
                for key, value in self.dict. items():
                    t_key, t_value = self.getType(key), self.getType(value)
                    if t_key != None and t_value != None:
                        bin_data += str(t_key)+" "+' '.join(format(ord(letter), 'b') for letter in str(key))+"\n"
                        bin_data += str(t_value)+" "+' '.join(format(ord(letter), 'b') for letter in str(value))+"\n"
                self.bin_data = bin_data.strip()
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
                self.bin_data = f.readlines()
        except Exception:
            raise Exception('Can not read data from file.')

    def getDataFromType(self, data):
        m_data = data.strip().split()
        type = int(m_data[0])
        r_data = ''.join(chr(int(x, 2)) for x in m_data[1:])
        if type == 0:
            return int(r_data)
        elif type == 1:
            return float(r_data)
        elif type == 2:
            return str(r_data)
        else:
            None

    def deserialize(self):
        #get dict from string text
        if self.bin_data != None:
            try:
                ans = {}
                for i in range(0,len(self.bin_data), 2):
                    key, value = self.getDataFromType(self.bin_data[i]), self.getDataFromType(self.bin_data[i+1])
                    ans[key] = value
                self.dict = ans
            except:
                raise Exception('Can not find deserialize data.')
        else:
            raise Exception('Can not find serialize data.')


p = DictAndBin({1:2, 1.2: 4, "ram": "ram is a good  boy, and he is: 13", 5:5})
p.serialize()
p.saveBinFile()
p.readBinFile()
p.deserialize()
print(p.dict)

   