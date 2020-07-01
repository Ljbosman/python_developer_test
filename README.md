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
### Lambda vs List Comprehension
I'm not 100% sure what the performance difference here is for the code I wrote, but I believe with the size of this
data set, the performance difference wouldn't have been noticeable. I added both as a showcase but in a production
environment I would use only one for consistency in code.

### Regarding the tenants dictionary (Please see branch "tenant-matching")
After implementing the tenants dictionary, I read through the requirements again and saw **treat these as
individual tenants**, which is not how I did it initially. Initially I treaded **Vodafone LTD** and **Vodafone LTD.**
as the same tenant. I removed it from my submission but thought I'd add the note here in case you wanted to see the
tenant matching logic as well.

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
