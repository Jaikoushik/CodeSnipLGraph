from langchain_groq import ChatGroq

class GroqChat: 

    def __init__(self,prompt,MODEL):
        self.prompt = prompt
        self.MODEL = MODEL

    from dotenv import load_dotenv
    load_dotenv()   
    def chat(self):
        model = ChatGroq(model = self.MODEL)
        return model.invoke(self.prompt)
    

a = GroqChat("What is the capital city of France?","llama-3.3-70b-versatile")

print(a.chat().content)

