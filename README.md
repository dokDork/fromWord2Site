# fromWord2Site
[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)  
<img src="https://raw.githubusercontent.com/dokDork/fromWord2Site/refs/heads/main/images/fromWord2Site.jpg" width="250" height="250">  

## Description
Starting from a list of words create a list of site name.
In addition to the word list, to get the list of websites, you need to provide a comma-separated list of prefixes (e.g. www,api,login) and a comma-separated list of suffixes (e.g. com,ctf,online).
It generates an output file, containing the list of generated websites, which is called like the file with the list of words given as input but with the extension .output

## Example Usage
 ```
python3 fromWord2Site.py wordList.txt www,api,login com,ctf,online
 ``` 

## Command-line parameters
```
python3 fromWord2Site.py <words list> <prefixes comma-separated> <suffixes comma-separated>
```

| Parameter | Description                          | Example       |
|-----------|--------------------------------------|---------------|
| `worss list`      | text file containing a list of words separated by the enter character | `words.txt` |
| `prefixes comma separated`      | comma separated list of prefixes  | `www,api,login`          |
| `suffixes comma separated`      | comma separated list of suffixes  | `com,crf,online`          |
  
## How to install it on Kali Linux (or Debian distribution)
It's very simple  
```
cd /opt
```
```
git clone https://github.com/dokDork/fromWord2Site.git
```
