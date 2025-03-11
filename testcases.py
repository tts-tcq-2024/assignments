def get_soundex_code(c):
    chararr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codearr = '01230120022455012623010202'
    c = c.upper()

    if c in chararr:
        return codearr[chararr.index(c)]
    return '0'

def check_code(code, soundex, s_index):
    if code != '0' and code != soundex[s_index - 1]:
        return code
    return None

def update_soundex(s_index, soundex):
    while s_index < 4:
        soundex += '0'
        s_index += 1
    return soundex

def generate_soundex(name):
    soundex = name[0].upper()
    s_index = 1

    for i in range(1, len(name)):
        code = get_soundex_code(name[i])
        if s_index < 4 and check_code(code, soundex, s_index):
            soundex += code
            s_index += 1

    soundex = update_soundex(s_index, soundex)
    return soundex

# Sample tests
def test_soundex():
    assert generate_soundex("X1") == "X000"
    assert generate_soundex("KUMTA") == "K530"
    assert generate_soundex("ABCDE") == "A123"
    assert generate_soundex("1234") == "1000"

def main():
    soundex = generate_soundex("THUB")
    print(soundex)  #Output should be T100

if __name__ == "__main__":
    main()
    test_soundex()
    print("All tests passed!")
