# Recap



### How to test ?

```c
    //checker.c
    
    int isTemperatureOk = (temperature >= 0 && temperature <= 45);
    int isSocOk = (soc >= 20 && soc <= 80);
    int isChargeRateOk = (chargeRate <= 0.8);
    
    if (!isTemperatureOk) {
        printf("Temperature out of range!\n");
    }
    if (!isSocOk) {
        printf("State of Charge out of range!\n");
    }
    if (!isChargeRateOk) {
        printf("Charge Rate out of range!\n");
    }
    
int main(){
    return (isTemperatureOk && isSocOk && isChargeRateOk);
}
```



### Principle of Least Knowledge Violation

```Java
public class Main {
    static boolean batteryIsOk(float temperature, float soc, float chargeRate) {
    	if(checkMinTemperature(temperature)) {
    		return checkMaxTemperature(temperature, soc, chargeRate);
    	} else {
    		return false;
    	}
    }
    
    private static boolean checkMinTemperature(float temperature) {
    	if(temperature < 0) {
    		printStatus("Temperature is out of range!");
            return false;
        }
    	return true;
    }
    
    private static boolean checkMaxTemperature(float temperature, float soc, float chargeRate) {
    	if(temperature > 45) {
    		printStatus("Temperature is out of range!");
            return false;
        }
    	return checkMinSoc(soc, chargeRate);
    }
    
    private static boolean checkMinSoc(float soc, float chargeRate) {
    	if(soc < 20) {
    		printStatus("State of Charge is out of range!");
    		return false;
    	}
    	return checkMaxSoc(soc, chargeRate);
    }
    
    private static boolean checkMaxSoc(float soc, float chargeRate) {
    	if(soc > 80) {
    		printStatus("State of Charge is out of range!");
    		return false;
    	}
    	return checkChargeRate(chargeRate);
    }
    
    private static boolean checkChargeRate(float chargeRate) {
    	if(chargeRate > 0.8) {
    		printStatus("Charge Rate is out of range!");
            return false;
        }
    	return true;
    }
```
```C
int chargeRate_range(float chargeRate)
{
  if(chargeRate > 0.8 ) {
    printf("Charge Rate out of range!\n");
    return 0;
  }
     return 1;
}

int soc_range(float soc,float chargeRate)
{
    int result = 1;
   if(soc > 80)
   {
    printf("State of Charge out of range!\n");
    return 0;
  }
   result = chargeRate_range(chargeRate);

    return result;
}

int temp_range(float temperature, float soc, float chargeRate)
{
    int result = 1;
    
    if(temperature > 45) {
    printf("Temperature out of range!\n");
    return 0;
  } 
    result = soc_range(soc,chargeRate);

    return result;
}

int batteryIsOk(float temperature, float soc, float chargeRate) {

  int result = 1;
   
  result = temp_range(temperature,soc,chargeRate);

  return result;
}
```



### Don't change Default interface of the Code

```python
def battery_temp_is_ok(temperature):
  if not 0<=temperature<=45:
    print('Temperature is out of range!')
    return False
  return True
def battery_soc_is_ok(soc):
  if not 20<=soc<=80:
    print('State of Charge is out of range!')
    return False
  return True
def battery__cr_is_ok(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False

  return True


if __name__ == '__main__':
  assert((battery_temp_is_ok(25) and battery_soc_is_ok(70) and battery__cr_is_ok(0.7)) is True)
  assert((battery_temp_is_ok(50) and battery_soc_is_ok(85) and battery__cr_is_ok(0)) is False)

```



###  DRY Violation

----

```C
int TemperaureIsOk(float temperature)
{
     if (temperature < 0 || temperature > 45) 
     {
        printf("Temperature out of range\n");
        return 0;
     }
     return 1;
}
int socIsOk(float soc)
{
    if (soc < 20 || soc > 80) 
    {
        printf("State of Charge out of range!\n");
        return 0;
    }
    return 1;
}

int chargeRateIsOk(float chargeRate)
{
    if (chargeRate > 0.8) 
    {
        printf("Charge Rate out of range!\n");
        return 0;
    }
    return 1;
}
```

### Is this code Bug Free?
---
```C++
bool batteryIsOk(float temperature, float soc, float chargeRate) {

   bool retvalue;

   retvalue = checktemp(temperature);
   retvalue = checksoc(soc);
   retvalue = checkchargeRate(chargeRate);

   return retvalue;
}
```

### Good Separation

---

