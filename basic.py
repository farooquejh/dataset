from exception import customexception
from logger import logging




class Car:
  def __init__(self,brand,model,year,max_speed):
    self.brand=brand
    self.model=model
    self.year=year
    self.max_speed=max_speed
    self.current_speed=0
    self.engine_on=False




  def start_engine(self):
    try:
      logging.info("starting of engine ")
      if not self.engine_on:
        self.engine_on=True
        print(f" the engine is onn now of {self.brand} and {self.model}")
        logging.info(f" the engine is onn now of {self.brand} and {self.model}")
      else:
        print("engine is already onn")
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



  def stop_engine(self):
    try:
      logging.info("stop of engine ")
      if self.engine_on and self.current_speed==0:
        self.engine_on=False
        print(f" the engine is  now off {self.brand} and {self.model}")
        logging.info(f" the engine is  now off {self.brand} and {self.model}")
      else:
        print("the engine is already off")
    except Exception as e:
        logging.info("exception in stop_engine...")
        raise customexception(e,sys)
        


  def car_accereration(self,increament):
    try:
      logging.info("car in accerelatin ")
      if self.engine_on:
        self.current_speed +=increament
        if self.current_speed>self.max_speed:
          self.current_speed=self.max_speed
          print(f" the maximum _speed running of car {self.max_speed}")
      else:
        print(f"the car is running at current_speed {self.current_speed}")
    
    except Exception as e:
        logging.info("exception in car_acceraration...")
        raise customexception(e,sys)

  def brake(self, decrease):
    try:
        logging.info("car in brake mode ")
        if self.current_speed > 0:
            self.current_speed -= decrease
            if self.current_speed < 0:
                self.current_speed = 0
            print(f"The car is running at a speed of {self.current_speed} km/h!")
            logging.info(f"The car is running at a speed of {self.current_speed} km/h")
        else:
            print("The car is stationary")
            logging.info("The car is stationary")
    except Exception as e:
        logging.info("Exception in car deceleration logic...")
        raise customexception(e, sys)
            

      
def info_car(self):
    print(f"{self.brand}")
    print(f"{self.model}")
    print(f"{self.year}")
    print(f"{self.max_speed}")
    print(f"{self.current_speed}")
    print(f"{self.engine_on}")





if __name__ == "__main__":
    my_car = Car("Ford", "Mustang", 2023, 200)
    my_car.start_engine()
    my_car.car_accereration(179)
    my_car.brake(69)
    my_car.stop_engine()