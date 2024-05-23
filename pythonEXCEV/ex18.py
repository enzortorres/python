from math import sin, cos, tan, radians
ang = float(input('\033[33mDigite o ângulo que você deseja:\033[30m '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'''\033[0;34mO ângulo de \033[4;31m{ang}\033[0;34m tem o SENO de \033[4;31m{seno:.2f}
\033[0;34mO ângulo de \033[4;31m{ang}\033[0;34m tem o COSSENO de \033[4;31m{cosseno:.2f}
\033[0;34mO ângulo de \033[4;31m{ang}\033[0;34m tem a TANGENTE de \033[4;31m{tangente:.2f}\033[m''')