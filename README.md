## The official Repo of the paper [MHPP: Exploring the Capabilities and Limitations of Language Models Beyond Basic Code Generation](https://arxiv.org/abs/2405.11430) 📄✨

Welcome to the official repository of our paper! 🎉

The dataset can be found in the `data` directory, which includes details of each question, such as the question's challenge type. The raw questions can be accessed using the 'question' field. We also provide a version of the prompt with a prefix for users, as mentioned in the paper. Creating this dataset was labor-intensive. If you find any errors, please submit an issue to provide feedback. Thank you very much! 🙏

The leaderboard is available at [MHPP Leaderboard](https://sparksofagi.github.io/MHPP/). 🏆

![MHPP Leaderboard](./fig/mhpp_leaderboard.png)

### To submit model results:

1. Run your model on our dataset in the `/data/` folder. You can either take the "prompt" field as input (as we do in the paper) or create a new input by adding more user instructions before or after the "question" field. 💻
2. Save the result in JSONL format. Remember to include the question ID, function name, and model response in each line. 📝
3. Click "[File a request](https://github.com/SparksofAGI/MHPP/issues/new?assignees=&labels=model+eval&projects=&template=model_eval_request.yml&title=💡+%5BREQUEST%5D+-+%3CMODEL_NAME%3E)" on the leaderboard page to create an issue, and upload the JSONL file in the "Model Response" part. 📤
4. Fill in other necessary information and submit. 📄
5. Wait. ⏳
6. Get your model result with a detailed report. 📊

Thank you for your interest and participation! 😊

