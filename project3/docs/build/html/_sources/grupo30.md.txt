# Indice (Grupo 30 - YL335B)

- [Classificação](#classificacao)
  - [Estação 10](#estacao-10)
  - [Estação 20](#estacao-20)
  - [Estação 30](#estacao-30) 
  - [Estação 40](#estacao-40)
  - [Estação 50](#estacao-50)
- [Componentes](#componentes)
  - [Sensor Fotoelétrico](#sensor-fotoeletrico)
  - [Sensor Magnético](#sensor-magnetico) 
  - [Sensor Indutivo](#sensor-indutivo) 
  - [Sensor Ótico](#sensor-otico) 
  - [Cilindro Pneumático](#cilindro-pneumatico)
- [Equipamentos](#equipamentos)
  - [Siemens S7 1200](#siemens-s7-1200) 
  - [Enconder](#enconder)
  - [Servo Motor](#servo-motor)
  - [Inversor de Frequência](#inversor-de-frequencia)
  - [HMI-T](#hmi-t)
  - [Manuais](#manuais)
    - [Manual Enconder](#manual-enconder) 
    - [Manual Servo Motor](#manual-servo-motor) 
- [Lines](#lines)
  - [Line 31](#line-31) 
  - [Line 32](#line-32) 
  - [Line 33](#line-33) 
- [Software](#software)
  - [TIA Portal](#tia-portal) 
- [Manuais Gerais](#manuais-gerais)

## Classificação
### Estação 10
### Estação 20

<!--Entradas da Estação 20-->
<div align="center">
<table>
   <head>
      <tr>
         <th align="center">Entradas</th>
      </tr>
   <head>
      <tr>
      <th></th>
         <th align="center">Label</th>
         <th align="center">Endereço</th>
         <th align="center">Comentário</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td style="vertical-align : middle;text-align:center;" rowspan="1">Estação 20</td>
         <td align="center">3220*B11</td>
         <td align="center">%I0.4</td>
         <td align="center">Sensor de Peça à Frente</td>
      </tr>
      <tr>
         <td style="vertical-align : middle;text-align:center;" rowspan="6">Estação 21</td>
         <td align="center">3221*B11</td>
         <td align="center">%I0.0</td>
         <td align="center">Sensor Cilindro1 Avançado</td>
      </tr>
      <tr>
         <td align="center">3221*B12</td>
         <td align="center">%I0.1</td>
         <td align="center">Sensor Cilindro1 Recuado</td>
      </tr>
      <tr>
         <td align="center">3221*B22</td>
         <td align="center">%I0.3</td>
         <td align="center">Sensor Cilindro2 Recuado</td>
      </tr>
      <tr>
         <td align="center">3221*B32</td>
         <td align="center">%I0.5</td>
         <td align="center">Sensor no Copo (Cima)</td>
      </tr>
      <tr>
         <td align="center">3221*B33</td>
         <td align="center">%I0.6</td>
         <td align="center">Sensor no Copo (Baixo)</td>
      </tr>
      <tr>
         <td align="center">3221*B31</td>
         <td align="center">%I0.7</td>
         <td align="center">Sensor de Peça Metálica</td>
      </tr>
      <tr>
         <td style="vertical-align : middle;text-align:center;" rowspan="4">Potência e Controlo</td>
         <td align="center">322920SB22</td>
         <td align="center">%I1.2</td>
         <td align="center">Botão Vermelho</td>
      <tr>
         <td align="center">322920SB21</td>
         <td align="center">%I1.3</td>
         <td align="center">Botão Verde</td>
      <tr>
         <td align="center">322920QS24</td>
         <td align="center">%I1.4</td>
         <td align="center">Botão Emergência</td>
      <tr>
         <td align="center">322920SA23</td>
         <td align="center">%I1.5</td>
         <td align="center">Seletor</td>
      </tr>
   </tbody>
</table>
</div>

<!--Saidas da Estação 20-->
<div align="center">
<table>
   <head>
      <tr>
         <th align="center">Saidas</th>
      </tr>
   <head>
      <tr>
      <th></th>
         <th align="center">Label</th>
         <th align="center">Endereço</th>
         <th align="center">Comentário</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td style="vertical-align : middle;text-align:center;" rowspan="2">Subestç
         ao 21</td>
         <td align="center">3221*Y10</td>
         <td align="center">%Q0.0</td>
         <td align="center">Cilindro 1</td>
      </tr>
      <tr>
         <td align="center">3221*Y20</td>
         <td align="center">%Q0.1</td>
         <td align="center">Cilindro 2</td>
      </tr>
      <tr>
         <td style="vertical-align : middle;text-align:center;" rowspan="3">Potência e Controlo</td>
         <td align="center">322920HL11</td>
         <td align="center">%Q0.7</td>
         <td align="center">Painel Luz Laranja</td>
      <tr>
         <td align="center">322920HL12</td>
         <td align="center">%Q1.0</td>
         <td align="center">Painel Luz Verde</td>
      <tr>
         <td align="center">322920HL12</td>
         <td align="center">%Q1.1</td>
         <td align="center">Painel Luz Vermelha</td>
   </tbody>
</table>
</div>

### Estação 10

*Entradas dos 19PLC*

|Label |Endereço  | Comentário|
--- | --- | ---
3220*B11|%I0.4|Sensor de Peça à Frente
3221*B11|%I0.0|Sensor Cilindro1 Avançado
3221*B12|%I0.1|Sensor Cilindro1 Recuado
3221*B21|%I0.2|Sensor Cilindro2 Avançado
3221*B22|%I0.3|Sensor Cilindro2 Recuado
3221*B32|%I0.5|Sensor no Copo (Cima)
3221*B33|%I0.6|Sensor no Copo (Baixo)
3221*B31|%I0.7|Sensor de Peça Metálica
322920SB22|%I1.2|Botão Vermelho
322920SB21|%I1.3|Botão Verde
322920QS24|%I1.4|Botão Emergência
322920SA23|%I1.5|Seletor

*Saidas dos 19PLC*

|Label |Endereço  | Comentário|
--- | --- | ---
3221*Y10|%Q0.0|Cilindro 1
3221*Y20|%Q0.1|Cilindro 2
322920HL11|%Q0.7|Painel Luz Laranja
322920HL12|%Q1.0|Painel Luz Verde
322920HL13|%Q1.1|Painel Luz Vermelha



### Estação 30
### Estação 40
### Estação 50

## Componentes
### Sensor Fotoelétrico
### Sensor Magnético
### Sensor Indutivo
### Sensor Ótico
### Cilindro Pneumático

## Equipamentos
### Enconder
### Servo Motor
### Inversor de Frequência
### Siemens S7 1200
### Manuais
#### [Manual Enconder](./manuais/manual_enconder.md)
#### [Manual Servo Motor](./manuais/manual_servo.md)
## Lines
### Line 31
### Line 32
### Line 33

## Software
### TIA Portal

## Manuais Gerais