### Conginitive Complexity
- https://github.com/tts-tcq-2024/modular-in-cpp-nitish1703-sys.git
- https://github.com/tts-tcq-2024/modular-in-cpp-ankegowdaja.git
- https://github.com/tts-tcq-2024/modular-in-cpp-nikhilkj1404.git
- https://github.com/tts-tcq-2024/modular-in-cpp-TatShri.git
- https://github.com/tts-tcq-2024/modular-in-cs-SanBhat19.git
- https://github.com/tts-tcq-2024/modular-in-py-Ananyaa-holla.git
- https://github.com/tts-tcq-2024/modular-in-java-Manikandan9559.git
- https://github.com/tts-tcq-2024/modular-in-c-EnciJeffrey13.git

### Naming Chaos
- https://github.com/tts-tcq-2024/modular-in-py-amrutha0404
- https://github.com/tts-tcq-2024/modular-in-c-Pranav-22.git
- https://github.com/tts-tcq-2024/modular-in-c-Deepthisv99.git
- https://github.com/tts-tcq-2024/modular-in-c-Chetan9850.git
- https://github.com/tts-tcq-2024/modular-in-c-vekash2021.git
- https://github.com/tts-tcq-2024/modular-in-py-TaheerAhmed.git

### DRY Violation

- https://github.com/tts-tcq-2024/modular-in-cs-Pavan9606.git

### Better Decomposition
- https://github.com/tts-tcq-2024/modular-in-cs-BhavanaYaraska
- https://github.com/tts-tcq-2024/modular-in-js-MilindAdiga.git
- https://github.com/tts-tcq-2024/modular-in-py-PrafullaPrabhu.git
- https://github.com/tts-tcq-2024/modular-in-cpp-Bharathi1603.git
- https://github.com/tts-tcq-2024/modular-in-java-yin2kor.git

### What would be the better name?
```js
function printManual() {
    const minorSize = MajorColorNames.length;
    const majorSize = MinorColorNames.length;
    let manual = '';

    for (let i = 1; i <= minorSize * majorSize; i++) {
        const colorPair = getColorFromPairNumber(i);
        manual += `Pair Number: ${i}, Colors: ${colorPair.toString()}\n`;
    }

    return manual;
}
```
### Testable ?
```c
void PrintColorCodingReference() {
    int pairNumber = 1;

    for (int major = 0; major < numberOfMajorColors; major++) {
        for (int minor = 0; minor < numberOfMinorColors; minor++) {
            printf("%d. %s-%s\n", pairNumber, MajorColorNames[major], MinorColorNames[minor]);
            pairNumber++;
        }
    }
}
```

```py
def display_color():
   print("\n================== Color Coding Reference Manual =====================")
   for pair_number in range(1,26):
       major_color, minor_color = get_color_from_pair_number(pair_number)
       print(pair_number,color_pair_to_string(major_color, minor_color))

```
#### When Name Reflects Requirement
```py
def create_reference_manual():
    manual = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major, minor)
            manual.append(f'{pair_number:2d} - {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)

```

```c++
std::map<std::uint8_t, ColorPair> TeleComm::getColorPairList()
{
  std::map<std::uint8_t, ColorPair> colorPairList;
  for(std::size_t pairNo = 1; pairNo <=  maxColorPair; pairNo++)
   {
      colorPairList.insert({pairNo, getColorFromPairNumber(static_cast<int>(pairNo))});
   }
   return colorPairList;
}
```


