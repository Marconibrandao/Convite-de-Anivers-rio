from cgitb import text
from email.mime import image
from tkinter import LEFT, font
from typing import Text
from PIL import Image, ImageDraw, ImageFont

CONVIDADOS = ["Nome do Convidado" ]

LEFT_BORDER = 100

font1 = ImageFont.truetype("./GreatVibes-Regular.ttf", size = 35) #./font1.ttf, size=35
font2 = ImageFont.truetype("./GreatVibes-Regular.ttf", size = 20) #./font2.ttf, size=35
font3 = ImageFont.truetype("./GreatVibes-Regular.ttf", size = 25)

for convidado in CONVIDADOS:

    imagem = Image.open("./imagem para o convite de melissa.png").convert("RGBA")
    lapis = ImageDraw.Draw(imagem)

    lapis.text(
            (125, 100),
            text=f"Olá {convidado}",
            fill="#000",
            font=font1
    )

    lapis.line(
        (LEFT_BORDER, 145, 279, 145), #
        fill="#ccc",
        width=5
    
    )

    lapis.text(
        (LEFT_BORDER, 160),
        text="Venha ao meu aniversário",
        fill="#000",
        font=font1,

    )

    lapis.text(
        (LEFT_BORDER, 200),
        text="Dia: dd/mm/aa",
        fill="#000",
        font=font1

    )
    lapis.text(
        (75, 240),
        text = "as xx horas, na Rua Xxxxxx,",
        fill = "#000",
        font = font2
    )

    lapis.text(
        (70, 260),
        text = "nº x, endereço tal",
        fill = "#000",
        font = font2
    )

    lapis.text(
        (LEFT_BORDER, 310),
        text="Abraços!",
        fill="#000",
        font=font1

    )
    lapis.text(
        (LEFT_BORDER, 360),
        text="Nome do Aniversariante",
        fill="#000",
        font=font3

    )

    imagem.save(f"/home/marconi/Imagens/convite_{convidado}.png")