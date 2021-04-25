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
  - [Enconder](#enconder)[
  - [Servo Motor](#servo-motor)]
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
  - [Tesla Scada](#tesla-scada)
  - [Draw.io](draw-io)
  - [GEMMA](#gemma) 

## Classificação
### Estação 10
*Entradas dos 29PLC*
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

*Saidas dos 29PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
3221*Y10|%Q0.0|Cilindro 1
3221*Y20|%Q0.1|Cilindro 2
322920HL11|%Q0.7|Painel Luz Laranja
322920HL12|%Q1.0|Painel Luz Verde
322920HL13|%Q1.1|Painel Luz Vermelha

### Estação 30
*Entradas dos 39PLC*

|Label |Endereço  | Comentário|
--- | --- | ---
3231*B11|%I0.0|Sensor Peça na Pinça
3231*B21|%I0.1|Sensor da Pinça (Abrir/Fechar)
3231*B31|%I0.2|Sensor de Pinça Avancada
3231*B32|%I0.3|Sensor de Pinça Recuada
3232*B11|%I0.4|Sensor de Prensa Subida
3232*B12|%I0.5|Sensor de Prensa Descida
323920SB22|%I1.2|Botão Vermelho
323920SB21|%I1.3|Botão Verde
323920QS24|%I1.4|Botão Emergência
323920SA23|%I1.5|Seletor

*Saidas dos 39PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
3231*Y20|%Q0.0|Cilindro de Fechar a Pinça
3231*Y20|%Q0.2|Cilindro da Pinça (Avanço e Recuo)
3232*Y10|%Q0.3|Cilindro da Prensa (Sobe e Desce)
323920HL11|%Q0.7|Painel Luz Laranja
323920HL12|%Q1.0|Painel Luz Verde
323920HL13|%Q1.1|Painel Luz Vermelha

### Estação 40
*Entradas dos 49PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
3241*B11|%I0.5|Sensor Cilindro1 Avançado
3241*B12|%I0.6|Sensor Cilindro1 Recuado
3241*B21|%I0.7|Sensor Cilindro2 Avançado
3241*B22|%I1.0|Sensor Cilindro2 Recuado
3241*B31|%I1.1|Sensor Prato (Posição Inicial)
3241*B32|%I1.2|Sensor Prato (Rotação)
3241*B41|%I0.0|Sensor no Copo (Cima)
3241*B42|%I0.1|Sensor no Copo (Baixo)
3241*B43|%I0.2|Sensor do Prato (Esquerdo)
3241*B44|%I0.3|Sensor do Prato (Direito)
3242*B11|%I8.1|Sensor de Garra á Frente
3242*B12|%I8.0|Sensor de Garra Atrás
3242*B21|%I1.|Sensor de Garra em Cima
3242*B22|%I1.4|Sensor de Garra em Baixo
3242*B31|%I1.3|Sensor de Garra (Abrir/Fechar)
3242*B41|%I0.4|Sensor de Peça à Frente
324920SB22|%I8.4|Botão Vermelho
324920SB21|%I8.5|Botão Verde
324920QS24|%I8.6|Botão Emergência
324920SA23|%I8.7|Seletor

*Saidas dos 49PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
3240*H13|%Q0.6|Semáforo Vermelho
3240*H12|%Q0.7|Semáforo Amarelo
3240*H11|%Q1.0|Semáforo Verde
3241*Y10|%Q0.1|Cilindro 1 Tubo
3241*Y20|%Q0.0|Cilindro 2 Tubo
3241*Y30|%Q0.2|Prato
3242*Y10|%Q0.5|Cilindro da Garra (Frente e Tras)
3242*Y20|%Q0.4|Cilindro da Garra (Cima e Baixo)
3242*Y30|%Q0.3|Cilindro da Garra (Abrir e Fechar)
324920HL11|%Q8.5|Luz do Painel (Laranja)
324920HL12|%Q8.6|Luz do Painel (Verde)
324920HL13|%Q8.7|Luz do Painel (Vermelha)

### Estação 50
*Entradas dos 59PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
Enconder_A|%I0.0|Enconder A
Enconder_B|%I0.1|Enconder B
Enconder_Z|%I0.2|Enconder Z
325010B11|%I0.3|Sensor de Peça (Tapete)
325010B13|%I0.4|Sensor de Peça Metálica
325010B12|%I0.5|Sensor de Peça Branca/Metálica
325010B21|%I0.7|Sensor Cilindro1 Avançado
325010B31|%I1.0|Sensor Cilindro2 Avançado
325010B41|%I1.1|Sensor Cilindro3 Avançado
325920SB22|%I1.2|Botão Vermelho
325920SB21|%I1.3|Botão Verde
325920QS24|%I1.4|Botão Emergência
325920SA23|%I1.5|Seletor

*Saidas dos 59PLC*
|Label |Endereço  | Comentário|
--- | --- | ---
3250M51A|%Q0.0|Inversores de Freq. (Frente)
3250M51B|%Q0.1|Inversores de Freq. (Atrás)
325010Y20|%Q0.4|Cilindro 1
325010Y30|%Q0.5|Cilindro 2
325010Y40|%Q0.6|Cilindro 3
325920HL11|%Q0.7|Luz do Painel (Laranja)
325920HL12|%Q1.0|uz do Painel (Verde)
325920HL13|%Q1.1|Luz do Painel (Vermelha)

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
#### - [Manual Enconder](./manuais/manual_enconder.md)
#### - [Manual Servo Motor](./manuais/manual_servo.md)
## Lines
### Line 31
### Line 32
### Line 33

## Software
### TIA Portal
[TIA Portal](https://new.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal.html), Totally Integrated Automation Portal, desenvolvido pela Siemens é um software que oferece uma vasta gama ferramentas, desta forma é possivel realizar o trabalho de forma rapida e eficaz. Intregado ao TIA Portal temos o WinCC, a ferramenta utilizada para a programação das HMI's na Ofina Luban.

### Tesla Scada
[Tesla Scada](https://teslascada.com/) foi o software escolhido para implementação de interfaces homem-máquina na Oficina Luban. O Tesla Scada permite o controlo e supervisão em tempo real de sistemas e processos industriais baseados em PLC. 

### Draw.io
[Draw.io](Draw.io), é um software gratuito que premite a criação de Grafcets, Fluxogramasm, entre outras.

### Gemma
![](./software/imagens/GEMMA.svg)


## Manuais Gerais