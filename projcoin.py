from hashlib import sha256
from datetime import datetime

def sha256_hash(*args):
    str_rep = ""
    for arg in args:
        str_rep += str(arg)
    return sha256(str_rep.encode()).hexdigest()

class Block:
    def __init__(self,
                 time="0000-00-00 00:00:00.000000",
                 prev_hash=None,
                 data=[],
                 validator=None,
                 signature=None):
        self.time = time
        self.prev_hash = prev_hash
        self.data = data
        self.validator = validator
        self.signature = signature

    def __str__(self):
        return f"created at: {self.time}\n"\
              +f"previous hash: {self.prev_hash}\n"\
              +f"current hash: {self.hash_block()}\n"\
              +f"data: {self.data}\n"\
              +f"validator: {self.validator}\n"\
              +f"signature: {self.signature}\n"

    def hash_block(self):
        #return sha256_hash(self.time, self.prev_hash, self.data, self.validator, self.signature)
        return sha256_hash(self.time, self.prev_hash, self.data)



class Blockchain():
    def __init__(self):
        self.chain = [Block()]

    def __str__(self):
        ret_str = ""
        for indx, block in enumerate(self.chain):
            ret_str += f"block number: {indx}\n{block}\n"
        return ret_str[:-1]

    def next_block(self, data):
        time = datetime.now()
        prev_hash = self.chain[-1].hash_block()
        block = Block(time, prev_hash, data)
        self.chain.append(block)
        return block

    def replace_chain(self, new_chain):
        if len(new_chain) > len(self.chain) and\
                self.is_chain_valid(new_chain):
            self.chain = new_chain
            return True
        else:
            return False

    def is_valid(self):
        return self.is_chain_valid(self.chain)

    @staticmethod
    def is_chain_valid(chain):
        if str(chain[0]) != str(Block()):
            return False
        for i in range(1, len(chain)):
            curr_block = chain[i]
            prev_block = chain[i-1]
            if curr_block.prev_hash != prev_block.hash_block():
                return False
        return True

def main():
    pass

if __name__ == "__main__":
    main()