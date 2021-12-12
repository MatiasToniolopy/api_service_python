
from flask import Flask, send_file, render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as sql


conn = sql.connect('personas.db')
cursor = conn.cursor()

data = cursor.execute('SELECT * FROM persona')

#edad
x = [x[2] for x in data]

data2 = cursor.execute('SELECT * FROM persona')

#ritmo cardiaco
y = [x[3] for x in data]

conn.close()


fig,ax = plt.subplots(figsize=(6,6))
ax = sns.set_style(style='darkgrid')



#ruta al grafico
app = Flask(__name__)

@app.route('/')

def principal():
    return render_template("graf.html")


@app.route('/visual')
def visual():
    sns.barplot(x,y)
    plt.title('RITMO CARDIACO BASADO EN DIFERENTES EDADES', color='red')
    plt.xlabel('EDADES', color='blue')
    plt.ylabel('RITMO CARDIACO', color='blue')
    FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')
    
    

    
 
  
    
    



if __name__ == '__main__':
    app.run(debug=True, port=5000)    



