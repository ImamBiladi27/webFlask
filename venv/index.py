from flask import Flask, render_template,request
import mysql.connector
app = Flask(__name__)
@app.route('/')
def student():
  return render_template('index.html')
##if __name__ == "__main__:
  ##  app.run()
@app.route('/result' ,methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='sanjay'
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        result=request.form.to_dict()
        name=result['Name']
        phy=int(result['Matkul1'])
        che = int(result['Matkul2'])
        mat=int(result['Matkul3'])
        s=str((phy+che+mat)/3)
        result["Total"]=s
        mycursor.execute("insert into priyanka (name,phy,che,mat,total)values(%s,%s,%s,%s,%s)",(name,phy,che,mat,s))
        mydb.commit()
        mycursor.close()
        return render_template('test.html',result=result)
    return render_template("index.html")
app.run(debug=True)