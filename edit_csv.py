import csv
import pandas as pd


def read_csv():
    csv_data = []
    csv_path = "mhpp.csv"
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    return csv_data


def read_excel():
    excel_path = "excels/MHPP Analysis.xlsx"
    df = pd.read_excel(excel_path, sheet_name="MHPP_benchmark_final_plan")
    data = [
        {"model": x,
         "total_greedy": f"{y * 100:.1f}%",
         "link": z} for x, y, z in zip(
            df.iloc[:, 1].tolist(), df.iloc[:, 10].tolist(), df.iloc[:,11].tolist())
    ]
    new_data = []
    for line in data[:21]:
        if not line["total_greedy"] or line["total_greedy"] == "nan%":
            continue
        new_data.append(line)
    return new_data


def manual_data():
    greedy_data = {
        "Llama2 Chat 7b": "2.9%",
        "Llama2 Chat 13b": "2.1%",
        "Mistral 7b": "7.9%",
        "Phi 1": "12.9%",
        "Phi 1.5": "8.6%",
        "Phi 2": "13.6%",
        "CodeLlama 7B": "3.6%",
        "CodeLlama 13B": "5.0%",
        "CodeLlama 7B Instruct": "8.6%",
        "CodeLlama 13B Instruct": "15.0%",
        "CodeLlama 34B Instruct": "16.4%",
        "CodeLlama 7B Py": "3.6%",
        "CodeLlama 13B Py": "5.0%",
        "CodeLlama 34B Py": "9.3%",
        "DeepSeek Instruct 1.3B": "11.4%",
        "DeepSeek Instruct 6.7B": "22.9%",
        "DeepSeek Instruct 33B": "38.6%",
        "WizardCoder-33B-V1.1": "31.4%",
        "WizardCoder-Python-34B-V1.0": "22.9%",
        "GPT-3.5 (gpt-3.5-turbo)": "27.9%",
        "GPT-4 (gpt-4-1106-preview)": "53.6%",
    }
    return greedy_data


def save_csv(path, data):
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    print("{} saved".format(path))


def main():
    greedy_data = manual_data()
    csv_data = read_csv()
    for idx, line in enumerate(csv_data):
        if idx == 0:
            line.append("Greedy")
        else:
            line.append(greedy_data[line[0]])

    excel_data = read_excel()
    for line in excel_data:
        new_line = [line["model"]] + ["-"] * 17 + [line["link"], line["total_greedy"]]
        csv_data.append(new_line)
    output_csv = "new_mhpp.csv"
    save_csv(output_csv, csv_data)


if __name__ == '__main__':
    main()
