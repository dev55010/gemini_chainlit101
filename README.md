# Gemini Chainlit Demo

This project demonstrates how to integrate the Gemini API with Chainlit to create a chatbot application. The chatbot can process user messages and generate responses using the Gemini model.

## Project Structure

```
.env
.gitignore
chainlit.md
gemini_chainlit.py
LICENSE
README.md
requirements.txt
run01.py
run02.py
```

- `.env`: Contains environment variables, including the Gemini API key.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `chainlit.md`: Contains the welcome screen content for the Chainlit application.
- `gemini_chainlit.py`: Main script to run the Chainlit application with the Gemini API.
- `LICENSE`: MIT License for the project.
- `README.md`: Project documentation (this file).
- `requirements.txt`: List of Python dependencies required for the project.
- `run01.py`: Script to test the Gemini API without Chainlit.
- `run02.py`: Script to run the Chainlit application with the Gemini API.

## Setup

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd gemini_chainlit101
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**

   Create a `.env` file in the root directory and add your Gemini API key:

   ```properties
   GEMINI_API_KEY="your_gemini_api_key"
   ```

## Running the Application

### Running with Chainlit

To run the Chainlit application, use the `gemini_chainlit.py` script:

```sh
python gemini_chainlit.py
```

### Running without Chainlit

To test the Gemini API without Chainlit, use the `run01.py` script:

```sh
python run01.py
```

To run the Chainlit application with the Gemini API, use the `run02.py` script:

```sh
python run02.py
```

## Usage

- **Chainlit Application:** Open your browser and navigate to the URL provided by Chainlit. You will see a welcome message and can start interacting with the chatbot.
- **Testing the API:** The `run01.py` script will print the response from the Gemini model to the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Chainlit](https://docs.chainlit.io) for providing the framework to build the chatbot.
- [Google Generative AI](https://cloud.google.com/generative-ai) for the Gemini API.

## Contact

For any questions or inquiries, please contact the project maintainer.