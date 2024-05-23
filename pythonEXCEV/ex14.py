celsius = float(input('\033[33mInforme a temperatura em °C:\033[30m '))
fahrenheit = celsius * 1.8 + 32
print(f'\033[34mA temperatura de \033[4;31m{celsius:.1f}°C\033[0;34m corresponde a \033[4;31m{fahrenheit:.1f}°F\033[m')
