# Line 32

**Autor:** *Luís Barroso*

- [Introdução](#introdução)
- [Processo](#processo)
    - [Peças](#peças)
    - [Estações](#estacoes)
- [Trabalho Realizado](#trabalho-realizado)
    - [Classificação](#classificacao)
        - [Estação 10](#estação-10)
        - [Estação 20](#estação-20)
        - [Estação 30](#estação-30) 
        - [Estação 40](#estação-40)
        - [Estação 50](#estação-50)   
    - [Software](#software)
        - [Grafcets Modo: Manual](#grafcets-modo:-manual)
            - [Estação 10](#estação-10-manual)
            - [Estação 20](#estação-20-manual)
            - [Estação 30](#estação-30-manual) 
            - [Estação 40](#estação-40-manual)
            - [Estação 50)](#estação-50-manual)
        - [Grafcets Modo: Automático](#grafcets-modo:-automático)	
            - [Estação 10](#estação-10-automático)
            - [Estação 20](#estação-20-automático)
            - [Estação 30](#estação-30-automático) 
            - [Estação 40](#estação-40-automático)
            - [Estação 50](#estação-50-automático)
        - [Gemma](#gemma)
            - [Projeto 1](#projeto-1)
 

## Introdução

A Line 32 é uma das Lines do Grupo 30. Divida em 5 estações das quais resultam: **"Transporte (Estação 10)"**, **"Aplicação (Estação 30)"**, **"Alimentação (Corpo (Estação 20) e Miolo (Estação 40))"** e **"Seleção (Estação 50)"**.

[LIN32_1](./images/line/line32_1.jpg)

## Processo

A Line 32, do Grupo 30, consiste num conjunto de estações, **cada uma com Equipamentos/Componenetes independentes**. A Line 32, assim com cada uma da estações, funcionam usando **sistemas pneumáticos** sendo assim possivel realizar os movimentos pretendidos. 

Para o controlo das peças são usados Sensores, como: **Sensores Fotoelétricos**, usados para a detecção das peças em deterniadas posições; **Sensores Indutivos** usados para distiguir as peças metálicas das peças de plástico; **Sensores Óticos** usados para distiguir a peças brancas das peças pretas e **Sensores Magneticos** usados para detetar a posição da haste do cilindro.

Para além dos **sistemas pneumáticos** também existem **sistemas eletromecânico**, na Estação 10 e 50. Na estação 10, este sistemas, são responsaveis pelo movimento do **robô**. Este robô é utilizado para o transporte das peças pelas diversas estações. Acoplado ao robô, temos uma **garra**, sendo assim possivel realizar as tarefas pretendidas. Para se deslocar pelas diversas estações, o robô, está conectado a um Servo Motor (Simotics S-1FL6) e um Inversor de Frequência (Siemens V90). Na estação 50, este sistemas, são responsáveis pelo movimento do tapete. Para o movimento deste tapete é usado um motor trifasico que acupolado tem um enconder, que, através da sua posição é possivel fazer o encaminhamento das peças, para a posição pretendida. Para a movimento do Motor é uitlizado um Inversor de Frequência (Siemens G120C), que converte o sinal elétrico em sinal analógico sendo assim possivel fazer o movimento do tapete e controlo da velocidade.

Para a comunicação entre as diversas estações é usado o protocolo de comunicação **PROFINET**, este protocolo é baseado em **Ethernet**. No programa TIA Portal é definida uma área de transferência de Bytes, desta forma, tanto o Master com os Slaves podem operar na zona defenida. 

### Peças

![P_1](./images/station/p_1.jpg)

Peças, constituidas por Corpo (Parte Exterior) e por um Miolo (Parte Interior). Representa o objetvo processado na Line32, quando os elementos são unificados representam o produto final. Podem ser classificadas de 9 maneiras, como nos mostra a tabela abaixo.

||Metálico|Branco|Preto|
-| ------ | ---- | --- |
Metálico|**x**|x|x|
Branco|x|**x**|x|
Preto|x|x|**x**|

Os **x** a negrito indicanos a combinações pretendidas, quando esseas combinações são processadas são encaminhadas para o respetivo armazém.

### Estações

**Estação 10**

A Estação 10, **estação de transporte da peça**, desde a sua fase inicial até à sua finalização. 

![ST10](./images/station/st_10.jpg)

**Estação 20**

A Estação 20, **estação de alimentação do corpo da peça**, o corpo da peça, é colocado no funil para ser processado. 

![ST20](./images/station/st_20.jpg)

**Estação 30**

A Estação 30, **estação de aplicação**, é aplicada uma *cola* para fixar o miolo ao corpo da peça. 

![ST30](./images/station/st_30.jpg)

**Estação 40**

A Estação 40, **estação de alimentação do miolo da peça**, o miolo da peça, é colocado na funil para ser processado.  

![ST40](./images/station/st_40.jpg)

**Estação 50**

A Estação 50, **estação de seleção**, responsável por ordenar as peças no respsetivo armazém. 

![ST50](./images/station/st_50.jpg)

### Modo de Funcionamento

Assim que a estação 20 for alimentada com o corpo da peça, essa informação é enviada para o PLC Master (Estação 10), assim que recebida, a peça é processada, ou seja, o cilindro avança e a peça esta pronta para o robô a processar e avançar para a proxima estação. 

Quando o robô estiver na posição realtiva à estação 30, a garra avança e pousa a peça na pinça e a peça é processada, quando concluido este processo o carro avança para a proxima estação. 

Quando o robô estiver na posição realtiva à estação 40, a garra avança e pousa a peça *suporte*. Assim que o corpo da peça for recebido pela estacão 40, a estacão entra em processamento, ou seja, o miolo é colocado no corpo da peça. Quando concluido este processo o carro avança para a proxima estação. 

Quando o robô estiver na posição realtiva à estação 50, a garra avança e pousa a peça no tapete. O tapete entra em funciomaneto, a peça é identificada, pelos sensores e encaminhada. Caso for uma peça pretendida (Metálico/Metálico; Branco/Branco; Preto/Preto) é encaminhada para o respetivo armazém, senão, a peça é rejeitda.

Depois do robô, pousar a pesa no tapete da estação 50, retorna para a sua posição de *home* e desta forma o ciclo foi concluido e pronto a realizar um novo ciclo. 

## Trabalho Realizado
### Classificação
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

### Software
#### Grafcets Modo: Manual
##### Estação 10 (Manual)

![](./software/grafcets/bancada32_manual/19PLC.svg)

##### Estação 20 (Manual)

![](./software/grafcets/bancada32_manual/29PLC.svg)

##### Estação 30 (Manual)

![](./software/grafcets/bancada32_manual/39PLC.svg)

##### Estação 40 (Manual)

![](./software/grafcets/bancada32_manual/49PLC.svg)

##### Estação 50 (Manual)

![](./software/grafcets/bancada32_manual/59PLC.svg)

#### Grafcets Modo: Automático
##### Estação 10 (Automático)

![](./software/grafcets/bancada32_automatico/19PLC.svg)

##### Estação 20 (Automático)

![](./software/grafcets/bancada32_automatico/29PLC.svg)

##### Estação 30 (Automático)

![](./software/grafcets/bancada32_automatico/39PLC.svg)

##### Estação 40 (Automático)

![](./software/grafcets/bancada32_automatico/49PLC.svg)

##### Estação 50 (Automático)

![](./software/grafcets/bancada32_automatico/59PLC.svg)

# Programacao

A programaçáo das Line 32 foi feita usando o programa TIA Portal.

#### Gemma
- [Projeto1](./software/gemma/projeto1/gemma.md)
