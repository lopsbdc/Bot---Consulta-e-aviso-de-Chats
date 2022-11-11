# Bot---Consulta-e-aviso-de-Chats
Bot para consultar chats em aberto em um sistema interno da empresa, e avisar colaboradores sobre o atendimento pelo Google Chat.

O bot foi feito como "função" para evitar repetição de código, visando consultar o chat de diversos departamentos da empresa.
O bot consulta no sistema interno, e verifica a quantidade de atendimentos, em loop. Depois, caso exista algum atendimento em aguardo, ele realiza o login no email e avisa através de um grupo no google chat.

Atualmente está hospedado em uma VBS Linux, na Cloud, executando 24/7.