```C++
bool BatteryManagementSystem::inputInRange(float minValue, float maxValue, float inputValue, const std::string&  valueType)
{
  if (inputValue > minValue && inputValue < maxValue)
  {
    printOutput(true, valueType);
    return true;
  }
  else
  {
    printOutput(false, valueType);
    return false;
  }
}

bool BatteryManagementSystem::printOutput(bool result, const std::string& valueType)
{
  bool inRange = result;
  std::string valueTypename = valueType;
  if (inRange)
  {
    printf("Value %s is in range", valueTypename.c_str());
    return true;
  }
  else
  {
    printf("Value %s is not in range! Please check", valueTypename.c_str());
    return false;
  }
}

bool BatteryManagementSystem::checkTemperatureOk(float temperature)
{
  float minTemperature = 0;
  float maxTemperature = 45;
  float currentTemperature = temperature;
  return inputInRange(minTemperature, maxTemperature, currentTemperature, "temperature");
}

bool BatteryManagementSystem::checkSocOk(float state_of_charge)
{
  float minSoc = 20;
  float maxSoc = 80;
  float currentSoc = state_of_charge;
  return inputInRange(minSoc, maxSoc, currentSoc, "state_of_charge");
}

bool BatteryManagementSystem::checkChargeRateOk(float charge_rate)
{
  float minCharge = 0.1;
  float MaxCharge = 0.8;
  float currentCharge = charge_rate;
  return inputInRange(minCharge, MaxCharge, currentCharge, "charge_rate");
}

```
### Good Spread of Test Cases(Object Oriented Paradigm)
```C++
#include <assert.h>
#include <iostream>

using namespace std;


class BatteryManagementSystem {
private:
    static constexpr float kMinTemperature = 0.0f;
    static constexpr float kMaxTemperature = 45.0f;
    static constexpr float kMinSoc = 20.0f;
    static constexpr float kMaxSoc = 80.0f;
    static constexpr float kMaxChargeRate = 0.8f;

public:
    bool isTemperatureInRange(float temperature) const;
    bool isSocInRange(float soc) const;
    bool isChargeRateInRange(float chargeRate) const;
    bool batteryIsOk(float temperature, float soc, float chargeRate) const;

private:
    void logMessage(const std::string& message, float value, bool isHigh) const;
};

void BatteryManagementSystem::logMessage(const std::string& message, float value, bool isHigh) const {
    cout << message << ": " << value << " (" << (isHigh ? "high" : "low") << ")" << endl;
}

bool BatteryManagementSystem::isTemperatureInRange(float temperature) const {
    if (temperature < kMinTemperature || temperature > kMaxTemperature) {
        logMessage("Temperature out of range", temperature, temperature > kMaxTemperature);
        return false;
    }
    return true;
}

bool BatteryManagementSystem::isSocInRange(float soc) const {
    if (soc < kMinSoc || soc > kMaxSoc) {
        logMessage("State of Charge out of range", soc, soc > kMaxSoc);
        return false;
    }
    return true;
}

bool BatteryManagementSystem::isChargeRateInRange(float chargeRate) const {
    if (chargeRate > kMaxChargeRate) {
        logMessage("Charge Rate out of range", chargeRate, true);
        return false;
    }
    return true;
}

bool BatteryManagementSystem::batteryIsOk(float temperature, float soc, float chargeRate) const {
    return isTemperatureInRange(temperature) && isSocInRange(soc) && isChargeRateInRange(chargeRate);
}

void testIsTemperatureInRange() {
    BatteryManagementSystem bms;
    assert(bms.isTemperatureInRange(0) == true);
    assert(bms.isTemperatureInRange(45) == true);
    assert(bms.isTemperatureInRange(25) == true);
    assert(bms.isTemperatureInRange(-0.1) == false);
    assert(bms.isTemperatureInRange(45.1) == false);
    assert(bms.isTemperatureInRange(-5) == false);
    assert(bms.isTemperatureInRange(50) == false);
}

void testIsSocInRange() {
    BatteryManagementSystem bms;
    assert(bms.isSocInRange(20) == true);
    assert(bms.isSocInRange(80) == true);
    assert(bms.isSocInRange(50) == true);
    assert(bms.isSocInRange(19.9) == false);
    assert(bms.isSocInRange(80.1) == false);
    assert(bms.isSocInRange(10) == false);
    assert(bms.isSocInRange(90) == false);
}

void testIsChargeRateInRange() {
    BatteryManagementSystem bms;
    assert(bms.isChargeRateInRange(0.7) == true);
    assert(bms.isChargeRateInRange(0) == true);
    assert(bms.isChargeRateInRange(0.7) == true);
    assert(bms.isChargeRateInRange(0.81) == false);
    assert(bms.isChargeRateInRange(0.9) == false);
}

void testBatteryIsOk() {
    BatteryManagementSystem bms;
    assert(bms.batteryIsOk(25, 70, 0.7) == true);
    assert(bms.batteryIsOk(25, 70, 0.7) == true);
    assert(bms.batteryIsOk(0, 20, 0) == true);
    assert(bms.batteryIsOk(-1, 70, 0.7) == false);
    assert(bms.batteryIsOk(25, 19, 0.7) == false);
    assert(bms.batteryIsOk(25, 70, 0.9) == false);
    assert(bms.batteryIsOk(50, 85, 0) == false);
}

int main() {
    testIsTemperatureInRange();
    testIsSocInRange();
    testIsChargeRateInRange();
    testBatteryIsOk();
    std::cout << "All tests passed!" << std::endl;
    return 0;
}

```
### Reusablity
```c
int value_within_range(float val,float min,float max, const char* msg)
{
  if(val < min || val > max)
  {
    printf("%s\n",msg);
    return 0;
  }
    return 1;
}

int batteryIsOk(float temperature, float soc, float chargeRate)
{
  return value_within_range(temperature,0,45,"Temperature out of range!")
      && value_within_range(soc,20,80,"State of Charge out of range!")
      && value_within_range(chargeRate,0,0.8,"Charge Rate out of range!");
    
}

int main() {
  assert(batteryIsOk(25, 70, 0.7));
  assert(!batteryIsOk(50, 85, 0));
}
```
### Look Up Solution
```c
typedef enum {
    TEMP_OK,
    SOC_OK,
    CHARGE_OK,
    TEMP_OUT_OF_RANGE,
    SOC_OUT_OF_RANGE,
    CHARGE_OUT_OF_RANGE
} BatteryStatus;

const char* getErrorMessage(BatteryStatus status) {
    switch (status) {
        case TEMP_OUT_OF_RANGE:
            return "Temperature out of range!\n";
        case SOC_OUT_OF_RANGE:
            return "State of Charge out of range!\n";
        case CHARGE_OUT_OF_RANGE:
            return "Charge Rate out of range!\n";
        default:
            return "";
    }
}
```
### Intresting Code
```c


int batteryIsOk(float temperature, float soc, float chargeRate) {
  if (1 < (temperatureIsOk(temperature) + socIsOk(soc) + chargeRateIsOk(chargeRate) ))
  {return 1;}
  else
  {return 0;}
}

int main() {
  assert(batteryIsOk(25, 70, 0.7));
  assert(!batteryIsOk(50, 85, 0));
}
```

