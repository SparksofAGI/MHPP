## The official Repo of the paper [MHPP: Exploring the Capabilities and Limitations of Language Models Beyond Basic Code Generation](https://arxiv.org/abs/2405.11430)

The dataset can be found in the data directory, which includes details of each question, such as question's challenge type. The raw questions can be accessed using the 'question' field. We also provide a version of the prompt with a prefix for users, as mentioned in the paper. Creating this dataset was labor-intensive. If you find any errors, please submit an issue to provide feedback. Thank you very much!

The leaderboard is availalable at [MHPP Leaderboard](https://sparksofagi.github.io/MHPP/).

![mhpp_leaderboard](./fig/mhpp_leaderboard.png)

To submit model result:

1. Run model on our dataset in folder /data/, you can either take "prompt" field as input (as we do in paper) or create a new input by adding more user instructions before or after "question" field.
2. Save result in jsonl format, remember to include the question ID, function name and model response in each line.
3. Click "[File a request](https://github.com/SparksofAGI/MHPP/issues/new?assignees=&labels=model+eval&projects=&template=model_eval_request.yml&title=💡+%5BREQUEST%5D+-+%3CMODEL_NAME%3E)" on leaderboard page to create an issue, upload jsonl file in "Model Response" part.
4. Fill in other necessary infomation and submit.
5. Wait.
6. Get you model result with a detailed report.
