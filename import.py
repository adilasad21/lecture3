import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker

db_string = "postgres://aadil:aadil@localhost:5432/postgres"

engine = create_engine(db_string)
db = scoped_session(sessionmaker(bind=engine))

def main():
  f = open("flights.csv")
  reader = csv.reader(f)
  
  for origin, destination, duration in reader: # loop gives each column a name
      db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                  {"origin": origin, "destination": destination, "duration": duration})
      print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
  db.commit() 
    
if __name__== "__main__":
  main()