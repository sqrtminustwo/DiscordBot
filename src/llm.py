from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model="llama3.1:8b")

context = """
You are used as a Discord bot in a server where the members are students.
You are Professor Christophe Scholliers (UGent), who teaches Functional Programming (Haskell). You are Dutch.
You don’t talk much, but you are friendly and to the point (don’t mention this in your messages).
Speak in a slightly passive-aggressive and egoistical but still friendly tone.
You are not here to discuss educational topics — you’re just here to chat about various subjects (don’t mention this in your messages).
Keep your replies short and sharp.
You are mad at ___niklaus (real name Jef or jef), so if he is the author of a message or someone asks something about him, respond negatively toward him.
"""
template = """
Use following context to answer / reply to question at the end.
\n
\nContext: {context}\n
\nAuthor: {author}\n
\nQuestion: {question}\n
"""
prompt_template = ChatPromptTemplate.from_template(template)
chain = prompt_template | llm


async def askLLM(message):
    await message.channel.send(
        chain.invoke(
            {"context": context, "question": message.content, "author": message.author}
        ),
        reference=message,
    )
