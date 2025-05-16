# 🕒 Relatório de Horas Extras por Funcionário

Esse projeto foi feito com o objetivo de automatizar a geração de **relatórios individuais em PDF** a partir de um arquivo `.CSV`, contendo dados como nome do colaborador, setor, quantidade de horas extras e o mês/ano. A ideia é transformar um processo manual em algo prático, rápido e com potencial de uso real dentro das empresas.

---

## 📌 Qual a proposta?

Ter controle sobre as horas extras por setor e por funcionário é algo essencial para qualquer empresa que deseja crescer com organização. Com esse projeto, é possível:

- Ver quais setores estão sobrecarregados
- Analisar se há necessidade de contratar ou redistribuir tarefas
- Tomar decisões baseadas em dados e não apenas em achismos

O projeto não só gera relatórios individuais, como também prepara os dados para uma análise geral, permitindo identificar padrões com muito mais clareza.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.10+**
- [`pandas`](https://pandas.pydata.org/): para ler e tratar os dados do CSV
- [`reportlab`](https://www.reportlab.com/): para gerar os arquivos PDF automaticamente
- [`faker`](https://faker.readthedocs.io/): usei essa biblioteca para gerar dados fictícios e testar o projeto

---

## 🗂️ Estrutura esperada do CSV

O arquivo `.csv` precisa ter essas quatro colunas:

| Nome          | Setor      | Horas Extras | Data    |
| ------------- | ---------- | ------------ | ------- |
| João da Silva | Financeiro | 12           | 03/2025 |
| Ana Souza     | RH         | 8            | 03/2025 |

📌 **Importante:** A coluna `Data` deve seguir o formato `MM/AAAA` (sem dia).

---

## 🚀 Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/kallanifernandes/GeradorPDF.git
cd GeradorPDF
```
