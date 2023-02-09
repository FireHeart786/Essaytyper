import wikipediaapi

def generate_essay(topic):
    # Initialize the Wikipedia API
    wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    
    # Get the page for the given topic
    page = wiki.page(topic)
    
    # Check if the page exists
    if page.exists():
        # Get the text from the page
        text = page.text
        
        # Split the text into sentences
        sentences = text.split(". ")
        
        # Initialize an empty list for the essay
        essay = []
        
        # Add the first few sentences to the essay until it reaches 450 words
        word_count = 0
        for i in range(len(sentences)):
            if word_count + len(sentences[i].split(" ")) < 450:
                essay.append(sentences[i])
                word_count += len(sentences[i].split(" "))
            else:
                break
        
        # Return the essay as a string
        return ". ".join(essay) + "."
    else:
        return "The page for the given topic does not exist."

# Call the generate_essay function
a= input("Enter the topic of Essay: ")
essay = generate_essay(a)

# Print the essay
print(essay)
