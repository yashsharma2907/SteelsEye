# SteelsEye
## Solution:
Prerequirements:
Python3+,pip3
1) We have to install FastApi using the terminal commands:
2)cd src/
3)pip install fastapi
4)pip install "uvicorn[standard]"
##Run the file using the command:
uvicorn api:app --reload
## I have created a data.csv file for fetching the data into it.
## I have created routes "/trades/filter" and implement callback function inside it using conditional statements and loops ,
i have implemented the search operations for "asset_class","start","end","maxPrice","minPrice","tradeType".
## Testing:
##For testing Swagger UI is used :
1) Follow the link: http://127.0.0.1:8000/docs
2) Now fill the entry and get your search results.
