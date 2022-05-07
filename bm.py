from hashlib import sha256
MAX_NONCE = 100000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"BAG SECURED! FREE LOOT TOOK {nonce} TRYS!!!!")
            return new_hash
    return new_hash

    raise BaseException(f"took way to long, im tired, I tried {MAX_NONCE} times :(")

if __name__=='__main__':
    transactions='''
    Dylan->Dean->20,
    Mom->Dad->45
    '''
    difficulty = 8
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, '0000000xb5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty)
    total_time = str(time.time() - start)
    print("Timer: " + total_time + " seconds")
    print(new_hash)