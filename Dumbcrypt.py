########################################################################################################################
#   Computer Project #4
#
#   print_banner --> print welcome message with the right formatting.
#   multiplicative_inverse --> finds and returns A_inverse.
#   check_co_prime --> check if two parameters are co-prime numbers.
#   get_smallest_co_prime --> Calculates the smallest co-prime of M(parameter).
#   caesar_cipher_encryption --> Encrypts given punctuation.
#   caesar_cipher_decryption --> Decrypts given punctuation.
#   affine_cipher_encryption --> Encrypts given letters or numbers.
#   affine_cipher_decryption --> Decrypts given letters or numbers.
#
#   main --> Prompts user for needed data to run program, then executes the needed task through all functions above.
#
########################################################################################################################
import math, string

# Define constants for punctuation and alphanumeric characters
# string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
# except space is not included in this string
PUNCTUATION = string.punctuation

# string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
# string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits


# Welcome message
BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy!
    We're combining Affine Cipher with Caesar Cipher to create a code
    so 'dumb,' it's brilliant.
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat!
    Let's dive into this cryptographic comedy adventure! *
    '''

def print_banner(message):
    '''
    Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.
    '''
    border = '*' * 50
    print(border)
    print(f'* {message}')
    print(border)
    print()

def multiplicative_inverse(A, M):
    '''
    Return the multiplicative inverse for A given M.
    Find it by trying possibilities until one is found.
    Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
    Returns:
        int: The multiplicative inverse of A modulo M.
    '''
    for A_inverse in range(M):
        if (A * A_inverse) % M == 1:
            return A_inverse


def check_co_prime(num, M):
    '''
    Checks if both parameter's greatest common denominator is 1 (if they are co-prime) using the math module.
    Returns: True if GCD is equal to 1, False if not.
    '''
    GCD = math.gcd(num, M)
    if GCD==1:
        return True
    else:
        return False


def get_smallest_co_prime(M):
    '''
    Calculates the smallest co-prime of M.
    For loop using every value of A(multiplicative) in the range 2 to M-1.
    Function check_co_prime to check if A and M are co-prime.
    If check_co_prime is true, then return A(multiplicative)
    '''
    for A in range(2,M):
        x = check_co_prime(A,M)
        if x:
            return A


def caesar_cipher_encryption(ch, N, alphabet):
    '''
    Will encrypt punctuation.
    Parameters(character, rotation, alphabet)
    First, transform alphabet into lower case.
    Assign M to the length of the alphabet being used.
    initialize variable i(index), then use loop to check the index for the given punctuation in given alphabet(x).
    Calculate E(encrypted index).
    Find the punctuation with index E in the encrypted alphabet.
    Return encrypted punctuation.
    '''
    alphabet = alphabet.lower()
    M = len(alphabet)
    i = 0

    for letter in alphabet:
        if letter == ch:
            x=i
        i += 1

    E = (x+N)%M
    encrypt_cc_ch = alphabet[E]
    return encrypt_cc_ch


def caesar_cipher_decryption(ch, N, alphabet):
    '''
    Will decrypt punctuation.
    Parameters(character, rotation, alphabet)
    First, transform alphabet into lower case.
    Assign M to the length of the alphabet being used.
    initialize variable i(index), then use loop to check the index for the given punctuation in given alphabet(x).
    Calculate D(decrypted index).
    Find the punctuation with index D in the decrypted alphabet.
    Return decrypted punctuation.
    '''
    alphabet = alphabet.lower()
    M = len(alphabet)
    i = 0

    for letter in alphabet:
        if letter == ch:
            x = i
        i += 1

    D = (x - N) % M
    decrypt_cc_ch = alphabet[D]
    return decrypt_cc_ch


def affine_cipher_encryption(ch, N, alphabet):
    '''
    Will encrypt letters and numbers(lower case only).
    Parameters(character, rotation, alphabet)
    First, transform alphabet into lower case.
    Assign M to the length of the alphabet being used.
    Find A(multiplicative) through the get_smallest_co_prime function with parameter M(length of alphabet)
    initialize variable i(index), then use loop to check the index for the given character in given alphabet(x).
    Calculate E(encrypted index).
    Find the character with index E in the encrypted alphabet.
    Return encrypted letter or number.
    '''
    alphabet = alphabet.lower()
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    i = 0

    for letter in alphabet:
        if letter == ch:
            x = i
        i += 1

    E = (A*x+N)%M
    encrypt_ac_ch = alphabet[E]
    return encrypt_ac_ch #done


def affine_cipher_decryption(ch, N, alphabet):
    '''
    Will decrypt letters and numbers(lower case only).
    Parameters(character, rotation, alphabet)
    First, transform alphabet into lower case.
    Assign M to the length of the alphabet being used.
    Find A(multiplicative) through the get_smallest_co_prime function with parameter M(length of alphabet).
    Using A find the A_inverse through the multiplicative_inverse(A,M) function.
    initialize variable i(index), then use loop to check the index for the given character in given alphabet(x).
    Calculate D(decrypted index).
    Find the character with index D in the decrypted alphabet.
    Return decrypted letter or number.
    '''
    alphabet = alphabet.lower()
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    A_inverse = multiplicative_inverse(A, M)

    i = 0
    for letter in alphabet:
        if letter == ch:
            x = i
        i += 1

    D = A_inverse*(x-N)%M
    decrypt_ac_ch = alphabet[D]
    return decrypt_ac_ch


def main():
    '''
    Print welcome message with print_banner(BANNER)
    Gets input for N(rotation) and verifies if it is an integer, if not error message displayed.
    If user inputs e, encryption of desired string will be done, if no spaces are found in string.
    If user inputs d, decryption of desired string will be done, if no spaces are found in string.
    If user inputs q, program will stop running.
    If user input is any other letter other than e, d, and q, then error message displayed and prompt for new action.
    '''
    print_banner(BANNER)

    action ="".lower()  # What function of the program will the user wish to use.

    space_count = 0  # Number of spaces found in string given by user.

    N=""  # Initialize rotation variable

    # Will make sure that input is an integer.
    while type(N) != int:
        try:
            N = int(input("Input a rotation (int): "))
        except:
            print("\nError; rotation must be an integer.")

    # If action == "q" program will stop running.
    while action != "q":
        action = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")

        # Will encrypt string.
        if action == "e":
            in_string = input("\nInput a string to encrypt: ")
            encrypted_string = ""  # Initializes final encrypted string

            for ch in in_string.lower():

                if ch in ALPHA_NUM:
                    e_ch = affine_cipher_encryption(ch,N,ALPHA_NUM)  # Encrypted letter or number
                    encrypted_string += e_ch  # Add new letter or number to the encrypted string

                elif ch in PUNCTUATION:
                    e_pun = caesar_cipher_encryption(ch,N,PUNCTUATION)  # Encrypted punctuation
                    encrypted_string +=e_pun  # Add new punctuation to the encrypted string.

                else:
                    print("\nError with character:")
                    print("Cannot encrypt this string.")
                    space_count += 1

            if space_count == 0:  # If no space was found in string initial and result string will be printed.
                print("\nPlain text:", in_string)
                print("\nCipher text:",encrypted_string)

        # Will decrypt string.
        elif action == "d":
            in_string = input("\nInput a string to decrypt: ")
            decrypted_string = ""  # Initializes final decrypted string

            for ch in in_string.lower():

                if ch in ALPHA_NUM:
                    d_ch = affine_cipher_decryption(ch, N, ALPHA_NUM)  # Decrypted letter or number
                    decrypted_string += d_ch  # Add new letter or number to the decrypted string.

                elif ch in PUNCTUATION:
                    d_pun = caesar_cipher_decryption(ch, N, PUNCTUATION)  # Decrypted punctuation
                    decrypted_string += d_pun  # Add the new punctuation to the decrypted string

                else:
                    print("\nError with character:")
                    print("Cannot decrypt this string.")
                    space_count += 1

            if space_count == 0:  # If no space was found in string initial and result string will be printed.
                print("\nCipher text:", in_string)
                print("\nPlain text:", decrypted_string)

        # If action is any letters not including "e","d",and "q", error message will be displayed.
        elif action != "q":
            print("\nCommand not recognized.")

# These two lines allow this program to be imported into other codes such as our function
# tests code allowing other functions to be run and tested without 'main' running.
# However, when this program is run alone, 'main' will execute.
if __name__ == '__main__':
    main()
