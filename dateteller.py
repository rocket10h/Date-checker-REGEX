import re

def read_file(filepath):
    with open(filepath,'r') as file:
        return file.read()

def convertingdates(text):
    date_pattern=r'\b(\d{2})-(\d{2})-(\d{4})\b'
    converted=re.sub(date_pattern,r'\3-\2-\1',text)
    return converted

def main():
    text=read_file('dates.txt')
    converted_text=convertingdates(text)

    print(f"Converted text    =    {converted_text}")


if __name__ == "__main__":
    main()
