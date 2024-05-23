m = int(input('\033[33mUma distância em metros:\033[30m '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'''\033[4;31m{km}\033[34mkm
\033[31m{hm}\033[34mhm
\033[31m{dam}\033[34mdam
\033[31m{m}\033[34mm
\033[31m{dm}\033[34mdm
\033[31m{cm}\033[34mcm
\033[31m{mm}\033[34mmm\033[m''') 