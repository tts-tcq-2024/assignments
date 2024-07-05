### Switch Case Refactored

```CS
private static readonly string[] SoundexMapping = {
    "01230120022455012623010202", // A-M
    "00000000000000000000000000"  // N-Z
  };

 private static char GetSoundexCode(char c)
  {
    c = char.ToUpper(c);
    int index = c - 'A';
    if (index < 0 || index >= SoundexMapping.Length * SoundexMapping[0].Length)
    {
      return '0';
    }

    return SoundexMapping[index / 13][index % 13];
  }

```

```c
char BFPV(char c){
    if(c=='B' || c=='F' || c=='P' || c=='V'){
        return '1';
    }
    return CGKKQSXZ(c);
}

char CGKKQSXZ(char c){
    if(c=='C' || c=='G' || c=='J' || c=='K' || c=='Q' || c=='S' || c=='X' || c=='Z'){
        return '2';
    }
    return  DT(c);
}

char DT(char c){
    if(c=='D' || c=='T'){
        return '3';
    }
    return L(c);
}


char L(char c){
    if(c=='L'){
        return'4';
    }
   return MN(c);
}


char MN(char c){
    if(c=='N' || c=='M'){
        return '5';
    }
    return R(c);
}


char R(char c){
    if(c=='R'){
        return '6';
    }
    return '0';
}


char getSoundexCode(char c) {
    c = toupper(c);
    return BFPV(c);
    
```
### Good Separation
```cs
 public static string GenerateSoundex(string name)
    {
        if (string.IsNullOrEmpty(name))
        {
            return string.Empty;
        }

        StringBuilder soundex = new StringBuilder();
        SoundexAppend(soundex, name[0]);
        GetSoundexProcess(soundex, name);

        checkingsoundex(soundex);

        return soundex.ToString();
    }

```
### Value Based Testing (Repeated)

```csharp
 [Fact]
    public void HandlesEmptyString()
    {
        Assert.Equal(string.Empty, Soundex.GenerateSoundex(""));
    }

    [Fact]
    public void HandlesSingleCharacter()
    {
        Assert.Equal("A000", Soundex.GenerateSoundex("A"));
    }

    [Fact]
    public void HandlesMultipleConsonantsAndVowels()
    {
        Assert.Equal("R163", Soundex.GenerateSoundex("Robert"));
    }
    
 
    [Fact]
    public void HandlesSpecialCharacters()
    {
        Assert.Equal("J530", Soundex.GenerateSoundex("John-Doe"));
    }


    [Fact]
    public void HandlesWithlowercaseCharacters()
    {
        Assert.Equal("A420", Soundex.GenerateSoundex("alice"));
    }

    [Fact]
    public void HandlesWithExactly_4_Characters()
    {
        Assert.Equal("A350", Soundex.GenerateSoundex("Adam"));
    }

    [Fact]
    public void HandlesWithMoreThan_4_Characters()
    {
        Assert.Equal("C623", Soundex.GenerateSoundex("Christopher"));
    }

    [Fact]
    public void HandlesLongString()
    {
        Assert.Equal("A123", Soundex.GenerateSoundex("abcdefghijklmnopqrstuvwxyz"));
    }
    
     [Fact]
    public void HandlesBothCharAndDigit()
    {
        Assert.Equal("J500", Soundex.GenerateSoundex("Jane123"));
    }   
```
### New Grammer but retains complexity

```csharp
public static char GetSoundexCode(char character)
{
    character = char.ToUpper(character);
    return character switch
    {
        'B' or 'F' or 'P' or 'V' => '1',
        'C' or 'G' or 'J' or 'K' or 'Q' or 'S' or 'X' or 'Z' => '2',
        'D' or 'T' => '3',
        'L' => '4',
        'M' or 'N' => '5',
        'R' => '6',
         _ => '0'
     };
}
}
```

### New Complexity
```c++
char getSoundexCode(char c) {
    c = toupper(c);
    std::map<char,char> charMap = { {'B','1'}, {'F','1'}, {'P','1'}, {'V','1'},
                           {'C','2'}, {'G','2'}, {'J','2'}, {'K','2'}, {'Q','2'}, {'S','2'}, {'X','2'}, {'Z','2'},
                           {'D','3'}, {'T','3'},
                           {'L','4'},
                           {'M','5'}, {'N','5'},
                           {'R','6'},
                           {'A','0'}, {'E','0'}, {'I','0'}, {'O','0'}, {'U','0'}, {'H','0'}, {'W','0'}, {'Y','0'}
                           };
    // return Map consonants to digits
    for (auto charValue : charMap) // Look at each key-value pair
    {
        if (charValue.first == c)
        {
            return charValue.second;
        }
    }
}
```

### Good Separation  in Action
```C++
class Soundex {
public:
    // Constructor
    Soundex();

    // Generates the full Soundex code for a given name
    std::string generateSoundex(const std::string& name);

private:
    // Static array mapping characters to Soundex codes
    static const char soundexMap[26];

    // Get the Soundex code for a given character
    char getSoundexCode(char c) const;

    // Start the Soundex code with the first letter of the name
    std::string startSoundex(const std::string& name) const;

    // Generate the remaining Soundex code
    void generateRemainingSoundex(std::string& soundex, const std::string& name) const;

    // Process the current character in the name
    void processCurrentChar(std::string& soundex, char currentChar, char& prevCode, char& prevPrevChar) const;

    // Check if the code should be added
    bool shouldAddCode(char prevPrevChar, char currentChar) const;

    // Add the character to the Soundex code
    void processCharacter(std::string& soundex, char code, char& prevCode) const;

    // Check if the Soundex code is valid (not '0')
    bool isValidSoundexCode(char code) const;

    // Check if the code is different from the previous one
    bool isNewCode(char code, char prevCode) const;

    // Check if characters are separated by 'H' or 'W'
    bool isSeparatedByHorW(char prevPrevChar) const;

    // Pad the Soundex code with zeros to ensure it's 4 characters long
    void padWithZeros(std::string& soundex) const;

    // Check if the character is a vowel
    bool isVowel(char c) const;

    bool shouldContinueProcessing(size_t nameLength, size_t soundexLength) const;

    bool shouldAddCode(char currentCode, char prevCode, char prevPrevCode) const;

    bool isShortName(const std::string& name) const;
    bool canAddCode(char prevPrevCode, char currentCode) const ;
```
### UnNecessary Test Cases
```c
char arr_with_ret_1[4] = {'B','F','P','V'};
char arr_with_ret_2[8] = {'C','G','J','K','Q','S','X','Z'};
char arr_with_ret_3[2] = {'D','T'};
char arr_with_ret_4[1] = {'L'};
char arr_with_ret_5[2] = {'M','N'};
char arr_with_ret_6[1] = {'R'};


// Test cases for getSoundexCode function
TEST(SoundexTest_ret_1, GetSoundexCode)
{
    for (int i=0;i<4;i++)
    {
        EXPECT_EQ(getSoundexCode(arr_with_ret_1[i]), '1');
    }
}

TEST(SoundexTest_ret_2, GetSoundexCode)
{
    for (int i=0;i<8;i++)
    {
        EXPECT_EQ(getSoundexCode(arr_with_ret_2[i]), '2');
    }
}

```
