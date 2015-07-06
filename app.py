from flask import Flask, render_template
import requests
app = Flask(__name__)


#Move to CACHE
CARS =  {}


resp_vList_Mock = {
  "1234": {
    "image": "http://www.digitaltrends.com/wp-content/uploads/2013/02/bmw-3-series-gt-leak-2_1035.jpg",
    "make": "BMW",
    "model": "3-series",
    "price": 40000
  },
  "5678": {
    "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/2011_Mazda_MX-5_PRHT_--_04-28-2011.jpg",
    "make": "Mazda",
    "model": "Miata",
    "price": 25000
  }
}



#Move
def loadData():
  #Replace with cache object
  global CARS
  CARS = requests.get('http://146.148.50.170:3000/api/vehicles').json()





@app.route("/")
@app.route("/index")
def main():

    return render_template('index.html', data=CARS)


@app.route("/info/<carId>")
def info(carId):
    data = CARS.get(carId)
    if not data:
      #ToDo
      #Car not found, may need to update cache or return to index
      raise NotImplementedError
    return render_template('info.html', data=data)








if __name__ == "__main__":
    loadData() #Move to init
    app.run(debug=True)
