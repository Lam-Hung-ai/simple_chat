from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel
from typing import Type

def get_info(thong_tin_buu_kien: str, instruction: str, api_key: str):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)
    context = []
    context.append(SystemMessage(content=instruction))
    context.append(HumanMessage(content=f"Nội dung bưu kiện: {thong_tin_buu_kien}"))
    response = llm.invoke(context)
    return response.content

def get_info_with_structure(thong_tin_buu_kien: str, instruction: str, schema: Type[BaseModel], api_key: str):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key).with_structured_output(schema=schema)
    context = []
    context.append(SystemMessage(content=instruction))
    context.append(HumanMessage(content=f"Nội dung bưu kiện: {thong_tin_buu_kien}"))
    response = llm.invoke(context)
    return response