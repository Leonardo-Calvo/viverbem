from flask import Flask
from flask import request
from flask import render_template
from datetime import date
import sqlite3
from sqlite3 import Error


app = Flask(__name__)

@app.route("/")
def pagina_principal():
  return render_template("home.html")

@app.route("/imc", methods=["GET", "POST"])
def pagina_imc():
    imc = None
    classificacao = ""
    imagem = ""
    descricao = ""

    if request.method == "POST":
        try:
            peso = float(request.form["peso"].replace(",", "."))
            altura = float(request.form["altura"].replace(",", "."))
            imc = round(peso / (altura ** 2), 1)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
                imagem = "images/imc_classificacao/imc_abaixo.png"
                descricao = "Procure um médico. Algumas pessoas têm um baixo peso por características" \
                " do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição." \
                " É preciso saber qual é o caso."
            
            elif 18.5 <= imc < 24.9:
                classificacao = "Peso normal"
                imagem = "images/imc_classificacao/imc_normal.png"
                descricao = "Que bom que você está com o peso normal! E o melhor jeito de continuar assim" \
                " é mantendo um estilo de vida ativo e uma alimentação equilibrada."
           
            elif 25 <= imc < 29.9:
                classificacao = "Sobrepeso"
                imagem = "images/imc_classificacao/imc_acima.png"
                descricao = "Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam " \
                "doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar" \
                " ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer."
           
            elif 30 <= imc < 39.9:
                classificacao = "Obesidade"
                imagem = "images/imc_classificacao/imc_obesidade.png"
                descricao = "Mesmo que seus exames aparentem estar normais, é hora de se cuidar," \
                " iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde."
           
            else:
                classificacao = "Obesidade grave"
                imagem = "images/imc_classificacao/imc_obesidade_grave.png"
                descricao = "Aqui o sinal é vermelho, com forte probabilidade de já existirem " \
                "doenças muito graves associadas. O tratamento deve ser ainda mais urgente."

        except:
            imc = None

    return render_template("imc.html", imc=imc, classificacao=classificacao, imagem=imagem, descricao=descricao)


@app.route("/tmb", methods=["GET", "POST"])
def pagina_tmb():
    resultado = None
    if request.method == "POST":
        sexo = request.form["sexo"]
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        idade = int(request.form["idade"])

        if sexo == "homem":
            resultado = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        elif sexo == "mulher":
            resultado = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

        resultado = round(resultado, 2)

    return render_template("tmb.html", resultado=resultado)

#=====================RECEITAS===================================================================#
@app.route('/receitas')
def pagina_receitas():
    return render_template('receitas.html')

@app.route('/receitas/almoco')
def receitas_almoco():
    return render_template('almoco.html')

@app.route('/receitas/cafe')
def receitas_cafe():
    return render_template('cafe.html')  

@app.route('/receitas/doces')
def receitas_doces():
    return render_template('doces.html')

@app.route('/receitas/bebidas')
def receitas_bebidas():
    return render_template('bebidas.html')

#=====================RECEITAS===================================================================#

#=====================Exercicios===================================================================#
@app.route("/exercicios")
def pagina_exercicios():
  return render_template("exercicios.html")

@app.route("/exercicios/peito")
def exercicio_peito():
  return render_template("peito.html")

@app.route("/exercicios/costa")
def exercicio_costa():
  return render_template("costas.html")

@app.route("/exercicios/perna")
def exercicio_perna():
  return render_template("perna.html")

@app.route("/exercicios/aerobico")
def exercicio_aerobico():
  return render_template("aerobico.html")


#=====================Exercicios===================================================================#

@app.route("/sobre")
def pagina_sobre():
  return render_template("sobre.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


app.run(debug= True)

