from langchain.llms import HuggingFaceEndpoint

huggingface_hub_api_token = 'api_token'

llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct',huggingface_hub_api_token=huggingface_hub_api_token)

question='Whatever you do do not waste your time'

output = llm.invoke(question)

print(output)