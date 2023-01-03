from flask import Flask,request,render_template
import requests

app=Flask(__name__)

# @app.route("/")
# def fun():
#     url="https://api.mfapi.in/mf/120185"
#     resp=requests.get(url)
#     return render_template("index.html",data=resp.json().get("data")[0].get("nav"))

l=[139619,148921,149383]
ll=[]
@app.route("/")
def fun():
    for i in range(len(l)):
        url="https://api.mfapi.in/mf/"+str(l[i])
        resp=requests.get(url)
        temp=resp.json()
        id=temp.get("meta").get("scheme_code")
        house=temp.get("meta").get("fund_house")
        nav=temp.get("data")[0].get("nav")
        dic={"id":id,'house':house,"nav":nav}
        ll.append(dic)
    return render_template("index.html",data=ll)

if __name__=="__main__":
    app.run(debug=True)