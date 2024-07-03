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
