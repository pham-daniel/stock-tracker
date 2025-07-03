# Stock Tracker
This project was created to show the performance of certain indices and stocks, and contains a search function to lookup specific stocks.

## Prerequisites
Ensure that Python 3 is installed. To install, follow these steps:
- Download from [python.org](https://www.python.org/downloads/).
- Ensure that Python is added to your system's path.

## Installation
1. Clone the repository or download the project files:
```
git clone (repository https/ssh link)
```
2. Open your terminal or command prompt.
3. Navigate to the project's root directory:
```
cd stock-tracker
```
4. Install the necessary project packages:
```
pip install -r requirements.txt
```
If the above command does not work, use this command:
```
python -m pip install -r requirements.txt
```

## How to Run
1. If you are not currently in the root main directory, follow steps 2 and 3 of the installation section.
2. Run the main script using Streamlit:
```
streamlit run window.py
```
A Streamlit window should open in your browser, which will give access to the project's functions.

To disconnect:
1. Use Ctrl + C or Command + C in the terminal or command prompt.
2. Close the Streamlit window. 

## Project Structure
```
window.py            # Main script to display the information
stock.py             # Retrieves stock information and creates graphs
```
