# CS325 Project 3

## Due Date: 04/01 [No Extension]
## Points: 150

### Project Description:

1. Utilize the repository from Project 2. You can create a separate branch for this project.
2. Develop a program to connect to the OpenAI/Gemini (Bard) API or LLM (Large Language Model) API. You must register an account with them to access their API.
3. Upon registration with an LLM account, generate a token akin to an access token, which will be required for API calls to the LLM model.
4. Connect to the LLM API and send a prompt to the model. For instance, "Please make the article concise, up to 50 words. The article is: '...The content of the article...'" Modify the prompt as needed. The LLM model will respond with an approximately 50-word concise description of the provided article.
5. Save the returned text in a file. This file should include the original title of the content along with the concise article. If the title is not saved, utilize the LLM model to generate a suitable title based on the concise or raw article.
6. Repeat the process for at least 10 articles.

### Rubric:

1. **Documentation for LLM API Setup** (30 points):
    - Add a section to the README explaining how to create an LLM API account, generate a Key, and use the Key to make API calls. Screenshots can be used for illustration.

2. **YAML File Update** (10 points):
    - Update the YAML file if necessary.

3. **Code Comments** (30 points):
    - Ensure comprehensive commenting throughout the codebase for clarity and understanding.

4. **Project File Structure** (10 points):
    - Maintain the project-2 file structure and add folders/files as required.

5. **Article Conciseness** (70 points):
    - Successfully generate a concise version of at least 10 articles, including titles.

For any queries regarding the project, please reach out either before or after class. Further explanations will be provided in the next class session.

**Submission Instructions:**
- Provide the GitHub link to the TA.
- Bundle all project files into a zip folder and upload it to MOODLE.

---

### Setting up LLM API Account and Key Generation:

1. **Registration**:
   - Visit the OpenAI website and sign up for an account. https://openai.com/
   - When asked make sure to select the API option

2. **Account Activation**:
   - Follow the activation steps sent to your registered email address.

3. **Generate API Key**:
   - After registration, you should be presented with the documentation page
   - Click on "API Keys" to begin the first process of generation of an API Key.
   - CLick on the ```+ Create new secret key``` and name it. Make sure to copy it because we will be using it later

https://github.com/Tearever/ScrapingTheeWeb/assets/146034304/f2fc4c5a-baa7-4d6e-8064-9a7a0ee993bf


4. **Using the API Key**:
   - Once generated, the API Key will be provided. Use this key in your program to authenticate API requests.
   - When developing this program, I used an environment variable to store the API Key, but this is not required for your testing.
   - You are welcome to try this, but I left ```#api_key = ""```, if you want to quickly test it.
   - just comment out ```api_key = os.environ.get("OPENAI_API_KEY")``` and place your key within the ```api_key = "key"```
  
https://github.com/Tearever/ScrapingTheeWeb/assets/146034304/f7c0ab85-49f9-4099-902a-93b142556940





---
