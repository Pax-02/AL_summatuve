# a function to turn list elements into a string
def list_string(array):
    # an empty string
    str=""
    # a loop to go through the array and add the elements to the string
    for elements in array:
        str+=elements
    return str

# Function to encrypt the message given takes text to encrypt and key being n
def encrypt(text,n):
    # make arrays to help in encryption
    a=[]
    b=[]
    c=[]
    # pointer to help us iterate in the text
    p = 0
    # array pointer to keep us on trak that we don't have rows over the key(n)
    ap = 1
    # a while loop to iterate through the text and add them to the arrays
    while p < len(text):
        # if ap is 1 add the letter to array a or first array
        if ap==1:

            a.append(text[p])
            p+=1
            ap+=1
            # if ap is greater than the key rest it to 1
            if ap > n:
                ap = 1
        # if ap is 2 add the letter to array b
        elif ap==2:
            b.append(text[p])
            p += 1
            ap += 1
            if ap > n:
                ap = 1
        # if ap is 3 add the letter to array c
        elif ap==3:
            c.append(text[p])
            p += 1
            ap += 1
            if ap > n:
                ap = 1
    #  after the loop turn the lists into strings to get the encrypted message
    code=(list_string(a) + list_string(b) + list_string(c))
    # print the encrypted message in text
    print("The coded message in words is: "+str(code))
    b=[a,b,c]
    # print the encrypted message in arrays
    print("encrypted message in arrays:" +str(b))

# a decrypting functin

def decrypt(encry_arrays):
    # variable to capture the decrypted message
    decrypt_message=""
    # variables that contains the length of the arrays in the encrpted message
    a=len(encry_arrays[0])
    b=len(encry_arrays[1])
    c=len(encry_arrays[2])
    # pointers to help us loop through the arrays
    pointer_in_a = 0
    pointer_in_b=0
    pointer_in_c=0
    while pointer_in_a<a:
        decrypt_message+=encry_arrays[0][pointer_in_a]
        pointer_in_a += 1
        if pointer_in_b<b:
            decrypt_message += encry_arrays[1][pointer_in_b]
            pointer_in_b += 1
            if pointer_in_c<c:
                decrypt_message += encry_arrays[1][pointer_in_c]
                pointer_in_b += 1




    print("The encoded message: "+str(encry_arrays)+ " have been decrypted to: "+decrypt_message)



encrypt("plain text",2)

coded_message= [['p', 'a', 'n', 't', 'x'], ['l', 'i', ' ', 'e', 't'], []]


decrypt(coded_message)



