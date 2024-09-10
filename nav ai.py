import openai


openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_brand_awareness_content(brand_name, target_audience, platform, theme):
    """
    Generate content for brand awareness using OpenAI GPT model.

    Parameters:
    brand_name (str): Name of the brand.
    target_audience (str): Description of the target audience (e.g., age group, interests).
    platform (str): Platform where the content will be published (e.g., social media, blog).
    theme (str): Theme or focus of the content (e.g., product benefits, customer stories).

    Returns:
    str: Generated content for brand awareness.
    """
    prompt = f"Create a brand awareness message for {brand_name} targeting {target_audience} to be posted on {platform}. The message should focus on {theme}."

    try:
        
        response = openai.Completion.create(
            engine="text-davinci-003",              
            max_tokens=150,  
            n=1,
            stop=None,
            temperature=0.7  
        )

        # Extract the generated text from the response
        generated_content = response.choices[0].text.strip()
        return generated_content

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    
    brand_name = "Nav AI"
    target_audience = "young entrepreneurs and startups"
    platform = "LinkedIn"
    theme = "innovative AI solutions for marketing and branding"

    
    content = generate_brand_awareness_content(brand_name, target_audience, platform, theme)
    
    if content:
        print("Generated Content for Brand Awareness:")
        print(content)
    else:
        print("Failed to generate content.")
