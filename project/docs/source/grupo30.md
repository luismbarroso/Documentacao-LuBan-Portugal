# Grupo 30 - YL335B

- [Classificação](#classificação)
  - [Estações](./classification/estacoes.md)
  - [Profinet](./classification/profinet.md)
  - [Modbus](./classification/modbus.md)
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
      - [João Evartisto](https://joaoevaristo-documentacao.readthedocs.io/en/latest/lines/line31/2020_2021/line31.html)
      - [Fábio Santo](https://fabiosanto-documentacao.readthedocs.io/en/latest/lines/line31/2020_2021/line31.html)
    - [2021_2022](./lines/line31/2021_2022/line31.md)
    - [2022_2023](./lines/line31/2022_2023/line31.md) 
  - [Line 32](#line-32)
    - [2020_2021](./lines/line32/2020_2021/line3222.md)
      - [Luís Barroso](https://luisbarroso-documentacao.readthedocs.io/en/latest/line32.html)
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
### [Estações](./classification/estacoes.md)
### [Profinet](./classification/profinet.md)
### [Modbus](./classification/modbus.md)

## Componentes
### Sensor Fotoelétrico
### Sensor Magnético
### Sensor Indutivo
### Sensor Ótico
### Cilindro Pneumático

## Equipamentos
### Enconder

Encoders ou geradores de Impulsos são equipamentos eletromecânicos, utilizados para conversão de movimentos rotativos ou deslocamentos lineares em impulsos elétricos de onda quadrada, que geram uma quantidade exata de impulsos por volta em uma distribuição perfeita dos pulsos ao longo dos 360 graus do giro do eixo. Ao longo deste documento serão abordados os passos de configuração do encoder e como integrar o mesmo num programa.

Os enconders podem ser classificados como **"Encoder Relativos"** ou **"Encoder Absoluto"**. **"Encoder Relativos"**, dizem-nos a posição relativa ao ponto onde o encoder foi
ativado, normalmente possuem 3 saídas A, B e Z. **"Encoder Absolutos"**, dizem-nos a posição absoluta através de saídas digitais codificadas em um valor binário.

#### - [Manual Enconder](./equipments/manuais/manual_enconder.md)

### Servo Motor

Um Servo Motor, é um equipamento eletrónico utilizado como um atuador em sistemas de controlo automático, ele converte sinais elétricos num movimento angular no veio do motor. Na
Oficina Luban, mais especificamente no Grupo 30 (YL-335B), o Servo Motor esta ligado a um Motor AC SIMOTICS S-1FL6 que permite a deslocação do carro.

#### - [Manual Servo Motor](./equipments/manuais/manual_servo.md)

### Inversor de Frequência

Um Inversor de Frequência é um equipamento eletrónico, u
ªtilizado para variar a velocidade de um motor. Este equipamento transforma o Sinal Analógico, vindo do PLC, em corrente alternada. Na Oficina Luban, mais especificamente no Grupo 30 (YL-335B), o Inversor de Frequência esta ligado a um Motor Triásico e a este está acoplado um Enconder que permite as seleção das peças de forma correta e precisa. 

### Siemens S7 1200

## Lines
### Line 31
#### 2020_2021
- [João Evartisto](https://joaoevaristo-documentacao.readthedocs.io/en/latest/lines/line31/2020_2021/line31.html)
- [Fábio Santo](https://fabiosanto-documentacao.readthedocs.io/en/latest/lines/line31/2020_2021/line31.html)
#### 2021_2022
#### 2022_2023

### Line 32
#### 2020_2021
- [Luís Barroso](https://luisbarroso-documentacao.readthedocs.io/en/latest/line32.html)
#### 2021_2022
#### 2022_2023

### Line 33
#### 2020_2021
#### 2021_2022
#### 2022_2023

## Software
### TIA Portal
[TIA Portal](https://new.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal.html), Totally Integrated Automation Portal, desenvolvido pela
Siemens é um software que oferece uma vasta gama ferramentas, desta forma é possivel realizar o trabalho de forma rapida e eficaz. Intregado ao TIA Portal temos o WinCC, a ferramenta
utilizada para a programação das HMI's na Ofina Luban.

### Tesla Scada
[Tesla Scada](https://teslascada.com/), foi o software escolhido para implementação de interfaces homem-máquina na Oficina Luban. O Tesla Scada permite o controlo e supervisão em
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
