from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="a simp ;( API server"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"    
# )
# model = ChatOpenAI()

llm = Ollama(model="llama3")


# prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

# add_routes(
#     app,
#     prompt1|model,
#     path="/essay"
# )

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8200)
