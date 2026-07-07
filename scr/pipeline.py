from pipeline import RAGPipeline


bot = RAGPipeline("Introbiology.pdf")

bot.build()

answer = bot.ask(
    "What is mitochondria?"
)

print(answer)
