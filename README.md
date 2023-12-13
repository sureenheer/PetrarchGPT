# PetrarchGPT

## Description:

PetrarchGPT is a semantic search engine that accepts any text input and outputs which one of Petrarch’s 366 poems most closely resembles this input along with a similarity score. The poems are taken from Peter Sadlon's website (https://petrarch.petersadlon.com/canzoniere.html) and processed into a JSON file. All the poems are translated from Italian to English by A.S. Kline. 

## General Overview of the program

First, I transform each poem into a text embedding, which is a vector representation of the text. I use the BAAI/bge-large-zh-v1.5 sentence transformer model by FlagEmbedding to create these embeddings. When a user inputs some text in the terminal, this text is transformed into an embedding and then this embedding is compared against all the other embeddings of the poems. The cosine similarity between the input embedding and each poem embedding is calculated. The five poems with the highest similarity scores are outputted in the terminal along with the poem text.

## How to run this program

1. Download the PetrarchGPT directory.
2. Then, on your terminal, navigate to the PetrarchGPT directory.
3. Type the following command: python3 PetrarchGPT.py (assumes you have python installed on computer)
4. Follow the command prompt and enter your input.

## Files in the PetrarchGPT directory:

1. PetrarchGPT.py (the main program)
2. poem_data.json (processed poems in JSON format)
3. process_poems.py (code used to process the poems)
4. the_canzoniere.txt (the TXT file I cleaned up from Peter Sadlon's website)
