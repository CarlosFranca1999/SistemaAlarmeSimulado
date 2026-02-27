# SistemaAlarmeSimulado
SistemaSimuladoIOT
🔐 Sistema de Alarme IoT (Simulado com Flask)

Aplicação web desenvolvida em Python + Flask que simula um sistema de alarme IoT com sensor de movimento (PIR), LED indicador e relé (alarme sonoro). A interface é moderna, responsiva e atualizada automaticamente.

🚀 Tecnologias

Python 3

Flask

HTML5 + CSS3

Random (simulação do sensor)

Datetime (registro de eventos)

⚙️ Funcionalidades

🚶 Sensor PIR Simulado – Gera detecção de movimento aleatória.

💡 LED Indicador – Liga quando há movimento.

🔔 Relé / Alarme – Ativado quando o sistema detecta movimento.

🔄 Ativar / Desativar Alarme – Controle via rota /toggle.

📜 Histórico de Eventos – Armazena os últimos 10 horários de detecção.

🔁 Atualização automática a cada 2 segundos.

📂 Estrutura do Projeto /projeto │ ├── app.py ├── templates/ │ └── index.html └── README.md ▶️ Como Executar

Instale o Flask:

pip install flask

Execute o projeto:

python app.py

Acesse no navegador:

http://127.0.0.1:5000

Ideal para projetos acadêmicos e demonstrações de IoT.
