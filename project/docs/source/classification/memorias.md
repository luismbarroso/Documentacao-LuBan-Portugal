# Memórias

- [Zonas de Memória](#zonas-de-memoria)
  - [I/O Locais](i/o-locais)
  - [Etapas de Grafcet](#etapas-de-grafcet)
  - [Profinet](#profinet)
  - [Modbus](#memorias)
- [Mapa de Memória](#mapas-de-memorias)
  - [19PLC](19-plc)
  - [29PLC](29-plc)
  - [39PLC](39-plc)
  - [49PLC](49-plc)
  - [59PLC](59-plc)

## Zonas de Memória
Cada PLC da Line 32 está divido 4 Zonas de Memórias:

- Memórias - I/O Locais
- Memórias - Etapas de Grafcet
- Memórias - Profinet
- Memórias - Modbus 

### I/O Locais

I/O Locais, consiste nas memórias destinadas aos Input's e Output's do próprio PLC, como por exemplo, um Sensor, uma eletroválvula, entre outros.

Para isso estão reservados 4 Bytes: MB0, MB1, MB2, MB3

### Etapas de Grafcet

Etapas de Grafcet, para o funcionamento de um Grafcet são necessárias memórias.

Para isso estão reservados 96 Bytes: MB10 até à MB99

### Profinet

Profinet, para a comunicação entre os vários PLC é necessário definir uma **Área de Transferência de Bytes**, para que estas comunicações ocorram de forma segura e eficaz. 

Para isso estão reservados 99 Bytes: MB100 até à MB199

### Modbus

Á semelhança do Profinet, o Modbus, também necessita de uma **Área de Transferência de Bytes**, para a comunicação entre o PLC Master e o Tesla Scada. 

Para isso estão reservados 99 Bytes: MB200 até à MB299

## Mapa de Memória
### 19PLC
### 29PLC
### 39PLC
### 49PLC
### 59PLC
