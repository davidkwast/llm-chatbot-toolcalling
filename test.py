from langchain.chat_models import init_chat_model

model = init_chat_model("granite3.3:2b", model_provider="ollama")

print(model.invoke("Hello, world!"))