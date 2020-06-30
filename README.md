# Python Developer Test

This is a python script designed for the purpose of a technical assessment.

## Usage

```bash
./scripts/setup.sh

python csv_reader.py -h
```

Alternatively you can execute 
```bash
./scripts/run.sh
```

I have also included a demo.sh with example args given:
```bash
./scripts/setup.sh # If you haven't yet

./scripts/demo.sh
```

## Testing
To run the tests you can simply run:
```bash
./scripts/setup.sh # If you haven't yet

./scripts/test.sh
```

## Notes
#### Regarding the tenants dictionary
I am aware that this is a very naive way of implementing it. Looping through every key of the dictionary and checking
where a similar key is (Levenshtein distance) is slow. 
One way this can be improved is by using a Trie. This means building up a tree where each node represents a partial or 
complete word. In this case it would be representing a letter at each node. Then each node would have a branch for each
letter that may follow it in our list of words. By using this structure we can write a search function that can return
a key closely matching our given tenant name which would be considerably faster than the current loop (important to note
that this would also mean more memory usage because the trie is stored in memory). 
I did not implement it this way because I believed that would be 'overthinking but I felt it was important to mention 
improvements.

Another note about this function is the fuzz ratio of 51%. This can be fine tuned I believe to avoid false positive
matching. If set to 50% we have many false positives, including examples like "dood" and "dodo". For the dataset
provided the lowest ratio I saw for the same company name was 56% and then I added 5% as a buffer for in case another
entry was added for the same company with a slightly smaller ratio. For this dataset as is, 56% could have been used.

## Lambda vs Loop
I'm not 100% sure what the performance difference here is for the code I wrote, but I believe with the size of this
data set, the performance difference wouldn't have been noticeable. I felt lambdas were easier to read here so it made
the most sense for me. This can of course be discussed and I would love feedback on if for loops would have been the 
better option in this case.
