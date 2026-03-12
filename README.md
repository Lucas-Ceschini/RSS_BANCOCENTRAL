# RSS Banco Central – Automação de Coleta e Monitoramento de Notícias Econômicas

## Descrição do Projeto
Este projeto consiste em um **pipeline automatizado para captura, processamento e distribuição de informações econômicas do Banco Central do Brasil**, utilizando **feeds RSS públicos**. O objetivo é **coletar informações relevantes de indicadores econômicos, decisões de política monetária e comunicados oficiais**, disponibilizando alertas e relatórios estruturados para análise e suporte à tomada de decisão.

---

## Objetivos
- Automatizar a coleta de notícias e comunicados oficiais do Banco Central do Brasil via **RSS feeds**.  
- Estruturar e consolidar os dados em **formatos legíveis e analisáveis** (CSV, banco de dados SQL).  
- Enviar notificações automatizadas para equipes de análise ou alta gestão sobre eventos relevantes.

---

## Arquitetura e Fluxo do Pipeline
1. **Coleta**  
   - Captura de feeds RSS do Banco Central em intervalos regulares (ex.: diário ou horário específico).  
   - Extração de campos como título, data, link e descrição.  

2. **Processamento e Limpeza**  
   - Normalização de texto, remoção de caracteres especiais e padronização de datas.  
   - Filtragem de conteúdos duplicados ou irrelevantes.  

3. **Armazenamento**  
   - Estruturação dos dados em **banco MySQL**, permitindo consultas rápidas e histórico completo.  
   - Alternativamente, exportação para **CSV** ou integração com **Power BI/Tableau** para visualização.  

4. **Distribuição e Alertas**  
   - Notificação automatizada via e-mail ou Slack para novos comunicados críticos.  
   - Possibilidade de gerar **dashboards interativos** com indicadores de frequência e impacto das notícias.  

---

## Tecnologias Utilizadas
- **Python:** Requests, feedparser, pandas
- **Banco de Dados:** SQLite (protótipo)
- **Automação:** Scripts agendados (cron jobs ou Airflow para pipelines escaláveis)  
- **Visualização/Integração:** Envio dos dados via e-mail

---
