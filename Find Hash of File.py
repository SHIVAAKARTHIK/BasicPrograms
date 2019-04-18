import hashlib


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


message = hash_file("C:/Users/karthik.manju/Downloads/48183804_2052320441520706_9071950692796596224_n.png")
print(message)
