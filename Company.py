import hashlib
# import block as Block
import random

# Num_Upload = 0
# Month = 0
# Token = 0
class Company(object):
    def __init__(self, Seq_company, Num_Upload = 0):
        self.Seq_company = Seq_company
        self.Num_Upload = Num_Upload


    def PrepareData(self):
        rad = random.randint(0,9)
        if rad <=7:
            print('Upload')
            Data = random.randint(0,100)
            DataHash = hashlib.sha256(str(Data).encode('utf-8')).hexdigest()
            self.Num_Upload = self.Num_Upload + 1
        else:
            print('None')
            DataHash = 0
        print(DataHash)
        print(self.Num_Upload)
        return DataHash
        # pass

    # def GetToken(Num_Upload, Month, Token):
    #     if Num_Upload < Month:
    #         Token = Token - 0.5
    #     elif Num_Upload == Month:
    #         Token = Token + 1
    #     elif Num_Upload > Month:
    #         print('Error')
    #     return Token
    #
    # def IssueBonds(DataHash):
    #     Bonds = None
    #     if Token >= 5:
    #         Bonds= hashlib.sha256(str(DataHash).encode('utf-8')).hexdigest()
    #     else:
    #         pass
    #     return Bonds



if __name__ == '__main__':
    comp1 = Company(0, 1)
    comp2 = Company(0, 2)
    comp3 = Company(0, 3)
    comp4 = Company(0, 4)
    print(comp1.Num_Upload)
