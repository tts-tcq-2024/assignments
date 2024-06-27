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

