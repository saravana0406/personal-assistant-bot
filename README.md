# Smart Task Executor – Personal Assistant using LSTM

Smart Task Executor is an AI-powered personal assistant system built using Recurrent Neural Networks (LSTM). It processes user input, identifies intent, and executes tasks such as retrieving system information, opening applications, and responding to basic queries.

---

## Features

* Intent detection using LSTM (RNN)
* Command-based chatbot interface
* Retrieve current system time
* Open browser/applications
* Basic weather responses
* Modular and scalable architecture

---

## Project Structure

```
smart-task-executor/
│
├── data/
│   └── intents.json
│
├── model/
│   ├── chatbot_model.h5
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── actions.py
│   └── utils.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## System Workflow

1. User provides input as a text command
2. Input is preprocessed using tokenization and padding
3. The LSTM model predicts the user intent
4. The system maps the intent to a predefined task
5. The task is executed and a response is returned

---

## Installation

### Clone the Repository

```
git clone https://github.com/your-username/smart-task-executor.git
cd smart-task-executor
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## Usage

### Train the Model

```
python src/train.py
```

### Run the Application

```
python app.py
```

---

## Sample Interaction

```
User: What is the time?
Bot: 14:32:10

User: Open chrome
Bot: Opening browser...
```

---

## Technology Stack

* Python
* TensorFlow (LSTM / RNN)
* NumPy
* Scikit-learn

---

## Future Enhancements

* Voice-based interaction
* Integration with real-time APIs (weather, news)
* Persistent memory for reminders
* Web-based user interface (Flask or Streamlit)
* Upgrade to Transformer-based models

---

## Limitations

* Limited intent dataset
* No long-term conversational memory
* Basic response handling

---

## Application

This project demonstrates a task-oriented conversational AI system that can be extended into virtual assistants, automation tools, and smart interfaces.

---

## Acknowledgement

Inspired by modern virtual assistant systems used in real-world applications.

---

## Contact

For improvements or collaboration, feel free to reach out.

---

If you find this project useful, consider starring the repository.
