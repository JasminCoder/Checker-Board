from flask import Flask, render_template

app = Flask(__name__)


#Haz que la ruta raíz renderice una plantilla con un tablero de ajedrez (8x8)
@app.route('/')
def tablero():
    return render_template("index.html", num=8, num2=8, color1="purple", color2="turquoise") 



#Haz que otra ruta acepte un solo parámetro (es decir, "/") y renderiza un tablero de ajedrez con x cantidad de filas, con colores alternos
@app.route('/4')
def tablero_dos():
    return render_template("index.html", num=4, num2=8, color1="aqua", color2="black")



#BONUS NINJA: Haz que otra ruta acepte 2 parámetro (es decir, "//") y renderiza un tablero de ajedrez con x filas e y columnas Las columnas, con colores alternos
@app.route('/<int:numero>/<int:number>')
def tablero_tres(numero, number):
    return render_template("index.html", num=numero, num2=number, color1="yellow", color2="antiquewhite")



#BONUS SENSEI: Haz que otra ruta acepte 4 parámetro (es decir, "////") y renderiza un tablero de ajedrez con x filas e y 
#columnas, con colores alternos, color1 y color2
@app.route('/<int:numero>/<int:number>/<string:color1>/<string:color2>')
def tablero_cuatro(numero, number, color1, color2):
    return render_template("index.html", num=numero, num2=number, color1=color1, color2= color2)


if __name__=="__main__":
    app.run(debug=True)

