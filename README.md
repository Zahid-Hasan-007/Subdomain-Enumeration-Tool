# Subdomain Enumeration Tool

This tool is designed to discover subdomains of a target domain using a wordlist. It makes HTTP requests to each subdomain and checks if the request is successful (status code 200).

## Features

- Discovers subdomains of a target domain
- Checks for valid subdomains using HTTP requests
- Displays discovered subdomains

## Technologies Used

- Python
- requests library
- multiprocessing module

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/subdomain-enumeration-tool.git


## Install dependencies

```sh
pip install requests
```

## Usage

1. Provie the 'target_URL' variable in the 'main' function
2. Run the script
```sh
python subdomain_enumeration.py
```
3. The script will read a wordlist from 'subdomainwordlist.txt' and make requests to each subdomain.
4. Valid subdomains will be displayed in the console.

## Optimization

- Uses 'requests.Session' to reuse connections for faster requests
- Uses 'multiprocessing.Pool' to parallelize requests for improved performance

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

