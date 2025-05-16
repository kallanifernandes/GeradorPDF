# 🕒 Relatório de Horas Extras por Funcionário

Projeto em Python que automatiza a geração de **relatórios individuais em PDF** com base em um arquivo `.CSV` contendo informações de funcionários, seus setores, quantidade de horas extras e o período (mês/ano). Ideal para análises estratégicas e tomadas de decisão por parte da alta gestão.

---

## 📌 Objetivo

O objetivo é facilitar o controle de horas extras por funcionário e setor, permitindo uma visão clara sobre a **distribuição da carga de trabalho** na empresa. Com isso, a gestão pode:

- Identificar sobrecarga em setores específicos
- Avaliar a necessidade de contratação ou redistribuição de tarefas
- Tomar decisões baseadas em dados reais

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- [`pandas`](https://pandas.pydata.org/) — para leitura e manipulação do CSV
- [`reportlab`](https://www.reportlab.com/) — para criação dos arquivos PDF
- [`faker`](https://faker.readthedocs.io/) — para gerar dados fictícios nos testes

---

## 📂 Estrutura dos dados

O arquivo CSV deve conter as seguintes colunas:

| Nome          | Setor         | Horas Extras | Data    |
|---------------|---------------|---------------|---------|
| João da Silva | Financeiro    | 12            | 03/2025 |
| Ana Souza     | RH            | 8             | 03/2025 |

> A coluna **Data** deve estar no formato `MM/AAAA`.

---

## 🚀 Como executar o projeto

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
