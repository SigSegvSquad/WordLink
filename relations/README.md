# Word Relations

These are the word-pairs or tuples used in training or evaluating linear models for establishing word-pair relations

### Format

Follow the format below for adding pairs

```
TITLE
word1, pair1
word2, pair2
word3, pair3
⋮
```

### Naming

Name the file as (relation).txt. For example, all the below are valid
- `country-city.txt`
- `male-female.txt`
- `fruit-color.txt`

### Usage

All read and extract operations of these pairs will be done through [`../relations.py`]()