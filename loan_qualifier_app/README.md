# Loan_qualifier_app

Imagine a startup trying to sift through users information manually to determine if they qualify for a loan... no need with the loan qualifier app. Any determined qualifiers set by the lenders is easy to integrate and the app automatically sifts and sorts which qualifying loans they're accepted for! 

---

## Technologies
Python 3.10 was used for this project. 

Fire - allows the applciation to interact with the cli

Questionary - asks the users for input 

---

## Installation Guide
```
pip install fire
```
```
pip install questionary
```
---

## Usage
After you clone the repo, navigate to it, and install the dependencies, please follow the below guide and reference the pictures: 

-Run the application.

-Select the data .csv path you'd like to read from (the lenders qualifier data). 

-The user inputs their information. 

-The application automatically calculates the users information and compares them to the lenders qualifer data to see if they qualify for any loans. 

-If no, they're notified and the application closes. 

-If yes, they have the option to save the file. If they choose no, it closes. If they chose yes, they're asked what they'd like to name the file. 

-The qualifying data is written to that specficed file within the directory. 


*You'll see that in the first one, I had no qualifying loans so it notified me and exited.* 
![no_qualifying](https://user-images.githubusercontent.com/23126459/196345065-2e7a0598-aa9d-4f14-8775-2d7e1e1ce330.PNG)


*In the next one, I had 24 qualifiying loans and it saved to the directory as the specfied file name.*
![24_qualifying](https://user-images.githubusercontent.com/23126459/196345192-48ef1ab3-a597-400c-8dc5-422f37349093.PNG)


---

## Contributors

brockchecksmail@gmail.com

---

## License

MIT
