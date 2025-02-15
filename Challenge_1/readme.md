This model is designed to perform transliteration from Banglish (Romanized Bengali) to Bengali script using the [facebook/mbart-large-50-many-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) model. The training was conducted using the dataset [SKNahin/bengali-transliteration-data](https://huggingface.co/datasets/SKNahin/bengali-transliteration-data).

The notebook used for training can be found here: [Kaggle Notebook](https://www.kaggle.com/code/shadabtanjeed/mbart-banglish-to-bengali-transliteration).

You can also find it on Hugging Face: [Hugging Face Repo](https://huggingface.co/shadabtanjeed/mbart-banglish-to-bengali-transliteration)

## Model Details

### Model Description

- **Developed by:** Shadab Tanjeed
- **Model type:** Sequence-to-sequence (Seq2Seq) Transformer model
- **Language(s) (NLP):** Bengali, Banglish (Romanized Bengali)
- **Finetuned from model:** [facebook/mbart-large-50-many-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)

### Model Sources

- **Repository:** [facebook/mbart-large-50-many-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)

## Uses

### Direct Use

The model is intended for direct transliteration of Banglish text to Bengali script.

### Downstream Use

It can be integrated into NLP applications where transliteration from Banglish to Bengali is required, such as chatbots, text normalization, and digital content processing.

### Out-of-Scope Use

The model is not designed for language translation beyond transliteration, and it may not perform well on text containing mixed languages or code-switching.

## Bias, Risks, and Limitations

- The model may struggle with ambiguous words that have multiple possible transliterations.
- It may not perform well on informal or highly stylized text.
- Limited dataset coverage could lead to errors in transliterating uncommon words.

### Recommendations

Users should validate outputs, especially for critical applications, and consider further fine-tuning if necessary.

## How to Get Started with the Model

```python
from transformers import MBartForConditionalGeneration, MBartTokenizer

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

text = "ami tomake bhalobashi"
inputs = tokenizer(text, return_tensors="pt")

translated_tokens = model.generate(**inputs)
output = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

print(output)  # Expected Bengali transliteration

```

## Training Details

### Training Data

The dataset used for training is [SKNahin/bengali-transliteration-data](https://huggingface.co/datasets/SKNahin/bengali-transliteration-data), which contains pairs of Banglish (Romanized Bengali) and corresponding Bengali script.

### Training Procedure

#### Preprocessing

- Tokenization was performed using the mBART tokenizer.
- Text normalization techniques were applied to remove noise.

#### Training Hyperparameters

- **Batch size:** 8
- **Learning rate:** 3e-5
- **Epochs:** 5

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

- The same dataset [SKNahin/bengali-transliteration-data](https://huggingface.co/datasets/SKNahin/bengali-transliteration-data) was used for evaluation.

## Technical Specifications

### Model Architecture and Objective

The model follows the Transformer-based Seq2Seq architecture from mBART.

#### Software

- **Framework:** Hugging Face Transformers

## Citation

If you use this model, please cite the dataset and base model:

```bibtex
@inproceedings{SKNahin2023,
  author = {SK Nahin},
  title = {Bengali Transliteration Dataset},
  year = {2023},
  publisher = {Hugging Face Datasets},
  url = {https://huggingface.co/datasets/SKNahin/bengali-transliteration-data}
}

@article{lewis2020mbart,
  title={mBART: Multilingual Denoising Pre-training for Neural Machine Translation},
  author={Lewis, Mike and others},
  journal={arXiv preprint arXiv:2001.08210},
  year={2020}
}
```
