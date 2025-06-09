# %%
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)
base_dir = Path().resolve().parent

# %%
from langchain.chat_models import ChatOpenAI
llm_model = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature=0.9, model=llm_model)

# %%
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader(f"{base_dir}/data/CourseOutline.pdf")
pages = loader.load()
# print(pages)  # Print the content of the first page

# async for page in loader.alazy_load():
#     print(page)

# %%
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
embed = embeddings.embed_query("What is the course about?")
print(embed)  # Print the embedding for the query

# %%
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embeddings,
).from_loaders([loader])

print(index.query("Can you tell me how many lecture student going to have and more schedule details if possible?", llm=llm))  # Query the index

# %%


# %%


# %%


# %%