### Pure Functions
```c
int isOutOfRange(float value, float LB, float UB)
{
  return (value < LB || value > UB);
}
int isGreaterThan(float value, float threshold)
{
  return (value > threshold);
}
bool batteryIsOk(float temperature, float soc, float chargeRate) 
{ 
  int count = 0;
  count = count + isOutOfRange(temperature, 0, 45);
  count = count + isOutOfRange(soc, 20, 80);
  count = count + isGreaterThan(chargeRate, 0.8);
  printf("count value: %d\n", count);
  if (count > 1)
  {
    printf("Battery not okay\n");
    return false;
  }
  else
  {
    return true;
  }
}
```

### DataStructure Based Solution
```c
typedef struct {
    CheckFunc check;
    float value;
    const char *message;
} Check;
 
int isTemperatureInRange(float temperature) {
    return (temperature >= 0 && temperature <= 45);
}
 
int isSocInRange(float soc) {
    return (soc >= 20 && soc <= 80);
}
 
int isChargeRateInRange(float chargeRate) {
    return (chargeRate <= 0.8);
}
.......
......
int batteryIsOk(float temperature, float soc, float chargeRate) {
    Check checks[] = {
        {isTemperatureInRange, temperature, "Temperature out of range!\n"},
        {isSocInRange, soc, "State of Charge out of range!\n"},
        {isChargeRateInRange, chargeRate, "Charge Rate out of range!\n"}
    };
 
    for (int i = 0; i < sizeof(checks) / sizeof(checks[0]); ++i) {
        if (!checks[i].check(checks[i].value)) {
            printf("%s", checks[i].message);
            return 0;
        }
    }
 ```

```
