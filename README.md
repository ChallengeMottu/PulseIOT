# 🚀 Pulse — Onde a Eficiência Encontra a Velocidade

O **Pulse** é uma solução desenvolvida para automatizar e otimizar a gestão dos pátios de motos da **Mottu**, que depende diretamente do controle eficiente de seus veículos. A proposta integra tecnologias físicas e digitais para garantir **rastreamento em tempo real** e **alocação inteligente** das motos.

A tecnologia central utilizada é o **Beacon BLE (Bluetooth Low Energy)**, especificamente o modelo **nRF52810**, da **Nordic Semiconductor**.  
Esses dispositivos são instalados nas motos e emitem sinais com identificadores únicos, permitindo que o sistema reconheça automaticamente cada veículo ao entrar no pátio.

✅ **Por que o nRF52810?**  
- Eficiência energética  
- Custo acessível (R$ 25 a R$ 60 por unidade)  
- Compatibilidade com **Bluetooth 5.0**, ideal para aplicações de rastreamento  

---

## 🖥️ Funcionalidades da Plataforma

A plataforma inclui uma interface web conectada ao backend, oferecendo as seguintes funcionalidades:

- 🔍 **Identificação automática** das motos
- 📍 **Sugestão inteligente** da melhor zona de alocação no pátio
- 🗺️ **Visualização em tempo real** do pátio com mapa interativo
- 📊 **Dashboard com indicadores** e integração com **câmeras de segurança**

O **Pulse** assegura **eficiência**, **rastreabilidade** e **segurança**, sendo uma solução prática, escalável e alinhada ao cenário tecnológico atual.

---

## 📡 Identificação dos Beacons nos Pátios

Além dos celulares utilizados pelos colaboradores para acessar a interface web do Pulse, o sinal Bluetooth emitido pelos **Beacons** será captado por **Gateways BLE** estrategicamente posicionados nos pátios.

---

## 🔧 Simulação IoT

Para demonstrar como a captação do sinal dos Beacons funciona, realizamos uma simulação utilizando:

- O aplicativo **nRF Connect**, que cria um **"Fake Beacon"**, emitindo sinais Bluetooth e dados numéricos equivalentes aos que um Beacon físico enviaria.
- Um código desenvolvido em **Python**, responsável por capturar e exibir apenas os sinais de Beacons do modelo **nRF52810**, da **Nordic Semiconductor**.

---

## ▶️ Como Executar o Código Python?

Para rodar o código de scanner dos Beacons, execute o comando no terminal:

```bash
python scanner.py
```

## ✅ Resultados obtidos
- É possível filtrar e identificar com precisão apenas os Beacons do modelo escolhido.
- A tecnologia Beacon BLE é eficaz para resolver o problema de identificação e organização das motos nos pátios.
- A estrutura proposta garante uma captação confiável de todas as motos presentes no espaço, promovendo agilidade e controle operacional.

## 👥  Grupo Desenvolvedor
- Gabriela de Sousa Reis - RM558830
- Laura Amadeu Soares - RM556690
- Raphael Lamaison Kim - RM557914 
