# Grupo 30 - YL335B

- [Classificação](#classificação)
  - [Estações](#estações)
    - [Estação 10](#estação-10)
    - [Estação 20](#estação-20)
    - [Estação 30](#estação-30) 
    - [Estação 40](#estação-40)
    - [Estação 50](#estação-50)
  - [PROFINET](#PROFINET)
  - [Modbus](#modbus)
- [Componentes](#componentes)
  - [Sensor Fotoelétrico](#sensor-fotoelétrico)
  - [Sensor Magnético](#sensor-magnético) 
  - [Sensor Indutivo](#sensor-indutivo) 
  - [Sensor Ótico](#sensor-ótico) 
  - [Cilindro Pneumático](#cilindro-pneumático)
- [Equipamentos](#equipamentos)
  - [Siemens S7 1200](#siemens-s7-1200) 
  - [Enconder](#enconder)
    - [Manual Enconder](./equipments/manuais/manual_enconder.md)
  - [Servo Motor](#servo-motor)
    - [Manual Servo Motor](./equipments/manuais/manual_servo.md)
  - [Inversor de Frequência](#inversor-de-frequência)
  - [HMI-T](#hmi-t)
- [Lines](#lines)
  - [Line 31](#line-31)
    - [2020_2021](./lines/line31/2020_2021/line31.md)
    - [2021_2022](./lines/line31/2021_2022/line31.md)
    - [2022_2023](./lines/line31/2022_2023/line31.md) 
  - [Line 32](#line-32)
    - [2020_2021](./lines/line32/2020_2021/line322.md)
    - [2021_2022](./lines/line32/2021_2022/line32.md)
    - [2022_2023](./lines/line32/2022_2023/line32.md)  
  - [Line 33](#line-33)
    - [2020_2021](./lines/line33/2020_2021/line33.md)
    - [2021_2022](./lines/line33/2021_2022/line33.md)
    - [2022_2023](./lines/line33/2022_2023/line33.md)  
- [Software](#software)
  - [TIA Portal](#tia-portal)
  - [Tesla Scada](#tesla-scada)
  - [Draw io](#draw-io)
  - [GEMMA](#gemma)

## Classificação
### Estações
#### Estação 10
*Entradas dos 19PLC*

|Label |Endereço  | Comentário|
--- | --- | ---
3211*B42|%I0.3|Sensor de Garra em Baixo
3211*B41|%I0.4|Sensor de Garra em Cima
3211*B32|%I0.5|Sensor Garra (Rotação)
3211*B31|%I0.6|Sensor Garra (Posição Inicial)
3211*B21|%I0.7|Sensor de Garra á Frente
3211*B22|%I1.0|Sensor de Garra Atrás
3211*B11|%I1.1|Sensor de Garra Fechada
321920SB22|%I8.4|Botão Vermelho
321920SB21|%I8.5|Botão Verde
321920QS24|%I8.6|Botão Emergência
321920SA23|%I8.7|Seletor

*Saidas dos 19PLC*

|Label |Endereço  | Comentário|
--- | --- | ---
3211*Y40|%Q0.3|Cilindro da Garra (Sobe e Baixa)
3211*Y30B|%Q0.4|Cilindro da Garra (Rotação)
3211*Y30A|%Q0.5|Cilindro da Garra (Posição Inicial)
3211*Y20|%Q0.6|Cilindro da Garra (Frente e Atrás)
3211*Y10B|%Q0.7|Cilindro de Fecho Garra
3211*Y10A|%Q1.0|Cilindro de Abertura da Garra
321920HL11|%Q8.5|Painel Luz Laranja
321920HL12|%Q8.6|Painel Luz Verde
321920HL13|%Q8.7|Painel Luz Vermelha

#### Estação 20
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

#### Estação 30
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

#### Estação 40
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
3242*B21|%I1.5|Sensor de Garra em Cima
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

#### Estação 50
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
325920HL12|%Q1.0|Luz do Painel (Verde)
325920HL13|%Q1.1|Luz do Painel (Vermelha)

### PROFINET
### Modbus

## Componentes
### Sensor Fotoelétrico
### Sensor Magnético
### Sensor Indutivo
### Sensor Ótico
### Cilindro Pneumático

## Equipamentos

### Enconder

Encoders ou geradores de Impulsos são equipamentos eletromecânicos, utilizados para conversão de movimentos rotativos ou deslocamentos lineares em impulsos elétricos de onda
quadrada, que geram uma quantidade exata de impulsos por volta em uma distribuição perfeita dos pulsos ao longo dos 360 graus do giro do eixo. Ao longo deste documento serão
abordados os passos de configuração do encoder e como integrar o mesmo num programa.

Os enconders podem ser classificados como **"Encoder Relativos"** ou **"Encoder Absoluto"**. **"Encoder Relativos"**, dizem-nos a posição relativa ao ponto onde o encoder foi
ativado, normalmente possuem 3 saídas A, B e Z. **"Encoder Absolutos"**, dizem-nos a posição absoluta através de saídas digitais codificadas em um valor binário.

#### - [Manual Enconder](./equipments/manuais/manual_enconder.md)

### Servo Motor

Um Servo Motor, é um equipamento eletrônico utilizado como um atuador em sistemas de controlo automático, ele converte sinais elétricos num movimento angular no veio do motor. Na
Oficina Luban, mais especificamente no Grupo 30 (YL-335B), o Servo Motor esta ligado a um Motor AC SIMOTICS S-1FL6 que permite a deslocação do carro.

#### - [Manual Servo Motor](./equipments/manuais/manual_servo.md)

### Inversor de Frequência

Um Inversor de Frequência é um equipamento eletrônico, utilizado para variar a velocidade de um motor. Este equipamento transforma o Sinal Analogico, vindo do PLC, em corrente
alternada. Na Oficina Luban, mais especificamente no Grupo 30 (YL-335B), o Inversor de Frequência esta ligado a um Motor Trisáfico e a este está acopulado um Enconder que permite as
seleção das peças de forma correta e precisa. 

### Siemens S7 1200

## Lines
### Line 31
#### - [2020_2021](./lines/line31/2020_2021/line31.md)
#### - [2021_2022](./lines/line31/2021_2022/line31.md)
#### - [2022_2023](./lines/line31/2022_2023/line31.md)

### Line 32
#### - [2020_2021](./lines/line32/2020_2021/line322.md)
#### - [2021_2022](./lines/line32/2021_2022/line32.md)
#### - [2022_2023](./lines/line32/2022_2023/line32.md)

### Line 33
#### - [2020_2021](./lines/line33/2020_2021/line33.md)
#### - [2021_2022](./lines/line33/2021_2022/line33.md)
#### - [2022_2023](./lines/line33/2022_2023/line33.md)

## Software
### TIA Portal
[TIA Portal](https://new.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal.html), Totally Integrated Automation Portal, desenvolvido pela
Siemens é um software que oferece uma vasta gama ferramentas, desta forma é possivel realizar o trabalho de forma rapida e eficaz. Intregado ao TIA Portal temos o WinCC, a ferramenta
utilizada para a programação das HMI's na Ofina Luban.

### Tesla Scada
[Tesla Scada](https://teslascada.com/) foi o software escolhido para implementação de interfaces homem-máquina na Oficina Luban. O Tesla Scada permite o controlo e supervisão em
tempo real de sistemas e processos industriais baseados em PLC. 

### Draw io
[Draw.io](Draw.io), é um software gratuito que premite a criação de Grafcets, Fluxogramas, entre outras.

### Gemma
O Gemma consiste num Guia de estudo dos modos de Marcha e Paragem. Num processo automaziado, por necessidade, é necessário prever todos os estados possíveis, desta forma, com o
Gemma, é possivel executar arranques ou paragens de forma segura sem prejudicar ou Homem ou a Máquina.

Como podemos observar na figura a baixo, o Gemma, devide-se em 3 grande blocos: **"Procedimentos de paragem"**, **"Procedimentos de execução"**, **"Procedimentos de falha"** e a cada
um dele correspondem um conjunto de funções/tarefas.

![](./software/imagens/GEMMA.svg)

- **Procedimentos de Paragem**
  - **A1 - Parado no estado inicial** -> Diz-nos que o processo já foi inciado e está pronto a começar.
  - **A2 - Fim de ciclo solicitado** -> Diz-nos que o processo encontra-se em produção, assim que chegar ao final do ciclo volta ao estado inicial. (A1)
  - **A3 - Paragem solicitada** -> Neste estado, o processo para num certo estado que não coincide com o fim do ciclo. Esta paragem ocorre devido alguma falha/erro na produção
  continua.
  - **A4 - Paragem finalizada** -> Diz-nos que a paragem solicitada foi concluida, desta forma, o processo está pronto a começar.
  - **A5 - Preparação para retomar** -> Neste estado, procedem todas as operações, que deram origem à Paragem de Emergencia ou Diagnóstico/tratamento de falha desde: limpeza,
  substituição/reparação de uma peça/produto, entre outros.
  - **A6 - Colocação no estado inicial** -> Neste estado, procedesse a inicialização do sistema.
  - **A7 - Colocação em estado específico** -> Neste estado, o processo é retornado para uma posição específica, quando não é necessário voltar ao estado inicial.

- **Procedimentos de execução**
  - **F1 - Marcha de produção COM ordem** -> Neste estado, o processo produz normalmente. Aqui as tarefas para as quais o processo foi desenvolvido devem ser realizadas.
  - **F2 - Marcha de preparação** -> Corresponde as ações necessárias para a máquina entrar produção.
  - **F3 - Marcha de finalização** -> Corresponde ao conjunto de ações necessárias que o processo deve realizar antes de parar.
  - **F4 - Marchas de verificação SEM ordem** -> Neste estado, o processo, opera por ordem do operador, pode realizar qualquer movimento. Corresponde ao Modo Manual, normalmente
  usado para funções de controle manutenção e verificação.
  - **F5 - Marchas de verificação COM ordem** -> Neste estado, o processo, realiza o ciclo completo de operação em ordem. Corresponde ao Modo Semi - Automático, normalmente usado
  para manutenção e verificação de possiveis erros não encontrados na Marchas de TESTE.
  - **F6 - Marchas de TESTE** -> Nesse estado, realizam-se operações de ajuste e manutenção preventiva.

- **Procedimentos de falha**
  - **D1 - Paragem de emergência** ->  Neste estado, por imposição do Homem ou do Processo, o processo entra em emergência, desta forma, evita-se e reduz-se o perigo.
  - **D2 - Diagnóstico/tratamento de falha** -> Neste estado, o processo, é examinado após uma falha. Esta falha pode ser tratada com ou sem a intervrção do operador. Quando concluida o processo está pronto para reiniciar.
  - **D3 - Produção em estado de emergência** -> Neste estado, o processo, mesmo encontrando-se em emergência, pode continuar a operar. Um exemplo, falta uma peça, essa falta origina
  um alarme mas não uma paragem total do processo, isto porque, pode ser rapidamente substituida ou não revela ser fundamental para o produto final.
    
  [WebGrafia Gemma]: <> (http://isa.uniovi.es/~vsuarez/Download/GemmaTelemecanique.PDF.)

## Manuais Gerais

# Teste

<video width="320" height="240" autoplay muted>
  <source src="./movie/1.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>