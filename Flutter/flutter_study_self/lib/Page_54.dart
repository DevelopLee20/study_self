void main(){
  Car one = Car(320,10000,'one');
  Car two = Car(250,1000,'two');

  one.sale();
  two.sale();
}

class Car{
  int speed;
  num price;
  String name;

  Car(int speed, num price, String name){
    this.speed = speed;
    this.price = price;
    this.name = name;
  }

  int sale(){
    price = price * 0.9;
    return price;
  }
}