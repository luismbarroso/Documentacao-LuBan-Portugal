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

Para isso estão reservados 7 Bytes: MB0, MB1, MB2, MB3, MB4, MB5, MB6

### Etapas de Grafcet

Etapas de Grafcet, para o funcionamento de um Grafcet são necessárias memórias.

Para isso estão reservados 7 Bytes: MB10, MB11, MB12, MB13, MB14, MB15, MB16.

### Profinet

Profinet, para a comunicação entre os vários PLC é necessário definir uma **Área de Transferência de Bytes**, para que estas comunicações ocorram de forma segura e eficaz. 

Para isso estão reservados 7 Bytes: MB100, MB101, MB102, MB103, MB104, MB105, MB106.

### Modbus

Á semelhança do Profinet, o Modbus, também necessita de uma **Área de Transferência de Bytes**, para a comunicação entre o PLC Master e o Tesla Scada. 

Para isso estão reservados 7 Bytes: MB200, MB201, MB202, MB203, MB204, MB205, MB206.

## Mapa de Memória
### 19PLC

19PLC, corresponde ao PLC Master da Line 32. Responsável por receber/enviar informações entre os vários PLC e por receber ordens do Tesla Scada.

- Memórias - I/O Locais: 
    - MB0, MB1, MB2, MB3, MB4, MB5, MB
- Memórias - Etapas de Grafcet 
    - MB10, MB11, MB12, MB13, MB14 e MB15
- Memórias - Profinet
    - **Inputs:**
    - IDW100 < QDW100 - 29PLC
    - IDW104 < QDW100 - 39PLC
    - IDW108 < QDW100 - 49PLC 
    - IDW112 < QDW100 - 59PLC
    - **Outputs:**
    - QDW100 > IDW100 - 29PLC
    - QDW104 > IDW100 - 39PLC
    - QDW108 > IDW100 - 49PLC
    - QDW112 > IDW100 - 59PLC
- Memórias - Modbus
    - **Inputs:**
    - IDW200 < QDW200 - 29PLC
    - IDW204 < QDW200 - 39PLC
    - IDW208 < QDW200 - 49PLC 
    - IDW212 < QDW200 - 59PLC
    - **Outputs:**
    - QDW200 > IDW200 - 29PLC
    - QDW204 > IDW200 - 39PLC
    - QDW208 > IDW200 - 49PLC
    - QDW212 > IDW200 - 59PLC 

### 29PLC

29PLC, corresponde ao um dos 4 PLC's Slave da Line 32. Responsável por receber/enviar informações sobre ele para o PLC Master. 

- Memórias - I/O Locais: 
    - MB0, MB1, MB2, MB3, MB4, MB5, MB6
- Memórias - Etapas de Grafcet 
    - MB10
- Memórias - Profinet
    - **Inputs:**
    - IDW100 < QDW100 - 29PLC
    - **Outputs:**
    - QDW100 > IDW100 - 29PLC
- Memórias - Modbus
    - **Inputs:**
    - IDW200 < QDW200 - 29PLC
    - **Outputs:**
    - QDW200 > IDW200 - 29PLC

### 39PLC

39PLC, corresponde ao um dos 4 PLC's Slaves da Line 32. 
Responsável por receber/enviar informações sobre ele para o PLC Master. 

- Memórias - I/O Locais: 
    - MB0, MB1, MB2, MB3, MB4, MB5, MB6
- Memórias - Etapas de Grafcet 
    - MB10
- Memórias - Profinet
    - **Inputs:**
    - IDW104 < QDW100 - 39PLC
    - **Outputs:**
    - QDW104 > IDW100 - 39PLC
- Memórias - Modbus
    - **Inputs:**
    - IDW204 < QDW200 - 39PLC
    - **Outputs:**
    - QDW204 > IDW200 - 39PLC

### 49PLC

49PLC, corresponde ao um dos 4 PLC's Slaves da Line 32. 
Responsável por receber/enviar informações sobre ele para o PLC Master. 

- Memórias - I/O Locais: 
    - MB0, MB1, MB2, MB3, MB4, MB5, MB6
- Memórias - Etapas de Grafcet 
    - MB10, MB11 e MB12 
- Memórias - Profinet
    - **Inputs:**
    - IDW108 < QDW100 - 49PLC 
    - **Outputs:**
    - QDW108 > IDW100 - 49PLC
- Memórias - Modbus
    - **Inputs:**
    - IDW208 < QDW200 - 49PLC 
    - **Outputs:**
    - QDW208 > IDW200 - 49PLC


### 59PLC

59PLC, corresponde ao um dos 4 PLC's Slaves da Line 32. 
Responsável por receber/enviar informações sobre ele para o PLC Master. 

- Memórias - I/O Locais: 
    - MB0, MB1, MB2, MB3, MB4, MB5, MB6
- Memórias - Etapas de Grafcet 
    - MB10, MB11, MB12 e MB13
- Memórias - Profinet
    - **Inputs:**
    - IDW112 < QDW100 - 59PLC
    - **Outputs:**
    - QDW112 > IDW100 - 59PLC
- Memórias - Modbus
    - **Inputs:**
    - IDW212 < QDW200 - 59PLC
    - **Outputs:**
    - QDW212 > IDW200 - 59PLC 


## Tabela

||||IOLocais||||
-- | - | - | - | - | - | -
MB0|MB1|MB2| ⠀ MB3|MB4|MB5|MB6	
	
||||Etapas de Grafet||||
--- | -- | -- | -- | -- | -- | --							
MB10|MB11|MB12| ⠀  ⠀  ⠀MB13|MB14|MB15|MB16	
														
||||Profinet||||
--- | -- | -- | -- | -- | -- | --						
MB100|MB101|MB102|MB103|MB104|MB105|MB106	
							
||||Modbus||||
---- | --- | --- | --- | --- | --- | ---
MB200|MB201|MB202|MB203|MB204|MB205|MB206		