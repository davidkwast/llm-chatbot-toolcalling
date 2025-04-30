# llm-chatbot-toolcalling

## usage

```shell
$ poetry run python tools.py 'qual o tch no talhao 23006'
qual o tch no talhao 23006
----------------------------------------
DEBUG: get_tch(23006)
----------------------------------------
========================================
O TCH do talhão "23006" é 999
```

```shell
$ poetry run python tools.py 'qual a quantidade colhida no Talhão 24001 na ultima safra?'
qual a quantidade colhida no Talhão 24001 na ultima safra?
----------------------------------------
DEBUG: get_tch(24001)
----------------------------------------
========================================
O TCH do talhão "24001" é 999
```

```shell
$ poetry run python tools.py 'abastecimento de 80L em JD01'
abastecimento de 80L em JD01
----------------------------------------
DEBUG: set_vehicle_fuel(80,JD01)
----------------------------------------
========================================
Abastecimento de 80L do veículo "JD01" registrado
```

```shell
$ poetry run python tools.py 'registrar abastecimento de 80 em JD01'
registrar abastecimento de 80 em JD01
----------------------------------------
DEBUG: set_vehicle_fuel(80,JD01)
----------------------------------------
========================================
Abastecimento de 80L do veículo "JD01" registrado
```