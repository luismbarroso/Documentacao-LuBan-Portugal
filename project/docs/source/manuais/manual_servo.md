<div align="center">
  <img src="../../source/manuais/logos/Logo_Luban.png" width="80" />   
  <img src="../../source/manuais/logos/Logo_IPS.jpg" width="110" /> 
</div>
<div align="center">
  <h2> IPS - Escola Superior de Tecnologia de Setúbal - Lu Ban Workshop Portugal </h2>
</div>
 ⠀ 
  ⠀ 

# Manual Servo Motor

**Autor:** ...

<img src="../../source/manuais/logos/Logo_IPS.jpg" width="80" />  

### Indice
- [Básico I](#basico-i)
- [Servos na Oficina Luban](#servos-na-oficina-luban)	
- [Configuração Básica do Servo com PTO](#configuracao-basica-do-servo-com-pto)	
    - [Noções sobre Pulse Train Output (PTO)](#nocoes-sobre-pulse-train-output-pto)
    - [Configurar servo no TIA Portal V15](#configurar-servo-no-tia-portal-v15)	
    - [Configuração Básica do Servo em PROFINET](#configuracao-basica-do-servo-em-profinet)
- [Noções sobre sobre o servo para PROFINET](#nocoes-sobre-o-servo-para-profinet)
    - [Configurar definições PROFINET no SINAMICS V-ASSISTANT](#configurar-definicoes-profinet-no-sinamics-v-assistant)
    - [Configurar definições PROFINET no TIA Portal V15](#configurar-definicoes-profinet-no-tia-portal-v15)	
    - [Configurar o servo com PROFIdrive no TIA Portal V15](#configurar-o-servo-com-profidrive-no-tia-portal-v15)
- [Introdução aos comandos de controlo de movimento](#introducao-aos-comandos-de-controlo-de-movimento)
    - [MC_Power](#mc-power)
    - [MC_Home](#mc-home)
    - [MC_Reset](#mc-reset)
    - [MC_Halt](#mc-halt)
    - [MC_MoveJog](#[mc-movejog)
    - [MC_MoveAbsolute](#mc-moveabsolute)   
    - [MC_MoveRelative](#mc-moverelative)
- [Axis Error](#axis-error)
    - [Resolução](#resolucao)

### Básico I

Durante esta primeira parte será ensinado o básico sobre o servo. Desde as bases de configuração até às bases de programação, abordando apenas a informação essencial para
conseguir por em prática uma ideia implementando um servo no processo. Serão ainda abordados alguns conceitos básicos em relação ao servo e ao método de comunicação
utilizado (PTO). 

### Servos na Oficina Luban

Um servo é utilizado como um atuador em sistemas de controlo automático, ele converte sinais elétricos num movimento angular no veio do motor. 

Os servos utilizados nas estações YL-335B (Linha de Produção Automática) na oficina Luban são da Siemens, mais especificamente um motor AC SIMOTICS S-1FL6 e um drive
SINAMISC V90 utilizados para a locomoção do “robô” manipulador de transporte. 

### Configuração Básica do Servo com PTO
#### Noções sobre Pulse Train Output (PTO)	

O CPU dos autómatos disponibilizam quatro saídas geradoras de pulsos, cada saída dessas disponibiliza uma saída para os pulsos e outra saída para direção que permite
controlar o servo através da interface de pulsos. As saídas de pulso proporcionam ao drive do servo o pulso necessário para o movimento do motor. 

As saídas PTO geram ondas quadradas de frequência variável que permitem especificar a velocidade a que o motor se irá mover, sendo estes pulsos gerados com base na
informação fornecida durante a configuração do servo no TIA Portal. 

#### Configurar servo no TIA Portal V15

1.Na aba **“Technology objects”** clique em  **“Add new object”.**

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/1.png" width="650" />
  
  <i>Imagem 1</i>
</div>

2.No menu **“Motion Control”** na pasta **“Motion Control”** selecione **“TO_PositioningAxis”**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/2.png" width="650" />
  
  <i>Imagem 2</i>
</div>

3.Na janela de configuração do Eixo, em **“General”** altere o nome do servo em **“Axis name”**, selecione o método de controle PTO favorecido pelo método de instalação do
drive no PLC e nas unidades de medida em **“Position Unit”** escolha **“mm”** (milímetros).

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/3.png" width="650" />
  
  <i>Imagem 3</i>
</div>

4.No menu lateral **“Drive”**, escolha um dos geradores de pulsos disponíveis em **“Pulse generator”** e de seguida certifique-se que as saídas de pulso e de direção estão
ligadas ao drive.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/4.png" width="650" />
  
  <i>Imagem 4</i>
</div>

5.Em **“Mechanics”** no menu lateral serão colocados alguns valores parametrizados pelos equipamentos ou valores obtidos através de uma calibração. Para os servos do
laboratório podem ser usados os valores na (Imagem 5).

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/5.png" width="650" />
  
  <i>Imagem 5</i>
</div>

6.Em relação aos limites de posição ative a opção **“Enable HW limit switches”** e opcionalmente **“Enable SW limit switches”**. Insira as entradas de alta (para valores de
medida máximos) e de baixa (para valores de medida mínimos) e selecione em ambos a opção **“High level”** para que o servo dispare a paragem de emergência quando um dos fins
de curso seja acionado.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/6.png" width="650" />
  
  <i>Imagem 6</i>
</div>

7.**(Opcional)** Em **“Dynamics”** todos os valores poderão ser escolhidos pessoalmente tendo em conta a segurança das pessoas ao seu redor, a integridade do equipamento e o
que se pretende para o processo.

8.Em **“Homing - Active”** selecionaremos a entrada do sensor referente à posição home, escolha **“Negative direction”**, ative **“Permit auto reverse at HW limit switch”**
e calibre as velocidades.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_pto_tia_portal_v15/8.png" width="650" />
  
  <i>Imagem 7</i>
</div>

9.E a configuração do Servo está concluída.

### Configuração Básica do Servo em PROFINET
#### Noções sobre sobre o servo para PROFINET

Para o funcionamento do SINAMICS V90 PN no modo “Speed Control (S)”, a seguinte lista de telegrams são suportados:

- Standard telegram 1
- Standard telegram 2
- Standard telegram 3
- Standard telegram 5
- Standard telegram 102
- Standard telegram 105

O standard telegram 1 só pode ser usado em modo **“Real-time”** (RT mode). Os standard telegram 2, 3 e 102 podem ser usados tanto em modo RT ou em modo **“Isochronous
Real-time”** (IRT mode), dependendo do controlador I/O. Os standard telegrams 5 e 105 apenas
suportam o modo IRT e só podem ser usados com TIA Portal V14.

Os telegrams 1, 2 e 102 são usados para controlo de velocidade do eixo enquanto os telegrams 3, 5 e 105 são usados para posicionamento do eixo pois estes telegrams possuem a
**“Posição atual”** do encoder (Gn_XIST1).

Se usado um SIMATIC S7-1200 para controlo de posição então TO (Technology Object) Positioning Axis terá de ser usado. O **“TO Positioning Axis”** apenas suporta os telegram
1, 2 e 3.

    NOTA: SIMATIC S7-1200 apenas suporta comunicação em modo RT.

#### Configurar definições PROFINET no SINAMICS V-ASSISTANT

1.Abra o **SINAMICS V-ASSISTANT** e certifique-se de que tem o drive a configurar ligado ao PC via USB.

2.Clique em online, selecione o equipamento a configurar e clique em **“Ok”**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/2.png" width="650" />
  
  <i>Imagem 8</i>
</div>

3.Na aba **“Select drive”** clique no botão **“Select motor”**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/3.png" width="650" />
  
  <i>Imagem 9</i>
</div>

4.No menu de seleção do motor, escolha a opção cujo **“Motor ID”** corresponda ao seu motor. 

    NOTA: O ID do motor pode ser encontrado na placa de identificação no motor.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/4.png" width="650" />
  
  <i>Imagem 10</i>
</div>

5.De seguida na aba **“Set PROFINET”** em **“Select telegram”** escolha em **“The current telegram”** o telegram adequado às suas necessidades. 

    NOTA: Para melhor entender desta fase leia as “Noções sobre o servo para PROFINET”.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/5.png" width="650" />
  
  <i>Imagem 11</i>
</div>

6.Ainda em **“Set PROFINET”** vá a **“Configure network”** e modifique o nome de identificação do equipamento e o seu respetivo IP para a rede. Clique por fim no botão *
“Save and active”**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/6.png" width="650" />
  
  <i>Imagem 12</i>
</div>

7.Concluídos os passos anteriores, va na barra superior do V-ASSISTANT, em “Tools” clique **"Restart Drive”**. E fica concluída a primeira fase da configuração.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_v-assistant/7.png" width="650" />
  
  <i>Imagem 13</i>
</div>

#### Configurar definições PROFINET no TIA Portal V15

1.Em **“Network view”** clique na barra lateral **“Hardware catalog”**, clique em **“Other field devices > Other field devices > PROFINET IO > Drives > SIEMENS AG > SINAMICS
** e dê duplo-clique sobre **“SINAMICS V90 PN V1.0”**

    NOTA: O mesmo terá de aparecer em “Network view” como no exemplo.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/1.png" width="650" />
  
  <i>Imagem 14</i>
</div>

2.Dê duplo-clique sobre o V90 na **“Network view”** e na janela do dispositivo clique no menu lateral **“Hardware catalog”** e em **“Submodules”** e dê um duplo-clique sobre
o telegram escolhido durante a configuração do V90 com o V-ASSISTANT.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/2.png" width="650" />
  
  <i>Imagem 15</i>
</div>

3.Ainda na janela do dispositivo clique com o botão direito no mesmo e clique em **"Properties"**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/3.png" width="650" />
  
  <i>Imagem 16</i>
</div>

4.Em **"General"**, nomeie o dispositivo com o mesmo nome dado durante a configuração no V-ASSISTANT.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/4.png" width="650" />
  
  <i>Imagem 17</i>
</div>

5.Em **"PROFINET Interface** > **Ethernet addresses"** coloque o endereço de IP  máscara configurados com o V-ASSISTANT. Desmarque a opção **"Generate PROFINET device name
automatically"**  e novamente coloque o nome dado ao dispositivo durante a configuração no
V-ASSISTANT.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/5.png" width="650" />
  
  <i>Imagem 18</i>
</div>

6.Clique novamente sobre o dispositivo V90 e clique na opção **"Assign device name"**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/6.png" width="650" />
  
  <i>Imagem 19</i>
</div>

7.Clique em **"Update list"** e de seguida clique sobre o dispositivo a configurar e clique no botão **"Assign name"**.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/7.png" width="650" />
  
  <i>Imagem 20</i>
</div>

8.Na **"Network view"** ligue o V90 ao PLC.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/8.png" width="650" />
  
  <i>Imagem 21</i>
</div>

9.Em **"Topology view"** ” refaça o desenho das ligações físicas entre o PLC e o V90. No exemplo a ligação entre os dois foi feita com um switch pelo que o mesmo teve de ser
devidamente adicionado. 

    NOTA: Este passo é muito importante, sem ele o dispositivo poderá não funcionar corretamente. Tome também atenção à portas nas ligações entre o PLC e o V90.

<div align="center">
  <img src="../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/9.png" width="650" />
  
  <i>Imagem 22</i>
</div>

10.E a configuração do servo em PROFINET está concluída.

#### Configurar o servo com PROFIdrive no TIA Portal V15

1. No menu lateral de dispositivos em **"Technology Objects"** clique em **"Add new** **object"**.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/10.png" width="650" />
  
  <i>Imagem 23</i>
</div>

2. Em **"Motion control"** clique sobre **"TO_PositioningAxis"**, em name coloque o nome para esse eixo (para facilitar dê-lhe o mesmo nome dado ao servo) e clique **"OK”**.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/11.png" width="650" />
  
  <i>Imagem 24</i>
</div>

3. Em **“General”** escolha a opção **"PROFIdrive"**.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/12.png" width="650" />
  
  <i>Imagem 25</i>
</div>

4. Em **"Drive"** clique nos **"..."** e escolha o drive configurado.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/13.png" width="650" />
  
  <i>Imagem 26</i>
</div>

5. Em **"Encoder"** marque a opção **"Encoder on PROFINET/PROFIBUS"**. E de seguido no campo a vermelho clique nos **"..."** e selecione o **"Encoder1"**.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_profinet_tia_portal_v15/14.png" width="650" />
  
  <i>Imagem 27</i>
</div>

6. **(Opcional)** Em **"Position limits"** ative os **"Limit switcher"** que pretende usar e configure os seus valores/entradas.

7. **(Opcional)** Em **"Homing"** configure o tipo de homing a usar e o respetivo switch de homing.

8. E fica concluída a configuração do servo.

### Introdução aos comandos de controlo de movimento

Para programação do Servo o TIA Portal disponibiliza um conjunto de blocos (sub-rotinas) de controlo de movimento que permitem integrar de forma fácil e prática o servo ao
nosso processo.

#### MC_Power

**MC_Power** – é uma função que deve ser chamada e ligada antes de qualquer instrução de movimento, sem ela não será possível comando o servo.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/1.png" width="650" />
  
  <i>Imagem 28</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Enable:** Entrada do sinal que irá ligar o servo

#### MC_Home

**MC_Home** – é a função responsável de levar o servo até ao local onde está situado o sensor configurado para “homing”, a sua posição inicial.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/2.png" width="650" />
  
  <i>Imagem 29</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Execute:** Entrada do sinal que irá ditar a ordem de movimento do servo
- **Position:** Valor absoluto da localização do servo, após ter chegado à posição home (coordenada absoluta de home)
- **Mode:** Permite escolher entre os diferentes tipos de **“homing”**

#### MC_Reset

**MC_Reset** – é a função que permite ignorar erros causados pela paragem do servo ao entrar em contacto com um fim de curso ou erros de configuração.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/3.png" width="650" />
  
  <i>Imagem 29</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Enable:** Entrada do sinal que irá ditar a ordem de reset

#### MC_Halt

**MC_Halt** – é a função que para os movimentos do servo.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/4.png" width="650" />
  
  <i>Imagem 29</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Enable:** Entrada do sinal que irá parar o servo

#### MC_MoveJog

**MC_MoveJog** – é uma das funções de movimento do servo, esta em especifico permite que o servo se mova enquanto uma das entras permaneça ativa.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/5.png" width="650" />
  
  <i>Imagem 30</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **JogForward:** Move o servo para coordenadas superiores
- **JogForward:** Move o servo para coordenadas inferiores
- **Velocity:** Velocidade com a qual o servo executará os movimentos

#### MC_MoveAbsolute

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/6.png" width="650" />
  
  <i>Imagem 31</i>
</div>

**MC_MoveAbsolute** – é a função responsável por levar o servo até uma posição absoluta através de uma coordenada.

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Execute:** Entrada do sinal que irá ditar a ordem de movimento do servo
- **Position:** Coordenada absoluta para a qual o servo se irá mover
- **Velocity:** Velocidade com a qual o servo executará o movimento

#### MC_MoveRelative

**MC_MoveRelative** – é a função responsável por mover o servo uma determinada distancia relativamente à sua atual coordenada.

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_programacao/7.png" width="650" />
  
  <i>Imagem 32</i>
</div>

**Principais parâmetros:**
- **Axis:** Nome do servo/eixo configurado
- **Execute:** Entrada do sinal que irá ditar a ordem de movimento do servo
- **Distance:** Distancia do ponto de referencia a qual o servo de moverá
- **Velocity:** Velocidade com a qual o servo executará o movimento

### Axis Error

Assim que o servo dispara a paragem de emergência quando um dos fins de curso é acionado, é necessario remover a emergência usado os blocos **"MC_Power"** e **"MC_Reset"** anteriomente explicados.

#### Resolução

1.Assim que um dos fins de curso é acionado, consulte o **"Status"** do Axis, clique em "**Technology objects > Axis > Diagnostics** e dê duplo-clique sobre **“Status and error bits”**

    NOTA: Para sabermos o estado do Axis é necessário clicar em "Monitor All"

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/1.png" width="650" />
  
  <i>Imagem 33</i>
</div> 

2.Para remover o **"Axis Error"** é necessário fazer o **"Disable"** no bloco **"MC_Power"**. Após o fazer volte ao **Diagnostics** e deve obter o resutlado apresentado na **"Figura 35"**

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/2.png" width="400" /> <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/3.png" width="400" />
  
  <i>Imagem 34/35</i>
</div> 

3.Com o **"disable"** feito, no bloco **"MC_Reset"**, faça o **"Execute"**. Após o fazer volte ao **Diagnostics** e deve obter o resutlado apresentado na **"Figura 37"**

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/4.png" width="400" /> <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/5.png" width="400" />
  
  <i>Imagem 36/37</i>
</div> 

4.Com o **"Disable"** do **"Axis Error"** e do **"HW limit switch has been aprroached"** no **“Status and error bits”** e necessário fazer o **"Reset"** ao **"Servo-Motor"**. Atualmente o Servo-Motor deve estar no estado apresentado na Imagem 38 *(COM - Luz Vermelha Permanente; RDY - Luz Vermelha a Piscar)*. Para fazer o **"Reset"** é necessário carregar nos botões **"M"** **"Ok"** em simultâneo, durante 5 segundos, desta forma, o *COM - Desliga; e o RDY - Luz Laranja Permanente*. Assim que o *COM - Luz Vermelho Permanente e o RDY - Luz Verde Permanente* o servo motor encontra-se sem erros.

    NOTA: Ativar o "Enable" no bloco "MC_Power"

<div align="center">
  <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/6.jpg" width="200" /> <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/7.jpg" width="200" />
  
  <i>Imagem 38/39</i>

  <img src="../../../source/manuais/manual_servo_imagens/img_erros_axis/8.png" width="650" /> 
  
  <i>Imagem 40</i>
</div> 
