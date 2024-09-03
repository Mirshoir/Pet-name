from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate


def generate_pet_name(animal_type, animal_color):
    llm = Ollama(model="llama3")

    prompt_template_name = PromptTemplate(
        input_variables=['animal_name', 'pet_color'],
        template=f"generate 5 names for my {animal_type} in {animal_color}. print only names, do not add explanations",
        output_key="pet_name"
    )

    name_sequence = prompt_template_name | llm

    response = name_sequence.invoke({"animal_type": animal_type, "pet_color": animal_color})

    return response


petnames = generate_pet_name("cow", "black")
print(petnames)
