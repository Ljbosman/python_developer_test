python3 -m pip install --user virtualenv

virtualenv venv
chmod +x venv/bin/activate
source venv/bin/activate

pip3 install fuzzywuzzy
pip3 install python-Levenshtein

python3 csv_reader.py -i file.csv -s -l 25 -t -d "01 Jun 1999" "31 Aug 2007"

