![banner](https://github.com/SigSegvSquad/WordLink/blob/master/assets/Wordlink.png)

### Notebook Links
- [Custom Embeddings](https://colab.research.google.com/drive/1wlRmxgJzMU0zxT7z5rZVKCgZRE7ZHg0t)
- [Eigen Space](https://colab.research.google.com/drive/1RaUc9hsNj52FGNl3-1MhU3EXxcjsgTXK?usp=sharing)

### Problem Statement
To establish a concrete mathematical relation between common word pair relations and then to improve the performance of word embeddings by integrating word pair relations.

### Approaches
#### Modify an Existing Word2VecModel
- Use Pre-existing Model to establish relations (one-one) with regression.
- Establish relationship word tuples .
- Convert said word tuples to vector tuples using multiple word2vec models.
- Find a subspace using regression that satisfies this relation.

#### Create Custom Embeddings
- Created a model with set word relation in mind.
- Injected word pairs of that relation while training our own word2vec model.
