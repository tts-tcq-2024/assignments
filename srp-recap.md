### Conginitive Complexity
https://github.com/tts-tcq-2024/modular-in-cpp-nitish1703-sys.git
https://github.com/tts-tcq-2024/modular-in-cpp-ankegowdaja.git
https://github.com/tts-tcq-2024/modular-in-cs-SanBhat19.git
https://github.com/tts-tcq-2024/modular-in-py-Ananyaa-holla.git
https://github.com/tts-tcq-2024/modular-in-java-Manikandan9559.git

### Better Decomposition
https://github.com/tts-tcq-2024/modular-in-cs-BhavanaYaraska
https://github.com/tts-tcq-2024/modular-in-js-MilindAdiga.git

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

