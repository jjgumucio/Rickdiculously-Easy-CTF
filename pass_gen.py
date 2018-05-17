def password_generator():
    uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    band_words = ['the', 'flesh', 'curtains', 'The', 'Flesh', 'Curtains']

    with open('passwords.txt', 'w') as passwords:
        for c in uppercase_chars:
            for d in range(10):
                for w in band_words:
                    passwords.write(c + str(d) + w + '\n')

password_generator()
