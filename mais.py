import pandas as pd
from reportlab.pdfgen import canvas #canvas é um PDF
from reportlab.lib.pagesizes import A4 

table = pd.read_csv("base_dados.csv")
print(table) #printa e ja deixa na tela para facilitar a criação das variaveis referente as colunas

for line in table.index:
  nome  = table.loc[line, "Nome"]
  setor = table.loc[line, "Setor"]
  horas = table.loc[line, "Horas Extras"]
  data  = table.loc[line, "Data"]

  
  arq_pdf = canvas.Canvas(f"Relatorio de horas extras {nome}.pdf ", A4)#o primeiro canvas é a lib o segundo é a CLASSE ----> essa linha vai gerar o arquivo pdf em si

  #seleciona a fonte e o tamanho do TITULO
  arq_pdf.setFont("Helvetica-Bold", 18)
  arq_pdf.drawString(100, 750, f"Relatorio de horas extras {nome}")

  arq_pdf.setFont("Helvetica", 14)
  # parametros dentro () largura, altura, texto em si, ele contra o tamanho de baixo pra cima
  #o eixo Y que representa a altura vai decrementando, ou seja, um abaixo do outro, no caso escoplhi distancia de 30
  arq_pdf.drawString(100, 720, f"Nome : {nome}")
  arq_pdf.drawString(100, 690, f"Setor : {setor}")
  arq_pdf.drawString(100, 660, f"Horas Extras: {horas}")
  arq_pdf.drawString(100, 630, f"Data : {data}")
  arq_pdf.drawString(100, 600, f"Este arquivo foi gerado automaticamente!!!")

  arq_pdf.save()
