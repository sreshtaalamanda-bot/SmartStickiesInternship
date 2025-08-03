import ollama

def construct_product(name, category, description):
    prompt = "Generate a 5 sentence product description for a product named " + name + " with the category " + category + ". The description should be engaging and informative, highlighting the key features and benefits of the product do not include a title or heading. Here is a brief description: " + description
    return prompt

#user input
print("--Welcome to the Product Builder Demo--")
print("Firstly, what is the name of your product?")
name = input("Product Name: ")
print("If you could summarize the use of the product in one word, what would it be? (E.g: 'sports', 'entertainment', 'educational')")
category = input("Category: ")
print("Please provide a brief 2-3 sentence description of your product.")
description = input("Description: ")

#generate response
response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": construct_product(name, category, description),
        },
    ],
)

print("--"+name+"--")
print("Category: " + category)
print(response["message"]["content"])

