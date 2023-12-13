from sentence_transformers import SentenceTransformer
import json

# create embedding for the peom's text
def get_embedding(text, model):
   text = text.replace("\n", " ")
   return model.encode(text, normalize_embeddings=True)

# generate embeddings for all the poems
def generate_embeddings(poem_data, model):
   embeddings = {}
   for i in range(len(poem_data)):
      index = i + 1
      title = poem_data[str(index)]['title']
      text = poem_data[str(index)]['text']
      embeddings[title] = get_embedding(text, model)
   return embeddings

# determine the most relevant poems based on cosine similarity
def closest_poems(embeddings, target):
  scores = {}
  for poem in embeddings:
    embedding = embeddings[poem]
    score = target @ embedding.T
    scores[poem] = score
    
  sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
  best_five = sorted_scores[:5]
  return best_five

# determine the five closest poems to query
def find_five_closest_poems(query):
  model = SentenceTransformer('BAAI/bge-large-zh-v1.5')
  poem_data = {} #dictionary poems
  with open('poem_data.json', 'r') as file:
    poem_data = json.load(file)
  print(poem_data)
  embeddings = generate_embeddings(poem_data, model)
  target = get_embedding(query, model)
  best_five = closest_poems(embeddings, target)
  return best_five

# user inputs a poem
def main():
  query = input("Please enter a poem that you would like analyzed:\n")
  best_five = find_five_closest_poems(query)
  result = ""
  for poem, score in best_five:
    result += f"Title: {poem}, Score: {score:.4f}\n"
  print(result)

if __name__ == "__main__":
   main()