# Python Developer Test

This is a python script designed for the purpose of a technical assessment.

## Usage

```bash
python -m pip install --user virtualenv

virtualenv venv
chmod +x venv/bin/activate
source venv/bin/activate

pip install fuzzywuzzy
pip install python-Levenshtein # To make fuzz run faster otherwise it uses a python-pure implementation which is slower

python csv_reader.py -h
```

Alternatively you can execute run.sh to skip the steps above

I have also included a demo.sh with example args given
