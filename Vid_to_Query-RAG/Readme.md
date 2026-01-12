#  How to use this RAG AI Teaching Assistant on your own data


## STEP 1 - Collect your videos
Move all your video files to the videos folder


## STEP 2  -  Convert to mp3_
Convert all the video file in mp3 by running video_to_mp3


## STEP 3 -  Convert mp3_to_json
Convert all the mp3 files to json by running mp3_to_json


## STEP 4 - Convert all the json files to vectors
Use the file preprocess_json to convert the json files to a dataframe with embedding and save it as a joblib picklE


## STEP 5 - Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM


## 🚀 Features

- Convert video files to audio (MP3)
- Transcribe audio using Whisper
- Store transcripts in structured JSON format
- Preprocess and chunk text data
- Generate and store embeddings using Joblib
- Perform semantic search using cosine similarity
- Lightweight and fully local (no paid APIs required)

---

## 🧠 Tech Stack

- *Python 3.9+*
- *Whisper (Speech-to-Text)*
- *NumPy & Pandas*
- *Scikit-learn (Cosine Similarity)*
- *Joblib (Embedding Storage)*
- *FFmpeg (Video/Audio Processing)*
-  *bge-m3(for embedding)
-  *llama3.2(for LLM output/ generated response)